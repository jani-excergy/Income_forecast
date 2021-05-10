# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 06:05:21 2021

"""
import numpy as np
import pandas as pd
import pickle
import streamlit as st
import math




pickle_in = open("time_forecast_2.pkl","rb")
model=pickle.load(pickle_in)

Mean_encoded_Income={90006: 48859.675,
 90008: 115060.87,
 90019: 51674.87,
 90022: 94156.55,
 90039: 121328.92,
 90045: 83225.34,
 90048: 68014.91,
 90049: 23933.54,
 90056: 146926.6,
 90059: 188652.92,
 90065: 95731.35,
 90066: 114742.73,
 90069: 82783.43,
 90201: 177410.42,
 90210: 63865.115,
 90220: 97789.81,
 90222: 107784.39,
 90240: 84356.17,
 90242: 52592.07,
 90245: 64231.93,
 90247: 130172.56,
 90249: 152346.75,
 90250: 32850.8,
 90262: 122574.406,
 90265: 60071.26,
 90275: 140071.41,
 90277: 279776.85,
 90303: 124675.4,
 90304: 36992.0,
 90403: 53960.72,
 90501: 92858.79,
 90504: 102857.38,
 90505: 128854.58,
 90601: 125343.60500000001,
 90603: 13836.0,
 90604: 1442.66,
 90606: 214287.195,
 90620: 128646.57666666668,
 90630: 41849.9,
 90631: 63902.24875,
 90638: 32925.41,
 90640: 35357.215,
 90650: 108596.07800000001,
 90660: 121130.75,
 90670: 21842.905,
 90680: 36504.72,
 90703: 69090.475,
 90710: 24089.0,
 90712: 208.43,
 90713: 122188.35333333333,
 90717: 124473.84,
 90742: 197808.55,
 90744: 153092.19,
 90745: 55735.08,
 90746: 88.0,
 90755: 2925.69,
 90806: 104509.01,
 90807: 101692.08499999999,
 90808: 108275.02,
 90815: 44012.55,
 91024: 65573.29,
 91104: 82920.44,
 91208: 847.0,
 91214: 76878.35,
 91306: 751.0,
 91311: 101839.73,
 91331: 67090.81,
 91352: 107272.21,
 91355: 31645.96,
 91405: 124470.87,
 91505: 58053.0,
 91605: 114714.14,
 91706: 45289.92,
 91722: 58058.55,
 91724: 110382.505,
 91733: 84259.98,
 91741: 46714.92,
 91744: 160116.3,
 91745: 132138.67500000002,
 91746: 126763.84,
 91752: 189499.97,
 91765: 96404.02,
 91766: 165622.06,
 91767: 16522.0,
 91773: 61277.82,
 91775: 138051.26,
 91776: 103213.11,
 91780: 79380.38,
 91789: 144402.6133333333,
 91791: 100515.06999999999,
 92201: 94838.49333333333,
 92203: 101549.87,
 92210: 159452.8,
 92211: 134017.5125,
 92220: 54158.5125,
 92234: 19522.94,
 92240: 59348.82,
 92253: 96131.54666666668,
 92260: 95589.476,
 92262: 74498.87,
 92264: 145142.385,
 92270: 74986.87000000001,
 92501: 109314.57999999999,
 92503: 101046.0625,
 92504: 165073.22,
 92505: 182552.48,
 92506: 101086.865,
 92507: 129218.67,
 92508: 122186.72000000002,
 92509: 33096.07666666667,
 92543: 77355.7,
 92544: 72048.78,
 92553: 153722.61666666667,
 92555: 133481.53,
 92557: 130070.17000000001,
 92562: 15559.7,
 92563: 69443.98666666666,
 92571: 186628.58,
 92584: 99625.26,
 92587: 96350.74500000001,
 92592: 97581.055,
 92595: 3616.0,
 92596: 21496.93,
 92602: 23112.77,
 92606: 110329.465,
 92612: 223768.01,
 92614: 131203.91,
 92620: 128642.08666666667,
 92627: 67736.95999999999,
 92630: 47461.3,
 92647: 98740.35,
 92648: 104138.58499999999,
 92649: 71885.605,
 92653: 223269.32,
 92656: 9433.0,
 92660: 123509.09,
 92661: 1252.0,
 92662: 30655.99,
 92663: 114534.21,
 92677: 77898.77857142859,
 92679: 180552.875,
 92683: 190746.16,
 92688: 104056.855,
 92703: 144841.46,
 92704: 185950.495,
 92705: 147820.3575,
 92706: 57214.11,
 92708: 154517.63,
 92780: 131518.575,
 92782: 144100.35,
 92801: 69715.785,
 92802: 145490.06,
 92804: 144666.80666666667,
 92805: 115451.515,
 92806: 80253.12,
 92807: 89202.565,
 92808: 94228.1875,
 92821: 108662.815,
 92823: 221180.07,
 92833: 83007.63,
 92835: 58140.31333333333,
 92840: 60903.12333333333,
 92860: 78196.4,
 92861: 5042.0,
 92867: 99387.80666666666,
 92869: 89756.84999999999,
 92870: 54263.088,
 92879: 2014.0,
 92880: 60198.704999999994,
 92881: 66516.5,
 92882: 219128.84,
 92883: 166244.7,
 92886: 16632.266666666666}

def welcome():
    return " welcome all"


def forecast(f1,f2,f3,f4,year,month_cos,week_sin,quarter_sin):
    
    
    prediction=model.predict(np.array([[f1,f2,f3,f4,year,month_cos,week_sin,quarter_sin]]))
    print(prediction)
    return prediction


def main():
    st.title("Income Forecast App")
    html_temp = """
    <div style="background-color:green;padding:20px">
    <h2 style="color:white;text-align:center;">Income Forecasting</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Date=st.date_input('Date input')
    Completed_Jobs= st.number_input(label="Completed_Jobs",format="%f")
    Avg_Sales = st.number_input(label="Avg_sales",format="%f")
    Tech_Count = st.number_input(label="Tech_count",format="%f")
    Max_Temp = st.number_input(label="Max_Temp",format="%f")
    Zipcode = st.number_input(label="Zipcode",format="%f")
    

    if Zipcode in list(Mean_encoded_Income.keys()):
        Zipcode=(Mean_encoded_Income[Zipcode])
    
    
    else:
        print('Enter correct zip')
    
    
    f1=np.abs(Completed_Jobs)*np.abs(Zipcode)
    f2=np.sqrt(Completed_Jobs**3)*np.abs(Avg_Sales)
    f3=np.abs(np.sqrt(Completed_Jobs) - np.sqrt(Tech_Count))
    f4=np.log(np.sqrt(Completed_Jobs)*Max_Temp**3)
    dates=pd.to_datetime(Date)
    week_day=dates.weekday
    month=dates.month
    year=dates.year
    quater=dates.quarter
    week_sin = np.sin(2 * np.pi * (week_day()/7))
    month_cos= np.cos(2 * np.pi * (month/12))
    quarter_sin = np.sin(2 * np.pi * (quater/4))
    
    if year==2020:
        year==1
    else:
        year==0

    
    
    
    result=""
    if st.button("Predict"):
        result=forecast(f1,f2,f3,f4,year,month_cos,week_sin,quarter_sin)
    st.success('The Forecasted Income {}'.format(result))
    if st.button("About"):
        st.text("datacube.ai")
        st.text(" 2021 ")

if __name__=='__main__':
    main()


