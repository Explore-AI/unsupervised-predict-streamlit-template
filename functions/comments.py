from datetime import datetime
import streamlit as st
import functions.CRUD.CREATE as create
import functions.CRUD.READ as read

def commenter(yr):

    read.select()

    form = st.form(yr + "comments")
    name = form.text_input("Name")
    comment = form.text_area("Comment")
    submit = form.form_submit_button("Share comment")

    if submit:
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        par = [name, comment, date]
        create.insert(par)
        if "just_posted" not in st.session_state:
            st.session_state["just_posted"] = True
        st.experimental_rerun()