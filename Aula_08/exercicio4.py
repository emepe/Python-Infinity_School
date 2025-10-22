import pandas as pd  # type: ignore
import streamlit as st  # type: ignore

df = pd.read_csv("padoca.csv")

print(df.head())