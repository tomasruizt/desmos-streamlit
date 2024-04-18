from datetime import date
import time

import pandas as pd
import numpy as np

import streamlit as st

@st.cache_data(show_spinner=False)
def beefy_algorithm(date: date) -> pd.DataFrame:
    time.sleep(5)
    dates = pd.date_range(date, periods=10)
    values = np.arange(10)
    return pd.DataFrame({"date": dates, "value": values})