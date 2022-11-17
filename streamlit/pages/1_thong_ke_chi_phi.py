import streamlit as st
import time
import numpy as np
from utils import show_code
from business.giam_sat import GiamSat
import math
import pandas as pd

def thong_ke_chi_phi_2():
    giamsat = GiamSat()
    data = giamsat.load_thong_ke_chi_phi()
    
    df = pd.DataFrame(columns = ['ky_qt', 'bq_noi'])
    for item in data:
        df = pd.concat([df, pd.DataFrame([[item[0], item[7]]], columns = ['ky_qt', 'bq_noi'])])

    st.write(df)

    chart = st.line_chart(df, x = 'ky_qt')



def thong_ke_chi_phi():
    giamsat = GiamSat()

    data = giamsat.load_thong_ke_chi_phi()

    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()

    last_rows = [[data[0][0],data[0][7], data[0][8]]]
    chart_data = pd.DataFrame(last_rows ,
    columns= [ 'ky_qt', 'bq_noi', 'bq_ngoai']  
    )
    #chart_data['ky_qt'] = pd.to_datetime(chart_data['ky_qt'])
    #chart_data = chart_data.set_index('ky_qt')

    chart = st.line_chart(chart_data,
        x = 'ky_qt'
    )    

    for i in range(1, len(data)):        
        new_rows = pd.DataFrame([[data[i][0],data[i][7],data[i][8]]], columns
        =['ky_qt', 'bq_noi', 'bq_ngoai']
        )
        #new_rows['ky_qt'] = pd.to_datetime(new_rows['ky_qt'])
        #new_rows = new_rows.set_index('ky_qt')        
        percent = math.ceil((i+1)/len(data) * 100)
        status_text.text("%i%% Complete" % percent)
        chart.add_rows(new_rows.set_index('ky_qt'))
        progress_bar.progress(percent)
        # last_rows = new_rows
        time.sleep(0.1)                

    progress_bar.empty()
    st.button("Re-run")

st.set_page_config(page_title="Thống kê chi phí KCB", page_icon="📈")
st.markdown("# Thống kê chi phí KCB BHYT qua các năm")
st.sidebar.header("Thống kê chi phí KCB")
st.write("""
    Đây là bảng thống kê chi phí kcb bhyt qua các năm
""")

thong_ke_chi_phi()

show_code(thong_ke_chi_phi_2)