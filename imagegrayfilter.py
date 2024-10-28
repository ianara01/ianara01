# 사용자가 업로드한 이미지에 대해 흑백 필터를 적용하는 옵션을 제공

import streamlit as st
from PIL import Image
import numpy as np

# 앱 제목
st.title("이미지 필터 애플리케이션")

# 이미지 업로드
uploaded_file = st.file_uploader("이미지를 업로드하세요", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # 이미지 열기
    image = Image.open(uploaded_file)
    
    # 원본 이미지 표시
    st.image(image, caption="업로드한 이미지", use_column_width=True)

    # 흑백 필터 적용
    if st.button("흑백 필터 적용"):
        # 이미지를 흑백으로 변환
        gray_image = image.convert("L")
        
        # 흑백 이미지 표시
        st.image(gray_image, caption="흑백 이미지", use_column_width=True)

        # 다운로드 버튼
        gray_image.save("gray_image.png")
        with open("gray_image.png", "rb") as file:
            btn = st.download_button(
                label="흑백 이미지 다운로드",
                data=file,
                file_name="gray_image.png",
                mime="image/png"
            )

# 앱 실행
if __name__ == "__main__":
    st.write("이미지를 업로드하고 필터를 적용해 보세요!")