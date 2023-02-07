import requests
import streamlit as st
import pandas as pd

# Make a GET request to the API endpoint

service_key = '4d42486779706d3034365957634870'

url = f'http://openapi.seoul.go.kr:8088/{service_key}/json/tbLnOpendataRentV/1/5'

req = requests.get(url)
content = req.json()
con = content['tbLnOpendataRentV']['row']
data = []

# Check if the request was successful
if req.status_code == 200:
    # Get the JSON data from the response
    
    for h in con:
        dic = {}
        dic['SGG_CD'] = h['SGG_CD']
        dic['SGG_NM'] = h['SGG_NM']
        dic['BJDONG_CD'] = h['BJDONG_CD']
        dic['BJDONG_NM'] = h['BJDONG_NM']
        dic['BOBN'] = h['BOBN']
        dic['BUBN'] = h['BUBN']
        dic['FLR_NO'] = h['FLR_NO']
        dic['CNTRCT_DE'] = h['CNTRCT_DE']
        dic['RENT_GBN'] = h['RENT_GBN']
        dic['RENT_AREA'] = h['RENT_AREA']
        dic['RENT_GTN'] = h['RENT_GTN']
        dic['RENT_FEE'] = h['RENT_FEE']
        dic['BLDG_NM'] = h['BLDG_NM']
        dic['BUILD_YEAR'] = h['BUILD_YEAR']
        dic['HOUSE_GBN_NM'] = h['HOUSE_GBN_NM']
        data.append(dic)
        data3 = pd.DataFrame(data)
    st.write(type(data3))
    st.write(data3)
else:
    st.write("Failed")