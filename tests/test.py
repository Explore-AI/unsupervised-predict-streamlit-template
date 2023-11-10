from eda import eda_functions as eda
from eda import model_functions as model
import pandas as pd

def test_eda_functions():
    """
    make sure eda functions work properly
    """
    # test user_ratings_count
    assert type(eda.user_ratings_count(df = pd.DataFrame({'userId':[1,2,3,1,2,4,5,4]}), n=3)) == 'NoneType', 'incorrect'
    # test ratings_distplot
    assert type(eda.ratings_distplot(df = pd.DataFrame({
        'userId':[1,1,1,2,2,2,3,3,3],
        'movieId':['a','b','c','a','b','c','a','b','c'],
        'rating':[4,3,3.5,3,3,4,3.5,4,2]}),)) == 'NoneType', 'incorrect'