import streamlit as st

class Calculator:
    @staticmethod
    def sum(x, y):
        return x + y

    @staticmethod
    def sub(x, y):
        return x - y

    @staticmethod
    def mul(x, y):
        return x * y

    @staticmethod
    def div(x, y):
        if y == 0:
            return "0으로 나눌 수 없습니다."
        return x / y

# Streamlit 앱 설정
st.title("간단한 계산기")

# 사용자 입력
num1 = st.number_input("첫 번째 숫자를 입력하세요:", format="%.2f")
num2 = st.number_input("두 번째 숫자를 입력하세요:", format="%.2f")

operation = st.selectbox("연산을 선택하세요:", ["덧셈", "뺄셈", "곱셈", "나눗셈"])

# 결과 계산
if st.button("계산"):
    if operation == "덧셈":
        result = Calculator.sum(num1, num2)
    elif operation == "뺄셈":
        result = Calculator.sub(num1, num2)
    elif operation == "곱셈":
        result = Calculator.mul(num1, num2)
    elif operation == "나눗셈":
        result = Calculator.div(num1, num2)

    st.write(f"결과: {result}")

# 앱 실행
if __name__ == "__main__":
    st.write("계산기를 사용하세요!")
