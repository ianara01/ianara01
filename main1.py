# streamlit에 쓸 파일
# ml은 colab

import streamlit as st

st.title("Machine Learning")
st.header("주식 예측 프로그램")


option = st.selectbox(
    "기업 선택",
    ("SKhynix", "Hyndai", "Samsung")
)

st.write("선택한 기업: ", option)
america_option = st.selectbox(
    "관심 기업은? ",
    ("Tesla", "NASA", "Meta")
)

st.write("관심 기업: ", america_option)