# 사용자가 선택한 주식의 코드에 대해 최근 90일의 가격 변화를 선 그래프로 보여주는 앱

import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Streamlit 앱 제목
st.title("주식 가격 변화 보기")

# 사용자가 선택할 수 있는 주식 리스트
stocks = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']
selected_stock = st.selectbox("주식을 선택하세요:", stocks)

# 최근 30일의 주식 데이터 가져오기
if selected_stock:
    stock_data = yf.download(selected_stock, period='90d', interval='1d')
    
    # 주식 데이터 확인
    if not stock_data.empty:
        # 데이터 프레임을 사용하여 날짜를 인덱스로 설정
        stock_data.reset_index(inplace=True)

        # 그래프 그리기
        plt.figure(figsize=(10, 5))
        plt.plot(stock_data['Date'], stock_data['Close'], marker='o')
        plt.title(f"{selected_stock}의 최근 30일 가격 변화")
        plt.xlabel("날짜")
        plt.ylabel("종가")
        plt.xticks(rotation=45)
        plt.grid()
        
        # Streamlit에 그래프 표시
        st.pyplot(plt)
    else:
        st.error("주식 데이터를 가져오는 데 실패했습니다.")
