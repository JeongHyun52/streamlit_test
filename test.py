import streamlit as st
import numpy as np
import pandas as pd
import joblib
import pydeck as pdk

# 구별로 의류수거함 위치 출력
def main_page_jongro():
    st.header('종로구')
    st.image('종로구.png')
    
def songpa():
    st.header('송파구')    
    st.image('송파구.png')
def gangseo():
    st.header('강서구')    
    st.image('강서구.png')

def gangnam():
    st.header('강남구')    
    st.image('강남구.png')

def dongdaemun():
    st.header('동대문구')    
    st.image('준비중.png')

def gangdong():
    st.header('강동구')    
    st.image('준비중.png')
    
def seongbuk():
    st.header('성북구')    
    st.image('준비중.png')
    
def seongdong():
    st.header('성동구')    
    st.image('준비중.png')
    
def nowon():
    st.header('노원구')    
    st.image('준비중.png')
    
def yongsan():
    st.header('용산구')    
    st.image('준비중.png')
    
def seocho():
    st.header('서초구')    
    st.image('준비중.png')
    
def gangbuk():
    st.header('강북구')    
    st.image('준비중.png')
    
def dongjak():
    st.header('동작구')    
    st.image('준비중.png')
    
def gwanak():
    st.header('관악구')    
    st.image('준비중.png')
    
def yangcheon():
    st.header('양천구')    
    st.image('준비중.png')
    
def guro():
    st.header('구로구')    
    st.image('준비중.png')
    
def gwangjin():
    st.header('광진구')    
    st.image('준비중.png')
    
def mapo():
    st.header('마포구')    
    st.image('준비중.png')
    
def jungrang():
    st.header('중랑구')    
    st.image('준비중.png')
    
def eunpyeong():
    st.header('은평구')    
    st.image('준비중.png')
    
def yeongdeungpo():
    st.header('영등포구')    
    st.image('준비중.png')
    
def geumcheon():
    st.header('금천구')    
    st.image('준비중.png')
    
def seodaemun():
    st.header('서대문구')    
    st.image('준비중.png')
    
def jung():
    st.header('중구')    
    st.image('준비중.png')
    
def dobong():
    st.header('도봉구')    
    st.image('준비중.png')
    
    
# 딕셔너리 선언 {  ‘selectbox항목’ : 페이지명 …  }
page_names_to_funcs = {'종로구':main_page_jongro, '송파구':songpa, '동대문구':dongdaemun, '강동구':gangdong, '성북구':seongbuk, '성동구':seongdong, '강남구':gangnam, '노원구':nowon, '용산구':yongsan, '강서구':gangseo, '서초구':seocho, '강북구':gangbuk, '동작구':dongjak, '관악구':gwanak, '양천구':yangcheon, '구로구':guro, '광진구':gwangjin, '마포구':mapo, '중랑구':jungrang, '은평구':eunpyeong, '영등포구':yeongdeungpo, '금천구':geumcheon, '서대문구':seodaemun, '중구':jung, '도봉구':dobong }

# 사이드 바에서 selectbox 선언 & 선택 결과 저장
selected_page = st.selectbox('Select a page',page_names_to_funcs.keys())

# 해당 페이지 부르기
page_names_to_funcs[selected_page]()


# def rfmodel(money, work, woman, marry, age2030, age_woman, trash):
#     loaded_model = joblib.load('./rf_model.pkl')
#     y_pred=loaded_model.predict([[money,  work,  woman,  marry,  age2030, age_woman,  trash]])
#     y_pred = str(y_pred)
#     y_pred = y_pred[1:-1]
#     col3_3.markdown('#### 배출량')
#     col3_3.info(y_pred)

# col1_1, col1_2, col1_3 = st.columns(3)
# money = col1_1.slider('평균급여를 입력해주세요', 0,1000, 1)
# col2_1, col2_2, col2_3 = st.columns(3)
# work = col2_1.slider('임금근로자 수를 입력해주세요', 0,1000, 1)
# col3_1, col3_2, col3_3 = st.columns(3)
# woman = col3_1.slider('여성인구를 입력해주세요', 0,1000, 1)
# col4_1, col4_2, col4_3 = st.columns(3)
# marry = col4_1.slider('미혼남녀 수를 입력해주세요', 0,1000, 1)
# col5_1, col5_2, col5_3 = st.columns(3)
# age2030 = col5_1.slider('2030인구를 입력해주세요', 0,1000, 1)
# col6_1, col6_2, col6_3 = st.columns(3)
# age_woman = col6_1.slider('2030 여성인구를 입력해주세요', 0,1000, 1)
# col7_1, col7_2, col7_3 = st.columns(3)
# trash = col7_1.slider('일반쓰레기 양을 입력해주세요', 0,1000, 1)
# rfmodel(money, work, woman, marry, age2030, age_woman, trash)


# chart_data = pd.read_csv('2주차_데이터셋.csv', encoding='cp949')
# st.line_chart(data=chart_data, y='여성인구')

import plotly.express as px
chart_data = pd.read_csv('자치구별_배출량.csv', encoding='cp949')
fig = px.bar(chart_data, x='자치구', y='폐의류 배출량', text_auto=True, title='자치구별 폐의류 배출량')
st.plotly_chart(fig)
