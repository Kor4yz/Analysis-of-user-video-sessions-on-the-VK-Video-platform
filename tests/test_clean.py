import pandas as pd
from src.clean import clean_df

def test_clean_filters_nonpositive_and_winsor():
    df = pd.DataFrame({"total_view_time":[0,-1,1,2,100000], "user_id":[1,1,1,1,1]})
    out = clean_df(df, perc=0.8)  
    assert (out["total_view_time"] > 0).all()
    assert out["total_view_time"].max() <= 2
