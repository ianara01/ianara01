# ml은 colab

import streamlit as st
import numpy as np
import pickle
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


st.title("Machine Learning")
st.header("캘리포니아 집값 예측 프로그램")

cols = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Lattitude', 'Longitude']
data = [0] * 8
for idx, col in enumerate(cols):
    data[idx] = st.number_input(f"{col}:", value=0.0)
x= np.array(data).reshape(1, -1)

# x.shape

with open("rf_house.pickle", 'rb') as f:
    rf_model = pickle.load(f)

y = rf_model.predict(x)

st.header("예측되는 집값: {} 입니다. ")