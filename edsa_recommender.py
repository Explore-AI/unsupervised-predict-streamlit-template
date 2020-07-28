"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np
import random

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Homepage","Recommender System","Solution Overview","Data & Insights","Diversity Statistics",
                    "Mzansi Movie Magic","Female Directed Films","Diversity in Films","Quote of the Day","Our Team"]

    # define mzansi list
    mzansi = ['Hijack Stories (2000): A 2000 South African crime film directed by Oliver Schmitz.',
              'Glory Glory (2000): The film was also marketed under the title Hooded Angels.',
              'State of Denial (2003): Documentary film about AIDS in Africa',
              'Red Water (2003): Horror film starring Lou Diamond Phillips',
              'Stander (2003 ): Biographical film about Captain André Stander - South African police officer turned bank robber',
              'Boy Called Twist (2004): Tells the story of a Cape Town street kid based on Charles Dickens’ classic 1838 novel Oliver Twist.',
              'Drum (2004): Life of South African investigative journalist Henry Nxumalo who worked for Drum magazine -  the first black lifestyle magazine in Africa.',
              'Engagement (2005): A film directed by Bryony and Mark Roughton.',
              'Bunny Chow (2006): Weekend journey of four stand up comedians who embark on a road trip to Oppikoppi.',
              'Faith Like Potatoes (2006): Biographical drama film based on the 1998 book written by Angus Buchan',
              'Running Riot (2006): Based on a play by Paul Slab Slabolepsky',
              'Tengers (2007): Animation produced in South Africa and uses the claymation technique',
              'Angels in the Dust (2007): The film follows Marion Cloete - a university-trained therapist who leaves behind her life of privilege in Johannesburg to build Boikarabelo',
              "Counting Headz: South Afrika's Sistaz in Hip Hop (2007): Explores South African hip hop culture through the stories of women in hip hop",
              'Skin (2008):  The story of Sandra Laing - a South African woman born to white parents who was classified as Coloured during the apartheid era',
              '50 Years! Of Love? (2008): The film showed at the 2008 Durban International Film Festival.',
              'Viva Riva! (2010): Crime thriller film written and directed by Djo Tunda',
              'Beauty (2011): South African film co-written and directed by Oliver Hermanus',
              'The Bang Bang Club (2011): Biographical drama film written and directed by Steven Silver and stars Ryan Phillippe as Greg Marinovic',
              'n Saak van Geloof (2011): Afrikaans-language drama film directed by Diony Kempen',
              'Dredd (2012): Science fiction action film directed by Pete Travis and written and produced by Alex Garland',
              'Otelo Burning (2012): Drama film directed and produced by Sara Blecher.',
              'Four Corners (2013): South African coming of age crime drama film about family lost and regained',
              'Khumba (2013): 3D computer-animated comedy film directed and produced by Anthony Silverston',
              'Leading Lady (2014): Comedy-drama film directed by Henk Pretorius & produced by Llewelynn Greeff',
              'Dis ek Anna (2015): Based on novels by Anchien Troskie (writing as Elbie Lotter)',
              'Hear Me Move (2015): The first South African Sbujwa dance',
              'Tell Me Sweet Something (2015): Romantic comedy film starring Nomzamo Mbatha',
              'Happiness is a Four-letter Word (2016): Based on the novel of the same name by Nozizwe Cynthia Jele the film tells the story of three friends trying to find their happiness',
              'Kalushi (2016): A story about Solomon Kalushi Mahlangu a nineteen-year-old hawker from the streets of Mamelodi',
              'Call Me Thief (2016): Crime film directed by Daryne Joshua.',
              'Vaya (2016): Drama film directed by Akin Omotoso & screened in the Contemporary World Cinema section at the 2016 Toronto',
              'Five Fingers (2017): Western thriller film directed by Michael Matthews',
              'High Fantasy (2017): Comedy film directed by Jenna Bass & screened in the Discovery section at the 2017 Toronto',
              "Keeping Up with the Kandasamys (2017): Indian comedy film: Jennifer and Shanti are neighbours who can't stand each other so the last thing they want is for their children to fall in love.",
              "Number 37 (2018): An injured young man confined to his apartment borrows his girlfriend's binoculars to spy on their neighbourhood and sees an opportunity to turn their lives around after witnessing a crime",
              'Kings of Mulberry Street (2019): Comedy-drama film revolving around the adventures of two young Indian boys & bullying local crime landlord',
              'Kandasamys: The Wedding (2019): Indian romantic comedy drama film about two meddling mothers who push their own demands and agendas for the big Wedding Day',
              'Buddha in Africa (2019): A Malawian orphan from a rural village growing up between the contrasting African culture and the strict discipline of the Confucian',
              "The Last Victims (2020): Political drama film following Dawid - a former member of South Africa's infamous C1 Counter Insurgency death squad",
              "District 9 (2009): A few aliens are forced to live in pathetic conditions on Earth but find support in a government agent who is responsible for their relocation",
              "3 Days to Go: A family together needs to survive for 3 days under one roof before they bury their father's ashes and part ways again",
              "Tsotsi (2005): The film tells the story of a young street thug who steals a car only to discover a baby in the back seat",
              "Invictus(2009): Biographical sports drama film based on the 2008 John Carlin book Playing the Enemy: Nelson Mandela and the Game That Made a Nation"]

    # define female director films
    directors = [
        'Booksmart(2019):  An unfiltered comedy about high school best friends and the bonds we create that lasts a lifetime, directed by Olivia Wilde',
        'Captain Marvel(2019): A 2019 American superhero film based on the Marvel Comics character Carol Danvers, directed by Anna Boden',
        'A Beautiful Day in the Neighborhood(2019): A timely story of kindness triumphing over cynicism, based on the true story of a real-life friendship , directed by Marielle Heller',
        'Blinded by the Light(2019): inspired by the life of journalist Sarfraz Manzoor and his love of the works of Bruce Springsteen, directed by Gurinder Chadha',
        'Hustlers(2019): follows a crew of savvy former strip club employees who band together to turn the tables on their Wall Street clients, directed by Lorene Scafaria',
        'Little Women(2019): Jo March reflects back and forth on her life, telling the beloved story of the March sisters, directed by Greta Gerwig',
        "Charlie's Angels(2019): new generation of Angels who are working for a private detective agency named the Townsend Agency, directed by Elizabeth Banks",
        'After Parkland(2019): an intimate chronicle of families as they navigate their way through the unthinkable, directed by Emily Taguchi',
        'Harriet(2019): Based on the thrilling and inspirational life of an iconic American freedom fighter Harriet Tubman a slave , directed by Kasi Lemmons',
        "Honey Boy(2019): based on Byron Bowers childhood and his relationship with his father, directed by Alma Har'el",
        'Family(2013): The film follows a Mafia family in the witness protection program who want to change their lives, directed by Laura Steinel',
        'Always Be My Maybe(2019): Reunited after 15 years, famous chef Sasha and hometown musician Marcus feel the old sparks of attraction, directed by Nahnatchka Khan',
        'Late Night(2019):  It stars Emma Thompson as a popular TV host who hires a new writer (Kaling) to keep from getting replaced, directed by Nisha Ganatra',
        'The Farewell(2019): A headstrong Chinese-American woman returns to China when her beloved grandmother is diagnosed with  cancer, directed by Lulu Wang',
        "A Dog's Journey(2019): The film is based on the 2012 novel of the same name by Cameron, directed by Gail Mancuso",
        'Breakthrough(2019): an account of true events written by Joyce Smith with Ginger Kolbaba, directed by Roxann Dawson',
        'Poms(2019): The film follows a group of women from a retirement community who decide to start a cheerleading squad, directed by Zara Hayes',
        'Nancy Drew & the Hidden Staircase(2019): Nancy accompanies her father on a trip to L.A, hoping to get clues to a murder mystery involving a movie star, directed by Katt Shea',
        'Otherhood(2019): A celebratory comedy about three mothers and their adult sons. The film explores the stage after motherhood, directed by Cindy Chupack',
        "Little Woods(2018): The plot for Little Woods is pretty simple, its about Ollie and her sister Deb and the struggles they're facing, directed by Nia DaCosta",
        'The Banana Splits Movie(2019): The Banana Splits is a fun-filled, cacophony of zany deaths and characters, directed by Danishka Esterhazy',
        'Hala(2019): A 17-year-old Pakistani American teenager struggles to balance desire with her cultural and religious obligations, directed by Minhal Baig',
        'Unicorn Store(2017): After failing out of art school and taking a humdrum office job, a whimsical painter gets a chance to fulfill her dream, directed by Brie Larson',
        "I'm Not Here(2017): a movie that follows the lead character Steve throughout three time periods of his life in a journey through alcoholism, directed by Michelle Schumacher",
        'Braid(2018): Two wanted women decide to rob their wealthy psychotic friend who lives in the fantasy world they created as kids, directed by Mitzi Peirone',
        'The Souvenir(2019): a beautiful portrayal of a friendship between two people from different generations, directed by  Joanna Hogg',
        'Tall Girl(2019): a heartfelt and hilarious coming-of-age story about finding the confidence to stop slouching and stand tall, directed by Nzingha Stewart',
        'Abominable(2019): The adventure is exciting without getting too harrowing and the characters are likeable enough, directed by Jill Culton',
        'The Kids are All Right(2010): 2 teenaged kids get the notion to seek out their father and introduce him to the family life that their mothers have built , directed by Lisa Cholodenko',
        'The Matrix(1999): a computer hacker learns from mysterious rebels about the nature of his reality/role in a war against the controllers of it, directed by Lana and Lilly Wachowski',
        'Boys Don’t Cry(1999): illustrates the violent intolerance and cruelty that humans can display towards others who appear different, directed by Kimberly Peirce',
        'Morvern Callar(2002): Out of the ordinary film about a somewhat whacked out young woman Morvern Callar, directed by Lynne Ramsay',
        'The Hitch-Hiker(1953): two fishing buddies who pick up a mysterious hitchhiker during a trip to Mexico, directed by Ida Lupino',
        'American Psycho(2000): Psycho follows the life of wealthy young investment banker Patrick Bateman, directed by Mary Harron',
        '35 Shots of Rum(2008): tells the story of a father-daughter relationship complicated by the arrival of an attractive young man, directed by Claire Denis',
        'The Beaches of Agnes(2008): an autobiographical essay where Varda revisits places from her past,reminisces about life, directed by Agnès Varda',
        'Somewhere(2010): The film follows Johnny Marco (played by Stephen Dorff), a newly famous actor, directed by Sofia Coppola',
        'The Silences of the Palace(1994): a film investigates issues of gender,class and sexuality in the Arab world through the lives of two generations of women, directed by Moufida Tlatli',
        'On Body and Soul(2017): The story revolves around a CFO of a slaughterhouse and the newly appointed meat quality inspector, directed by Ildikó Enyedi',
        'Whale Rider(2002): a film about the coming of age of a 12 year old New Zealand girl and her struggle for acceptance of her father, directed by Niki Caro']

    div_list = [
        'Parasite (2019: Greed and class discrimination threaten the newly formed symbiotic relationship between the wealthy Park family and the destitute Kim clan',
        'Hidden Figures (2016): The story of a team of female African-American mathematicians who served a vital role in NASA during the early years of the U.S. space program.',
        "Moana (2016): In Ancient Polynesia, when a terrible curse incurred by the Demigod Maui reaches an impetuous Chieftain's daughter's island, she answers the Ocean's call to seek out the Demigod to set things right.",
        'The Farewell (2019):  The film follows a Chinese-American family who, upon learning their grandmother has only a short while left to live, decide not to tell her and schedule a family gathering before she dies.',
        'Arrival (2016): When twelve mysterious spacecraft appear around the world, linguistics professor Louise Banks is tasked with interpreting the language of the apparent alien visitors.',
        'Moonlight (2016): A chronicle of the childhood, adolescence and burgeoning adulthood of a young, African-American, gay man growing up in a rough neighborhood of Miami.',
        'Silence (2016) : In the 17th century, two Portuguese Jesuit priests travel to Japan in an attempt to locate their mentor, who is rumored to have committed apostasy, and to propagate Catholicism.',
        'Zootopia (2016): In a city of anthropomorphic animals, a rookie bunny cop and a cynical con artist fox must work together to uncover a conspiracy.',
        'Bend it like Beckham (2002): A girl bends the rules, to reach her goal, in professional soccer.',
        "The Help (2011): An aspiring author during the civil rights movement of the 1960s decides to write a book detailing the African American maids' point of view on the white families for which they work, and the hardships they go through on a daily basis.",
        '12 Years a Slave (2013): In the antebellum United States, Solomon Northup, a free black man from upstate New York, is abducted and sold into slavery.',
        'Fences (2016): A working-class African-American father tries to raise his family in the 1950s, while coming to terms with the events of his life.',
        'Django Unchained (2012): With the help of a German bounty hunter, a freed slave sets out to rescue his wife from a brutal Mississippi plantation owner.',
        'Her (2013): A lonely writer develops an unlikely relationship with an operating system designed to meet his every need.',
        'Straight Outta Compton (2015): The group NWA emerges from the mean streets of Compton in Los Angeles, California, in the mid-1980s and revolutionizes Hip Hop culture with their music and tales about life in the hood.',
        'Dear White People (2014): The lives of four black students at an Ivy League college.',
        'The Blind Side (2009): The story of Michael Oher, a homeless and traumatized boy who became an All American football player and first round NFL draft pick with the help of a caring woman and her family.',
        'Bride and Predjudice (2004): Bollywood-style adaptation of the Jane Austen novel Pride and Prejudice',
        'Dallas Buyers Club (2013): In 1985 Dallas, electrician and hustler Ron Woodroof works around the system to help AIDS patients get the medication they need after he is diagnosed with the disease.',
        "Cracy Rich Asians (2018): Rachel, a professor, dates a man named Nick and looks forward to meeting his family. However, she is shaken up when she learns that Nick belongs to one of the richest families in the country",
        'Slumdog Millionaire (2008): A Mumbai teen reflects on his upbringing in the slums when he is accused of cheating on the Indian Version of "Who Wants to be a Millionaire?"',
        "Black Panther (2008): After his father's death, T'Challa returns home to Wakanda to inherit his throne. However, a powerful enemy related to his family threatens to attack his nation.",
        'Big Hero 6 (2014): The special bond that develops between plus-sized inflatable robot Baymax, and prodigy Hiro Hamada, who team up with a group of friends to form a band of high-tech heroes.',
        'District 9 (2009): An extraterrestrial race forced to live in slum-like conditions on Earth suddenly finds a kindred spirit in a government agent who is exposed to their biotechnology.',
        'American Gangster (2007): In 1970s America, a detective works to bring down the drug empire of Frank Lucas, a heroin kingpin from Manhattan, who is smuggling the drug into the country from the Far East.',
        'Half of a Yellow Sun (2013): Sisters Olanna and Kainene return home to 1960s Nigeria, where they soon diverge on different paths. As civil war breaks out, political events loom larger than their differences as they join the fight to establish an independent republic.',
        "Loving (2016): The story of Richard and Mildred Loving, a couple whose arrest for interracial marriage in 1960s Virginia began a legal battle that would end with the Supreme Court's historic 1967 decision.",
        'Milk (2008): Harvey Milk, an American activist, faces several difficulties while fighting for gay rights and becomes the first openly gay official to be elected to public office in California',
        "Dope (2015): Life changes for Malcolm, a geek who's surviving life in a tough neighborhood, after a chance invitation to an underground party leads him and his friends into a Los Angeles adventure.",
        "The Pursuit of Happyness (2006): A struggling salesman takes custody of his son as he's poised to begin a life-changing professional career.",
        "The King's Speech (2010): The story of King George VI of the United Kingdom of Great Britain and Northern Ireland, his impromptu ascension to the throne and the speech therapist who helped the unsure monarch become worthy of it.",
        'Life of Pi (2012): A young man who survives a disaster at sea is hurtled into an epic journey of adventure and discovery. While cast away, he forms an unexpected connection with another survivor: a fearsome Bengal tiger.',
        'The Princess and the Frog (2009): A waitress, desperate to fulfill her dreams as a restaurant owner, is set on a journey to turn a frog prince back into a human being, but she has to face the same problem after she kisses him.',
        '42: This movie is about Jackie Robinson and his journey to becoming a Brooklyn Dodger and his life during that time.',
        'Freedom Writers (2007): A young teacher inspires her class of at-risk students to learn tolerance, apply themselves, and pursue education beyond high school.',
        "Precious (2009): In New York City's Harlem circa 1987, an overweight, abused, illiterate teen who is pregnant with her second child is invited to enroll in an alternative school in hopes that her life can head in a new direction.",
        'Dreamgirls (2006): A trio of black female soul singers cross over to the pop charts',
        'Queen of Katwe (2016): A Ugandan girl sees her world rapidly change after being introduced to the game of chess.',
        "Selma (2014): A chronicle of Martin Luther King's campaign to secure equal voting rights via an epic march from Selma to Montgomery, Alabama in 1965.",
        "Get Out (2017): Chris, an African-American man, decides to visit his girlfriend's parents during a weekend getaway. Although they seem normal at first, he is not prepared to experience the horrors ahead.",
        "Fruitvale Station (2013): Based on the events leading to the death of Oscar Grant, a young man who was killed in 2009 by BART police officer Johannes Mehserle at the Fruitvale district station of the Bay Area Rapid Transit (BART) system in Oakland.",
        "Hotel Rwanda (2004): Paul Rusesabagina, a hotel manager, leads a happy life with his wife and children in Rwanda. He displays immense courage by saving the lives of many helpless refugees during a communal war.",
        "On the Basis of Sex (2018): Ruth Bader Ginsburg is a struggling attorney and new mother who faces adversity and numerous obstacles in her fight for equal rights."]

    q_list = [
        '"Find a truly original idea. It is the only way I will ever distinguish myself. It is the only way I will ever matter." - Beautiful Mind',
        '"Sometimes it is the people who no one imagines anything of who do the things that no one can imagine." - The Imitation Game',
        '"There should be no boundaries to human endeavor. We are all different. However bad life may seem, there is always something you can do, and succeed at. While there is life, there is hope." - The Theory of Everything',
        '"Most people live life on the path we set for them. Too afraid to explore any other. But once in a while people like you come along and knock down all the obstacles we put in your way. People who realize free will is a gift that you will never know how to use until you fight for it." - The Adjustment Bureau',
        """Most of life's burdens, with a little help, can become a gift" - Seventh Son""",
        '"I found it is the small everyday deeds of ordinary folk that keep the darkness at bay." - The Hobbit',
        '"I have to believe that when things are bad I can change them." - The Cinderella Man',
        """"Your dignity's inside you. Nobody can take something away from you you don't give them." - Glory Road""",
        'Oh yes, the past can hurt. But you can either run from it, or learn from it.  - – Rafiki, from The Lion King',
        '“Our lives are defined by opportunities, even the ones we miss.” - The Curious Case of Benjamin Button',
        '“To see the world, things dangerous to come to, to see behind walls, to draw closer, to find each other and to feel. That is the purpose of life.” - TheSecret Life of Walter Mitty',
        '"Sometimes the right path is not the easiest one." - Pocahontas',
        '"If you focus on what you left behind, you will never be able to see what lies ahead." - Ratatouille',
        '"It is not our abilities that show what we truly are… it is our choices." - Harry Potter and the Chamber of Secrets',
        'Carpe diem. Seize the day, boys. Make your lives extraordinary. - Dead Poets Society',
        'How many times do I have to teach you: just because something works doesn’t mean it can’t be improved. - Black Panther',
        '"The flower that blooms in adversity is the most rare and beautiful of all” - Mulan',
        '"Happiness can be found even in the darkest of times, if one only remembers to turn on the light.” - Harry Potter and the Prisoner of Azkaban',
        '"It’s only a passing thing, this shadow. Even darkness must pass. A new day will come. And when the sun shines it will shine out the clearer.: - The Lord of the Rings: The Two Towers',
        '"A laugh can be a very powerful thing. Why, sometimes in life, it’s the only weapon we have." - Who Framed Roger Rabbit?',
        '"Hope is a good thing, maybe the best of things, and no good thing ever dies." - The Shawshank Redemption',
        "Doubt is useful, it keeps faith a living thing. After all, you cannot know the strength of your faith until it is tested.' - Life of Pi",
        '“No matter what anybody tells you, words and ideas can change the world.” - Dead Poets Society',
        '“Why do we fall sir? So that we can learn to pick ourselves up.” - Batman Begins',
        'You mustn’t be afraid to dream a little bigger, darling.” - Inception',
        '"All we have to decide is what to do with the time that is given to us." - The Lord of the Rings',
        'Going in one more round when you don’t think you can – that’s what makes all the difference in your life. - Rocky IV',
        '“It’s only after we’ve lost everything that we’re free to do anything.” - Fight Club',
        '“At some point you’ve got to decide for yourself who you gonna be. Can’t let nobody make that decision for you.” - Moonlight',
        '“The greatest thing you’ll ever learn is just to love and be loved in return." - Moulin Rouge',
        """“Life moves pretty fast. If you don’t stop and look around once in a while, you could miss it" - Ferris Bueller's Day Off""",
        '“Every man dies, not every man really lives.” - nan',
        '"Do, or do not. There is no “try”." - Star Wars',
        '“When you get a different vantage point it changes your perspective… It allows you to see things you should have seen a long time ago." - First Man',
        '“It’s not who I am underneath but what I do that defines me.” - Batman Begins',
        '“To infinity and beyond!” - Toy Story',
        '“A wise man can learn more from his enemies than a fool from his friends.” - Rush',
        "“From where I stand, the sun is shining all over the place.” - Singin' in the Rain",
        '“After all, tomorrow is another day.” - Gone with the Wind',
        '“With great power comes great responsibility.” - Spider-Man',
        '“It takes a great deal of bravery to stand up to your enemies, but a great deal more to stand up to your friends.” - Harry Potter and the Chamber of Secrets',
        '“Why are you trying so hard to fit in when you were born to stand out?” - What a Girl wants',
        '"You know what kind of plan never fails? No plan. No plan at all. You know why? Because life cannot be planned" - Parasite',
        "“My mama always said life was like a box of chocolates. You never know what you're gonna get.” - Forrest Gump",
        '"Not all who wander are aimless, especially those who seek truth beyond tradition, beyond definition, beyond the image." - Mona Lisa Smile',
        '"Watch your thoughts, for they become words. Watch your words, for they become actions. Watch your actions, for they become habits. Watch your habits, for they become your character. And watch your character, for it becomes your destiny." - The Iron Lady',
        'Life’s a little bit messy. We all make mistakes. No matter what type of animal you are, change starts with you. - Zootopia',
        '"Oh No! These Facts And Opinions Look So Similar!" - Inside Out',
        '"Manners. Maketh. Man" - Kingsman: The Secret Service']

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)

    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('First Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Solution Overview":
        st.write("# Solution Overview")
        st.write("Collaborative filtering uses the ratings of users with similar taste to make suggestions of future content.")
        st.write("""Matrix Factorisation is a class of Collaborative filtering algorithm that decomposes the user-item ratings matrix into a product of two lower
        dimensionality matrices that each represent users and items in latent space. Matrix R (m x n) is a sparse matrix of ratings where m = the
        number of users, and n = the number of items (movies). Matrix R can be factorised into two matrices, P (m x k) and Q (k x n) where k
        represents k unknown 'latent factors’.""")
        st.write("""These latent factors are hidden or underlying features in the data that account for the user's logic or decision making process in weighting
        factors that contribute to the rating of the item. This could be a genre they like, an actor they don't like, the movie being too long, amazing
        CGI, or bad sound mixing and so on.""")
        st.write("""All these latent features are taken into account when a user rates a movie. By using the known, true user ratings, Stochastic Gradient
        descent is used to find the optimum weightings of the latent features that will most closely approximate the actual rating. The predicted
        rating is equal to the dot product of the user vector and the item vector""")
	st.write("""A common issue with Collaborative filtering is Cold-start, that is, no ratings for any one of the three movie titles input by the user. In this instance,
	we provide recommendations based on the top 100 most rated films in the MovieLense Data, however, other methods of handling cold start would include deep learning,
	or implementation of a hybrid approach that uses content-based filtering as well.""")
        st.image("https://github.com/Pilasande/unsupervised-predict-streamlit-template/blob/master/resources/imgs/sol_overview.png?raw=true", use_column_width=True)

    if page_selection == "Data & Insights":
        st.write("# Data & Insights")
        st.write("""The Spotlight Movie Recommender System uses the
        MovieLens dataset, maintained by the GroupLens research
        group in the Department of Computer Science and
        Engineering at the University of Minnesota. Additional
        movie content data is sourced from IMDB. Click through to
        view insights""")
        graphs = ["Ratings Distribution", "Top 10 Most Rated Movies", "Top 10 Movies: 5.0 Rating",
                  "Top 10 Movies: 0.5 Rating",
                  "Exploring Genres", "Exploring Title Casts", "Most Rated Directors", "Film Production by Country",
                  "Ratings by Release Year"]

        choice = st.selectbox("Choose graph",graphs)
        if choice == "Ratings Distribution":
            st.write("""The average movie rating is 3.55 with a standard deviation of 1.05.
            15% of ratings are rated as 5.00 & 17% of the ratings are below 2.50.
            The rating score with the highest percentage of observations is 4.0.""")
            st.image("https://github.com/Pilasande/unsupervised-predict-streamlit-template/blob/master/resources/imgs/ratingdist.png?raw=true",use_column_width=True)

        if choice == "Top 10 Most Rated Movies":
            st.write("• The most rated movie is the Shawshank Redemption,")
            st.write("""• The visualisation is not indicative of the quality, critical
            acclaim or public reception of the movie, but rather the next
            best approximation of the most popular or most watched
            movies.""")
            st.image("https://github.com/Pilasande/unsupervised-predict-streamlit-template/blob/master/resources/imgs/most_rated.png?raw=true",use_column_width=True)

        if choice == "Top 10 Movies: 5.0 Rating":
            st.write("• The most rated movie is the Shawshank Redemption,")
            st.write("""• The top ten movies with the highest number of 5.0 ratings
            contain most of the movies that have the most ratings
            overall.""")
            st.write("• Most of these movies are from 90's")
            st.image("https://github.com/Pilasande/unsupervised-predict-streamlit-template/blob/master/resources/imgs/high_rated.png?raw=true",use_column_width=True)

        if choice == "Top 10 Movies: 0.5 Rating":
            st.write("""• Three comedy movies starring Jim Carrey ('Dumb & Dumber', 'Ace
            Ventura: When Nature Calls' and 'Ace Venture: Pet Detective') make an
            appearance in the top ten.""")
            st.write("""• 50% of the top ten comprise popular movie franchises: 'Twilight', 'Star
            Wars' and 'The Lord of the Rings'. This indicates that although these
            films are popular with their respective fandoms, lots of people do not
            enjoy them.""")
            st.write("""• Star Wars: A New Hope (1977) appears in the top ten for both Most 5.0
            ratings and and Most 0.5 ratings alluding to the fact that it is one of the
            most watched (rated) movies.""")
            st.image("https://github.com/Pilasande/unsupervised-predict-streamlit-template/blob/master/resources/imgs/low_rated.png?raw=true",use_column_width=True)

        if choice == "Exploring Genres":
            st.write("""• As the various films can fall into multiple genres, a
            wordcloud is an appropriate method of visualising the
            most common genres""")
            st.write("""• The most common genres in the data set include
            Drama, Comedy and Action.""")
            st.image("https://github.com/Pilasande/unsupervised-predict-streamlit-template/blob/master/resources/imgs/genres.png?raw=true",use_column_width=True)

        if choice == "Exploring Title Casts":
            st.write("""Tom Hanks, Samuel L Jackson, Morgan Freeman and Brad Pitt
            appear frequently overall. A repeating trend is the lack of female
            actresses that appear overall which highlights the gender
            disparity in casting and leading film roles for women in the
            industry.""")
            st.image("https://github.com/Pilasande/unsupervised-predict-streamlit-template/blob/master/resources/imgs/cast.png?raw=true",use_column_width=True)

        if choice == "Most Rated Directors":
            st.write("• Quentin Tarantino is the Director with the most film ratings.")
            st.write("""• Unusually, several book authors appear in this visualisation: Michael Chrichton (Jurrassic Park Series), J.R.R.Tolkien
            (The Lord of the Rings Trilogy), Stephen King (The Shining & other books) and Thomas Harris (Hannibal Series. When
            researched, all of these films have directors that differ from the authors of the books they were based on.""")
            st.write("""• The DGA (Director's Guild of America) states that films can only have one credited director, unless directed by an
            established duo (such as the Coen brothers) 6. Even if the authors were bestowed director credits, they would have
            been given assistant director credits.""")
            st.write("""• This points to inconsistencies in the database, as the authors should be replaced with the actual directors of the
            movies.""")
            st.write("""• Ethan Coen and Lily Wachowski are listed as sole directors whilst in reality they work in established 'duo' directorships
            with their siblings and should be listed as 'established duos'.""")
            st.write("""• There is only one female director (Lily Wachowski, co-director of The Matrix) in the top 10. This reflects the current
            lack of gender diversity in the film industry.""")
            st.image("https://github.com/Pilasande/unsupervised-predict-streamlit-template/blob/master/resources/imgs/directors.png?raw=true",use_column_width=True)

        if choice == "Film Production by Country":
            st.write("• The majority of films for which a film budget is listed are either produced/filmed or funded in the United States.")
            st.write("""• Films made in China (CNY, Chinese Yuan) and India (INR, Indian Rupee) seem under represented in the data
            (No of films). Both the Chinese and Indian (Bollywood) film industry churn out a sizeable number of movies every
            year (772 & 1986 films in 2016 respectively in comparison to Hollywood's 646 5).""")
            st.write("""• This could be attributed to the Hollywood film industry being much older and therefore having more films, but if
            Bollywood and Chinese films had the same level of inclusivity for just 2016 alone, the no of films for INR and CYN
            would at least hit 2758 collectively.""")
            st.write("""• This speaks to the lack of diversity in films featured in the database. Although these films are in foreign
            languages, they do have subtitles and can gain more exposure if featured in the database and ergo the resultant
            recommender system. It would also attract a more diverse audience and improve user experience for users that
            are interested in foreign films to whatever platform the recommender system is being built for""")
            st.image("https://github.com/Pilasande/unsupervised-predict-streamlit-template/blob/master/resources/imgs/film_curr.png?raw=true", use_column_width=True)

        if choice == "Ratings by Release Year":
            st.write("• The release year of movies in the database ranges from 1888 to 2019.")
            st.write("• Movie ratings range from 0 to a just over 1000 from the year 1888 to 1949.")
            st.write("• An upward trend is noted beyond 1949. This could be due to the wider use of colour negative film in the 1950s.")
            st.write("""• The number of ratings peak at 59600 in the year 1995. Movies produced in the 90's seem to have the most
            ratings. This could attributed to a number of factors:""")
            st.write("• They were released 20-30 years ago and have had more time for people to watch and rate them.")
            st.write("• The movies made in this era are simply, good movies with high 'rewatchability'.")
            st.write("• Popular movies and cult classics from the era are being discovered by younger generations.")
            st.write("""• A downward trend is noted from 1995 onward. This could either be because the data set is incomplete, i.e
            missing movies or ratings for this period, or perhaps less users are rating movies via the MovieLens platform in
            recent years. MovieLens is a web-based recommender system platform that recommends movies for its users to
            watch using collaborative filtering of users' movie ratings and reviews""")
            st.image("https://github.com/Pilasande/unsupervised-predict-streamlit-template/blob/master/resources/imgs/years.png?raw=true", use_column_width=True)

    if page_selection == "Diversity Statistics":
        st.write("# Diversity Statistics")
        st.write("Facts and statistics about diversity in Film")
        st.write("""Click through to explore findings from the Hollywood Diversity Report
            (2019) & USC Annenberg Inclusion Initiative (2018)""")
        stats = ["Gender Diversity","Minority Groups"]
        sel = st.selectbox("Select Statistics",stats)
        if sel == "Gender Diversity":
            st.write("""Metacritic scores show just a slight difference between male directors
            (median 54: average 54.2) and female directors (median 55, average
            55.8).""")
            st.write("""Only 5.1% of Best Director award nominees across the Golden Globes,
            Academy Awards, DGA Awards, and Critics’ Choice Awards were
            women.""")
            st.write("""95.1% of top grossing film directors have been male since 2007.
            Women make up 4.9% with women of colour accounting for <1 %.""")
            st.image("https://github.com/Pilasande/unsupervised-predict-streamlit-template/blob/master/resources/imgs/gender.png?raw=true",use_column_width=True)

        if sel == "Minority Groups":
            st.write("""Metacritic scores of directors in 2019 by race are (median 54, average
            54.9) for directors of colour and (median 54, average 54.2) for white
            directors.""")
            st.write("86.4 % of top grossing film directors have been male since 2007.")
            st.write("Directors of colour account for 13.6 %.")
            st.write("""Source: Hollywood Diversity Report (2019) & USC Annenberg Inclusion
            Initiative (2018) )""")
            st.image("https://github.com/Pilasande/unsupervised-predict-streamlit-template/blob/master/resources/imgs/minorities.png?raw=true",use_column_width=True)
    if page_selection == "Mzansi Movie Magic":
        st.write("# Mzansi Movie Magic")
        st.write("""Celebrate modern South African Film. Click to generate a proudly South African Film to check out!""")
        if st.button('Find an SA film'):
            mz_movie = random.choice(mzansi)
            st.write(str(mz_movie))
        st.image("https://github.com/Pilasande/unsupervised-predict-streamlit-template/blob/master/resources/imgs/mazansi.png?raw=true",use_column_width=True)

    if page_selection == "Female Directed Films":
        st.write("# Female Directed Films")
        st.write("""Of the top 100 grossing films of 2019, women represented
                only 12% of directors (Center for the Study of Women in
                Television and Film). Only five female director’s have been
                nominated for the Academy Award for Best Director, with
                only one winner. Click below discover a female director with
                a story to tell.""")
        if st.button('Find a film'):
            fem_dir = random.choice(directors)
            st.write(str(fem_dir))
        st.image("https://github.com/Pilasande/unsupervised-predict-streamlit-template/blob/master/resources/imgs/wom_film.png?raw=true",use_column_width=True)

    if page_selection == "Diversity in Films":
        st.write("# Diversity in Films")
        st.write("""Click below discover a film celebrating the diversity of people!""")
        if st.button('Find a Film'):
            div_movie = random.choice(div_list)
            st.write(str(div_movie))
        st.image("https://github.com/Pilasande/unsupervised-predict-streamlit-template/blob/master/resources/imgs/diversity.png?raw=true",use_column_width=True)

    if page_selection == "Quote of the Day":
        st.write("""# Quote of the Day""")
        st.write("""Click below for a quote to inspire you in the fight to be seen and feel represented""")
        if st.button('Quote Me!'):
            quote_movie = random.choice(q_list)
            st.write(str(quote_movie))
        st.image("https://github.com/Pilasande/unsupervised-predict-streamlit-template/blob/master/resources/imgs/inspo.png?raw=true",use_column_width=True)






    if page_selection == "Our Team":
        team="""

	<div style="background: #f1f2f6;text-align: center;">
		<div style="max-width: 1500px;margin: auto;padding: 40px;color: #333;overflow: hidden;">
      <h2><b>Meet our Team</b></h2>
      <!---Team members---->
				<div style="float: left;width: calc(100% / 3);overflow: hidden;padding: 40px 0;transition: 0.4s;">
					<img style="width: 150px;height: 150px;border-radius: 50%;" src="https://github.com/Tumisang-hub/Unsupervised-Sprint/blob/master/RNT03793-2%20(2).JPG?raw=true" alt="rafeh">
					<div style="margin: 5px;text-transform: uppercase;">Rohini Jagath</div>
					<div style="font-style: italic;color: #3498db;">Data Scientist</div>
					<div style=";color: #f63366;"><p>Passionate about all things data... but she won't share popcorn at the movies.</p></div>
					<div style="margin-top: 6px;">
						<a href="https://www.linkedin.com/in/rohini-jagath-2492a156" style="margin: 0 4px;display: inline-block;width: 30px;height: 30px;transition: 0.4s;"><img border="0" alt="Linkein" src="https://image.flaticon.com/icons/svg/1384/1384014.svg" width="25" height="25"></a>
					</div>
				</div>
<!-------------------->
<!---Team members---->
				<div style="float: left;width: calc(100% / 3);overflow: hidden;padding: 40px 0;transition: 0.4s;">
					<img style="width: 150px;height: 150px;border-radius: 50%;" src="https://github.com/Tumisang-hub/Unsupervised-Sprint/blob/master/pila.jpg?raw=true">
					<div style="margin: 5px;text-transform: uppercase;">Pilasande Pakkies</div>
					<div style="font-style: italic;color: #3498db;">Data Scientist</div>
					<div style=";color: #f63366;"><p>An enthusiast who loves volleyball more than any sport. A pizza lover.</p></div>
					<div style="margin-top: 6px;">
						<a href="http://www.linkedin.com/in/Pilasande-Pakkies" style="margin: 0 4px;display: inline-block;width: 30px;height: 30px;transition: 0.4s;"><img border="0" alt="Linkein" src="https://image.flaticon.com/icons/svg/1384/1384014.svg" width="25" height="25"></a>
					</div>
				</div>
<!-------------------->
<!---Team members---->
				<div style="float: left;width: calc(100% / 3);overflow: hidden;padding: 40px 0;transition: 0.4s;">
					<img style="width: 150px;height: 150px;border-radius: 50%;" src="https://github.com/Tumisang-hub/Unsupervised-Sprint/blob/master/20191130_203409.jpg?raw=true" alt="rafeh">
					<div style="margin: 5px;text-transform: uppercase;">Tumisang Sentle</div>
					<div style="font-style: italic;color: #3498db;">Web Developer</div>
					<div style=";color: #f63366;"><p>A math addict. He loves listening to debates but he can't debate.</p></div>
					<div style="margin-top: 6px;">
						<a href="https://www.linkedin.com/in/tumisang-sentle-53100a1a5/" style="margin: 0 4px;display: inline-block;width: 30px;height: 30px;transition: 0.4s;"><img border="0" alt="Linkein" src="https://image.flaticon.com/icons/svg/1384/1384014.svg" width="25" height="25"></a>
					</div>
				</div>
<!-------------------->
<!---Team members---->
				<div style="float: left;width: calc(100% / 3);overflow: hidden;padding: 40px 0;transition: 0.4s;">
					<img style="width: 150px;height: 150px;border-radius: 50%;" src="https://github.com/Tumisang-hub/Unsupervised-Sprint/blob/master/60532fb212cb493f8fc0c629ef61aa1b.jpg?raw=true" alt="rafeh">
					<div style="margin: 5px;text-transform: uppercase;">Refentse Motlogelwa</div>
					<div style="font-style: italic;color: #3498db;">Data Engineer</div>
					<div style=";color: #f63366;"><p>A lover of life with good statistics background. He is also a great DJ.</p></div>
					<div style="margin-top: 6px;">
						<a href="https://www.linkedin.com/in/ramotse-motlogelwa-8a09358b" style="margin: 0 4px;display: inline-block;width: 30px;height: 30px;transition: 0.4s;"><img border="0" alt="Linkein" src="https://image.flaticon.com/icons/svg/1384/1384014.svg" width="25" height="25"></a>
					</div>
				</div>
<!-------------------->
<!---Team members---->
				<div style="float: left;width: calc(100% / 3);overflow: hidden;padding: 40px 0;transition: 0.4s;">
					<img style="width: 150px;height: 150px;border-radius: 50%;" src="https://media-exp1.licdn.com/dms/image/C5603AQEtkA_hyaeciA/profile-displayphoto-shrink_800_800/0?e=1600300800&v=beta&t=i2wG9MJ8LyVMEYkssSfzhKKIoCCmruWTIlt92QEFT9U">
					<div style="margin: 5px;text-transform: uppercase;">Philani Mkhize</div>
					<div style="font-style: italic;color: #3498db;">Data Analyst</div>
					<div style=";color: #f63366;"><p>The world is one big data problem inspired by Andrew McAfee.</p></div>
					<div style="margin-top: 6px;">
						<a href="https://www.linkedin.com/in/philani-mkhize-519995149/" style="margin: 0 4px;display: inline-block;width: 30px;height: 30px;transition: 0.4s;"><img border="0" alt="Linkein" src="https://image.flaticon.com/icons/svg/1384/1384014.svg" width="25" height="25"></a>
					</div>
				</div>
<!-------------------->
<!---Team members---->
				<div style="float: left;width: calc(100% / 3);overflow: hidden;padding: 40px 0;transition: 0.4s;">
					<img style="width: 150px;height: 150px;border-radius: 50%;" src="https://github.com/Tumisang-hub/Unsupervised-Sprint/blob/master/IMG-2211.jpg?raw=true" alt="rafeh">
					<div style="margin: 5px;text-transform: uppercase;">Sandile Mkize</div>
					<div style="font-style: italic;color: #3498db;">Data Analyst</div>
					<div style=";color: #f63366;"><p>A former side stepper from the rugby field who turned into a data scientist.</p></div>
					<div style="margin-top: 6px;">
						<a href="https://www.linkedin.com/in/sandile-mkize-2395b4161/" style="margin: 0 4px;display: inline-block;width: 30px;height: 30px;transition: 0.4s;"><img border="0" alt="Linkein" src="https://image.flaticon.com/icons/svg/1384/1384014.svg" width="25" height="25"></a>
					</div>
				</div>
<!-------------------->

                """
        st.markdown(team, unsafe_allow_html=True)
    if page_selection == "Homepage":
        st.write("# Spotlight Movie Recommender")
        st.write("""What are you in the mood for? Fast paced Action, a magical trip into a faraway fantasy land or
                feeling the thrill of the chase as you solve a mystery or save the world with our heroes &
                heroines? Whatever it may be, we have movie recommendations at your fingertips""")
        st.write("""Spotlight is a movie recommender app with a difference. Besides recommending movies based
                on your individual taste and preferences, we aim to direct the ‘spotlight’ on diversity in film. Use
                the Navigation bar on the left to explore movie recommendations, statistics and visualizations
                and discover something new!""")
        st.image("https://github.com/Pilasande/unsupervised-predict-streamlit-template/blob/master/resources/imgs/homepage.png?raw=true", use_column_width=True)




if __name__ == '__main__':
    main()
