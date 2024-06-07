import streamlit as st  # streamlit 라이브러리 임포트
import pandas as pd  # pandas 라이브러리 임포트
import numpy as np   # numpy 라이브러리 임포트
from PIL import Image     # 이미지 처리를 위한 PIL 라이브러리 임포트
import os  # 파일 경로 확인을 위한 os 라이브러리 임포트

# 타이틀 텍스트 출력
st.title('첫번째 웹 어플 만들기👋')

# 텍스트 출력
st.write('# 1. Markdown 텍스트 작성하기')

# Markdown 문법으로 작성된 문장 출력
st.markdown(
    '''
    # 마크다운 헤더1
    - 마크다운 목록1. **굵게** 표시
    - 마크다운 목록2. *기울임* 표시
        - 마크다운 목록2-1
        - 마크다운 목록2-2

    ## 마크다운 헤더2
    - [네이버](https://naver.com)
    - [구글](https://google.com)

    ### 마크다운 헤더3
    일반 텍스트
    '''
)

# DataFrame 출력
st.write('# 2. DataFrame 표시하기')  # 텍스트 출력
df = pd.DataFrame({  # DataFrame 생성
    '이름': ['홍길동', '이순신', '강감찬'],
    '나이': [20, 45, 35]
})

st.dataframe(df)  # DataFrame 출력

# 그래프 출력
st.write('# 3. 그래프 표시하기')  # 텍스트 출력
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"]) # DataFrame 생성

st.bar_chart(chart_data)  # 바 차트 출력

# # 이미지 출력
# st.write('# 4. 이미지 표시하기')   # 텍스트 출력

# # 이미지 파일 경로
# image_path = 'C:/StreamlitImages/chi.png'

# # 파일 존재 여부 확인
# if os.path.exists(image_path):
#     st.write(f"이미지 파일 경로: {image_path}")
#     img = Image.open(image_path)     # 이미지 파일 열기
#     st.image(img, width=300)         # 이미지 출력
# else:
#     st.write(f"이미지 파일을 찾을 수 없습니다. 경로를 확인해주세요: {image_path}")


# 사이드바
st.header('🤖 사이드바')
st.sidebar.write('## 사이드바 텍스트')
st.sidebar.checkbox('체크박스 1')
st.sidebar.checkbox('체크박스 2')
st.sidebar.radio('라디오 버튼', ['radio 1', 'radio 2', 'radio 3'])
st.sidebar.selectbox('셀렉트박스', ['select 1', 'select 2', 'select 3'])
