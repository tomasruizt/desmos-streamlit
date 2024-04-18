from datetime import date
import time

import pandas as pd
import numpy as np

import streamlit as st

def beefy_algorithm(date: date) -> pd.DataFrame:
    time.sleep(5)
    dates = pd.date_range(date, periods=3)
    values = np.arange(3)
    return pd.DataFrame({"date": dates, "value": values})