'''
bigdata2026-basic/subwaypages_src/data_loader.py

작성자 : 노가희
작성일 : 2026-08-05
목적 : 여러 페이지에서 공통으로 사용하는 "csv 불러오기" 함수를 한 곳에 모아둔 파일
'''
import streamlit as st
import pandas as pd

# 월요일부터 순서대로 정렬해서 보여주기 위한 고정 순서
WEEKDAY_ORDER = ['월', '화', '수', '목', '금', '토', '일']

@st.cache_data
def load_subway(path: str='./input/subway_long.csv') -> pd.DataFrame:
    """
    subway_long.csv를 읽어 반환 (대구 지하철 시간대별 승하차 데이터)
    """
    dtype_map = {   # 문자열로 반복되는 컬럼은 category 타입으로 읽어 메모리 절약
        '역명':'category',
        '승하차':'category',
        '시간대컬럼':'category',
        '요일코드':'category'
    }

    df = pd.read_csv(path, dtype=dtype_map)

    # 날짜 컬럼은 datetime 형태
    df['날짜'] = pd.to_datetime(df['날짜'])

    # 요일코드 컬럼 '정렬 가능한' 순서형(Categorical)으로 바꾼다
    # 그룹이나 그래프 등 작업시 항상 월~일 순서로 나오게 하기 위한 작업(안하면 데이터 등장 순서대로 정렬)
    df['요일코드'] = pd.Categorical(df['요일코드'], categories=WEEKDAY_ORDER, ordered=True)

    return df