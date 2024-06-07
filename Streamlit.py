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

# 레이아웃: 컬럼
st.header('🤖 컬럼 레이아웃')
col_1, col_2, col_3 = st.columns([1,2,1]) # 컬럼 인스턴스 생성. 1:2:1 비율로 컬럼을 나눔

with col_1:
    st.write('## 1번 컬럼')
    st.checkbox('이것은 1번 컬럼에 속한 체크박스 1')
    st.checkbox('이것은 1번 컬럼에 속한 체크박스 2')

with col_2:
    st.write('## 2번 컬럼')
    st.radio('2번 컬럼의 라디오 버튼', ['radio 1', 'radio 2', 'radio 3'])  # 동일한 라디오 버튼을 생성할 수 없음
    # 사이드바에 이미 라디오 버튼이 생성되어 있기 때문에, 여기서는 라디오 버튼의 내용을 변경해야 오류가 발생하지 않음

col_3.write('## 3번 컬럼')
col_3.selectbox('3번 컬럼의 셀렉트박스', ['select 1', 'select 2', 'select 3'])
# 사이드바에 이미 셀렉트박스가 생성되어 있기 때문에, 여기서는 셀렉트박스의 내용을 변경해야 오류가 발생하지 않음

# 레이아웃: 탭
st.header('🤖 탭 레이아웃')
tab_1, tab_2, tab_3 = st.tabs(['탭A', '탭B', '탭C'])  # 탭 인스턴스 생성. 3개의 탭을 생성

with tab_1:
    st.write('## 탭A')
    st.write('이것은 탭A의 내용입니다.')

with tab_2:
    st.write('## 탭B')
    st.write('이것은 탭B의 내용입니다.')

tab_3.write('## 탭C')
tab_3.write('이것은 탭C의 내용입니다.')

# 사용자 입력
st.header('🤖 사용자 입력')

text = st.text_input('여기에 텍스트를 입력하세요') # 텍스트 입력은 입력된 값을 반환
st.write(f'입력된 텍스트: {text}')

number = st.number_input('여기에 숫자를 입력하세요') # 숫자 입력은 입력된 값을 반환
st.write(f'입력된 숫자: {number}')

check = st.checkbox('여기를 체크하세요') # 체크박스는 True/False 값을 반환
if check:
    st.write('체크되었습니다.')

radio = st.radio('여기에서 선택하세요', ['선택 1', '선택 2', '선택 3']) # 라디오 버튼은 선택된 값을 반환
st.write(radio+'가 선택되었습니다.')

select = st.selectbox('여기에서 선택하세요', ['선택 1', '선택 2', '선택 3']) # 셀렉트박스는 선택된 값을 반환
st.write(select+'가 선택되었습니다.')

slider = st.slider('여기에서 값을 선택하세요', 0, 100, 50) # 슬라이더는 선택된 값을 반환
st.write(f'현재의 값은 {slider} 입니다.')

multi = st.multiselect('여기에서 여러 값을 선택하세요', ['선택 1', '선택 2', '선택 3']) # 멀티셀렉트박스는 선택된 값을 리스트로 반환
st.write(f'{type(multi) = }, {multi}가 선택되었습니다.')

button = st.button('여기를 클릭하세요') # 버튼은 클릭 여부를 반환
if button:
    st.write('버튼이 클릭되었습니다.(일반 텍스트: st.write()')
    st.success('버튼이 클릭되었습니다.(메시지: st.success())')  # 성공 메시지 출력
    st.balloons() # 풍선 애니메이션 출력
