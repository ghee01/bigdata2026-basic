"""
작업일자 : 2026-08-03
작업자 : 노가희
목적 : train.py로 만든 churn_model.joblib를 실제로 시용하는 사용자화면 코드(웹페이지 화면), 시각적
데이터 파일 : ../ml_data/telecom_churn.csv

실행 : streamlit run streamlit_app.py
"""

# 라이브러리 불러오기
from pathlib import Path
import joblib
import pandas as pd
import streamlit as st

# 경로 설정
MODEL_PATH = Path(__file__).resolve().parent / 'churn_model.joblib'

# 브라우저 탭 제목과 아이콘 설정 - 반드시 다른 st.명령어보다 먼저 호출해야 한다
st.set_page_config(page_title='실습:고객 이탈 위험', page_icon='⚠️')

st.title('🚨고객 이탈 조기 경보')
st.caption('상담 우선순위를 정하기 위한 의사결정 보조 도구이며, 예측만으로 불이익을 주면 안됩니다')

# 모델 파일 존재 확인
if not MODEL_PATH.exists():
    st.error('모델 파일이 없습니다')
    st.stop()   # 스크립트 실행 완전 중단

# 저장했던 전처리+모델 복원
model = joblib.load(MODEL_PATH)

with st.form('customer'):
    pass