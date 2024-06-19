import streamlit as st  # streamlit 라이브러리 임포트
import pandas as pd  # pandas 라이브러리 임포트
import numpy as np   # numpy 라이브러리 임포트
from PIL import Image  # 이미지 처리를 위한 PIL 라이브러리 임포트
import os  # 파일 경로 확인을 위한 os 라이브러리 임포트

st.set_page_config(
    page_title="창업하고 싶은 아이템",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 타이틀 텍스트 출력
st.title('창업하고 싶은 아이템')

st.markdown('''새로운 창업 아이디어를 소개합니다.  
각 아이디어는 데이터 분석 및 머신러닝 기술을 활용하여 다양한 문제를 해결하고, 더 나은 사용자 경험을 제공하는 것을 목표로 합니다.''')

# 스마트 콘텐츠 추천 시스템
st.header('📊 스마트 콘텐츠 추천 시스템')
st.markdown('''
사용자의 선호도를 분석하고 맞춤형 콘텐츠를 추천하는 시스템입니다. 
- **특징**: 
  - 실시간 데이터 분석을 통한 최신 트렌드 반영
  - 머신러닝 알고리즘을 사용한 개인 맞춤형 추천
  - 사용자의 시청, 클릭, 구매 데이터를 종합적으로 분석
- **기대 효과**:
  - 사용자가 원하는 콘텐츠를 빠르게 찾을 수 있어 만족도 증가
  - 콘텐츠 제공자의 수익 증대
''')
image_path1 = 'C:/StreamlitImage/1.png'
if os.path.exists(image_path1):
    img1 = Image.open(image_path1)  # 이미지 파일 열기
    st.image(img1, width=300)  # 이미지 출력
else:
    st.write("이미지 파일을 찾을 수 없습니다.")

# 소셜 네트워크 분석 도구
st.header('🔗 소셜 네트워크 분석 도구')
st.markdown('''
사용자 간의 연결 강도를 분석하여 인플루언서 및 주요 커뮤니티를 식별하는 도구입니다.
- **특징**:
  - 소셜 네트워크의 구조와 동향 분석
  - 주요 인플루언서 및 커뮤니티 식별
  - 사용자 활동 패턴 분석
- **기대 효과**:
  - 마케팅 전략 수립에 유용
  - 커뮤니티 관리 및 발전에 기여
''')
image_path2 = 'C:/StreamlitImage/2.png'
if os.path.exists(image_path2):
    img2 = Image.open(image_path2)  # 이미지 파일 열기
    st.image(img2, width=300)  # 이미지 출력
else:
    st.write("이미지 파일을 찾을 수 없습니다.")

# 모빌리티 데이터 분석 플랫폼
st.header('🚗 모빌리티 데이터 분석 플랫폼')
st.markdown('''
운행 데이터를 분석하여 교통 흐름을 최적화하고 경로를 추천하는 플랫폼입니다.
- **특징**:
  - 실시간 교통 상황 분석
  - 최적의 경로 추천
  - 긴급 차량 경로 최적화
- **기대 효과**:
  - 교통 혼잡 감소
  - 운행 시간 절약
  - 긴급 상황 대처 능력 향상
''')
image_path3 = 'C:/StreamlitImage/3.png'
if os.path.exists(image_path3):
    img3 = Image.open(image_path3)  # 이미지 파일 열기
    st.image(img3, width=300)  # 이미지 출력
else:
    st.write("이미지 파일을 찾을 수 없습니다.")

# 광고 효율성 분석 도구
st.header('📈 광고 효율성 분석 도구')
st.markdown('''
데이터를 수집하고 분석하여 광고 캠페인의 효율성을 최적화하는 도구입니다.
- **특징**:
  - 광고 성과 지표 분석
  - 머신러닝을 통한 타겟팅 광고 추천
  - 실시간 성과 모니터링
- **기대 효과**:
  - 광고 비용 절감
  - 효율적인 마케팅 전략 수립
  - ROI(투자 대비 수익) 극대화
''')
image_path4 = 'C:/StreamlitImage/4.png'
if os.path.exists(image_path4):
    img4 = Image.open(image_path4)  # 이미지 파일 열기
    st.image(img4, width=300)  # 이미지 출력
else:
    st.write("이미지 파일을 찾을 수 없습니다.")
