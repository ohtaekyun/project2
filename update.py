import requests
import pandas as pd
import streamlit as st
import numpy as np
import csv
import sqlite3
import time
from datetime import datetime

# #[1]DB생성-->Conncetion객체의-->connect()함수를 사용하여 생성
# dbConn=sqlite3.connect('mydata.db')
# print(type(dbConn)) #sqlite3.Conncetion 객체.

# #[2]DB커서 객체 생성-->Conncetion객체인 dbConn을 사용해 Cursor객체를 생성.
# cs=dbConn.cursor()
# print(type(cs)) #sqlite3.Cursor객체.

# #[3]DB테이블 생성
# # cs.execute("Create table if not exists tbl_PublicAPI)_")
# cs.execute('Create table if not exists tbl_PublicAPI(SGG_CD varchar, SGG_NM varchar, BJDONG_CD varchar, BJDONG_NM varchar, BOBN varchar, BUBN varchar, FLR_NO varchar, CNTRCT_DE varchar, RENT_GBN varchar, RENT_AREA varchar, RENT_GTN varchar, RENT_FEE varchar, BLDG_NM varchar, BUILD_YEAR varchar, HOUSE_GBN_NM varchar)')

# # #[1]csv파일 읽기-->open()사용-->csv.reader()메서드 사용하여 한 줄씩 읽기.
# fileName="data/bds_data.csv"
# file=open(fileName,"r")
# reader=csv.reader(file)
# st.write(reader)



#[3]순회하면서 할 일 처리.
# arr=[]

# for row in reader:
#     # print(row)
#     arr.append(row)
    
# for row in arr:
#     strSQL="INSERT INTO tbl_PublicAPI(SGG_CD,SGG_NM,BJDONG_CD,BJDONG_NM,BOBN,BUBN,FLR_NO,CNTRCT_DE,RENT_GBN,RENT_AREA,RENT_GTN,RENT_FEE,BLDG_NM,BUILD_YEAR,HOUSE_GBN_NM)values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
#     cs.execute(strSQL,(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]))

# dbConn.commit()

# 출력
# [2]DB연결 및 커서 객체 생성
# dbConn=sqlite3.connect("mydata.db")
# cs=dbConn.cursor()

# #[4]DB데이터 출력
# def db_list():
#     cs.execute('SELECT * FROM tbl_PublicAPI')
#     sugg = cs.fetchall()
#     return sugg

# list = db_list()     
# df0 = pd.DataFrame(list, columns=['SGG_CD','SGG_NM','BJDONG_CD','BJDONG_NM','BOBN','BUBN','FLR_NO','CNTRCT_DE','RENT_GBN','RENT_AREA','RENT_GTN','RENT_FEE','BLDG_NM','BUILD_YEAR','HOUSE_GBN_NM'])     
# df0 = df0.drop(0, axis=0)
# st.write(df0)


# service_key = '4d42486779706d3034365957634870'
# data = []

# for j in range(1,4):
#     url = f'http://openapi.seoul.go.kr:8088/{service_key}/json/tbLnOpendataRentV/{1+((j-1)*1000)}/{j*1000}'
#     print(url)
#     req = requests.get(url)
#     content = req.json()
#     con = content['tbLnOpendataRentV']['row']

#     for h in con:
#         dic = {}
#         dic['SGG_CD'] = h['SGG_CD']
#         dic['SGG_NM'] = h['SGG_NM']
#         dic['BJDONG_CD'] = h['BJDONG_CD']
#         dic['BJDONG_NM'] = h['BJDONG_NM']
#         dic['BOBN'] = h['BOBN']
#         dic['BUBN'] = h['BUBN']
#         dic['FLR_NO'] = h['FLR_NO']
#         dic['CNTRCT_DE'] = h['CNTRCT_DE']
#         dic['RENT_GBN'] = h['RENT_GBN']
#         dic['RENT_AREA'] = h['RENT_AREA']
#         dic['RENT_GTN'] = h['RENT_GTN']
#         dic['RENT_FEE'] = h['RENT_FEE']
#         dic['BLDG_NM'] = h['BLDG_NM']
#         dic['BUILD_YEAR'] = h['BUILD_YEAR']
#         dic['HOUSE_GBN_NM'] = h['HOUSE_GBN_NM']
#         data.append(dic)
# # #   ===
# # # --
# df = pd.DataFrame(data)
# df['BOBN'].replace('', np.nan, inplace=True)
# df['BUBN'].replace('', np.nan, inplace=True)
# df['BLDG_NM'].replace('', np.nan, inplace=True)
# df['BUILD_YEAR'].replace('', np.nan, inplace=True)
# df['CNTRCT_DE'] = df['CNTRCT_DE'].astype('str')
# df['CNTRCT_DE'] = df['CNTRCT_DE'].apply(lambda x: pd.to_datetime(str(x), format="%Y/%m/%d"))
# df['CNTRCT_DE'] = df['CNTRCT_DE'].astype('str')
# df['CNTRCT_DE'].replace('T00:00:00', '', inplace=True)
# df = df.dropna()

# df.drop(index = df[df['CNTRCT_DE']=='2023-01-30'].index, inplace=True)

# df2 = pd.concat([df,df0])

# st.write(df)

# df2.to_sql('budonsan',dbConn, index=False)



# def db1_list():
#     cs.execute('SELECT * FROM budonsan')
#     bds = cs.fetchall()
#     return bds

# list2 = db1_list()     
# df0 = pd.DataFrame(list2, columns=['SGG_CD','SGG_NM','BJDONG_CD','BJDONG_NM','BOBN','BUBN','FLR_NO','CNTRCT_DE','RENT_GBN','RENT_AREA','RENT_GTN','RENT_FEE','BLDG_NM','BUILD_YEAR','HOUSE_GBN_NM'])     
# df0 = df0.drop(0, axis=0)
# st.write(df0)
# cs.execute('DROP table budongsan')
# cs.execute('drop table budonsan')
# cs.execute('SELECT * FROM budonsan')
# bds = cs.fetchall()
# st.write(bds)
# st.write(type(bds))
# st.write(bds.keys())

# today = datetime.today()
# today = today.strftime("%Y-%m-%d") 
# st.write(today)

# service_key = '4d42486779706d3034365957634870'
# data = []

# for j in range(1,2):
#     url = f'http://openapi.seoul.go.kr:8088/{service_key}/json/tbLnOpendataRentV/{1+((j-1)*1000)}/{j*1000}'
#     print(url)
#     req = requests.get(url)
#     content = req.json()
#     con = content['tbLnOpendataRentV']['row']

#     for h in con:
#         dic = {}
#         dic['SGG_CD'] = h['SGG_CD']
#         dic['SGG_NM'] = h['SGG_NM']
#         dic['BJDONG_CD'] = h['BJDONG_CD']
#         dic['BJDONG_NM'] = h['BJDONG_NM']
#         dic['BOBN'] = h['BOBN']
#         dic['BUBN'] = h['BUBN']
#         dic['FLR_NO'] = h['FLR_NO']
#         dic['CNTRCT_DE'] = h['CNTRCT_DE']
#         dic['RENT_GBN'] = h['RENT_GBN']
#         dic['RENT_AREA'] = h['RENT_AREA']
#         dic['RENT_GTN'] = h['RENT_GTN']
#         dic['RENT_FEE'] = h['RENT_FEE']
#         dic['BLDG_NM'] = h['BLDG_NM']
#         dic['BUILD_YEAR'] = h['BUILD_YEAR']
#         dic['HOUSE_GBN_NM'] = h['HOUSE_GBN_NM']
#         data.append(dic)
# # #   ===
# # # --
# df = pd.DataFrame(data)
# df['BOBN'].replace('', np.nan, inplace=True)
# df['BUBN'].replace('', np.nan, inplace=True)
# df['BLDG_NM'].replace('', np.nan, inplace=True)
# df['BUILD_YEAR'].replace('', np.nan, inplace=True)
# df['CNTRCT_DE'] = df['CNTRCT_DE'].astype('str')
# df['CNTRCT_DE'] = df['CNTRCT_DE'].apply(lambda x: pd.to_datetime(str(x), format="%Y/%m/%d"))
# df['CNTRCT_DE'] = df['CNTRCT_DE'].astype('str')
# df['CNTRCT_DE'].replace('T00:00:00', '', inplace=True)
# df = df.dropna()

# dbConn=sqlite3.connect("mydata.db")
# cs=dbConn.cursor()

# arr=[]

# for row in reader:
#     # print(row)
#     arr.append(row)
    
# for row in arr:
#     strSQL="INSERT INTO budongsan(SGG_CD,SGG_NM,BJDONG_CD,BJDONG_NM,BOBN,BUBN,FLR_NO,CNTRCT_DE,RENT_GBN,RENT_AREA,RENT_GTN,RENT_FEE,BLDG_NM,BUILD_YEAR,HOUSE_GBN_NM)values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) where not exists (select * from budongsan)"
#     cs.execute(strSQL,(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]))

# dbConn.commit()


# # db 접속
# dbConn=sqlite3.connect("data/mydata.db")
# cs=dbConn.cursor()

# # db에서 budongsan 테이블 조회(날짜 최신순)
# def bds_list():
#     cs.execute('SELECT * FROM budonsan ORDER BY 8 desc')
#     bds = cs.fetchall()
#     return bds

# # 데이터 프레임 만들기
# bds_list = bds_list()     
# df = pd.DataFrame(bds_list, columns=['SGG_CD','SGG_NM','BJDONG_CD','BJDONG_NM','BOBN','BUBN','FLR_NO','CNTRCT_DE','RENT_GBN','RENT_AREA','RENT_GTN','RENT_FEE','BLDG_NM','BUILD_YEAR','HOUSE_GBN_NM'])     
# df = df.drop(0, axis=0)
# df = df.astype({'RENT_AREA' : 'float'})
# df = df.astype({'FLR_NO' : 'float'})
# df = df.astype({'FLR_NO' : 'int'})

# st.write(df)

# # db 접속 종료
# cs.close()
# dbConn.close()

dbConn = sqlite3.connect("data/mydata.db")
cs = dbConn.cursor()

# cs.execute('select * from tbl_PublicAPI')
# bds = cs.fetchall()
# st.write(bds)

service_key = '4d42486779706d3034365957634870'
data = []

for j in range(1,2):
    url = f'http://openapi.seoul.go.kr:8088/{service_key}/json/tbLnOpendataRentV/{1+((j-1)*1000)}/{j*1000}'
    
    req = requests.get(url)
    content = req.json()
    con = content['tbLnOpendataRentV']['row']
    

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
        st.write(dic)
        st.write(data)
# #   ===
# # --
df = pd.DataFrame(data)
df['BOBN'].replace('', np.nan, inplace=True)
df['BUBN'].replace('', np.nan, inplace=True)
df['BLDG_NM'].replace('', np.nan, inplace=True)
df['BUILD_YEAR'].replace('', np.nan, inplace=True)
df['CNTRCT_DE'] = df['CNTRCT_DE'].astype('str')
df['CNTRCT_DE'] = df['CNTRCT_DE'].apply(lambda x: pd.to_datetime(str(x), format="%Y/%m/%d"))
df['CNTRCT_DE'] = df['CNTRCT_DE'].astype('str')
df['CNTRCT_DE'].replace('T00:00:00', '', inplace=True)
df = df.dropna()

df['FLR_NO'] = df['FLR_NO'].astype('int')
df['FLR_NO'] = df['FLR_NO'].astype('str')
df['RENT_AREA'] = df['RENT_AREA'].astype('str') 
st.write(type(df))
st.write(df)
# cs.execute('SELECT * FROM sqlite_schema')
# a = cs.fetchall()
# st.write(a)

cs.execute('Create table if not exists test3(SGG_CD text, SGG_NM text, BJDONG_CD text, BJDONG_NM text, BOBN text, BUBN text, FLR_NO text, CNTRCT_DE text, RENT_GBN text, RENT_AREA text, RENT_GTN text, RENT_FEE text, BLDG_NM text, BUILD_YEAR text, HOUSE_GBN_NM text)')
for row in df.itertuples():
    strSQL="INSERT OR IGNORE INTO test3(SGG_CD,SGG_NM,BJDONG_CD,BJDONG_NM,BOBN,BUBN,FLR_NO,CNTRCT_DE,RENT_GBN,RENT_AREA,RENT_GTN,RENT_FEE,BLDG_NM,BUILD_YEAR,HOUSE_GBN_NM)values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    cs.execute(strSQL,(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15]))
dbConn.commit()

def db_list():
    cs.execute('SELECT * FROM test3 ORDER BY 8 desc')
    sugg = cs.fetchall()
    return sugg

list = db_list()     
df0 = pd.DataFrame(list, columns=['SGG_CD','SGG_NM','BJDONG_CD','BJDONG_NM','BOBN','BUBN','FLR_NO','CNTRCT_DE','RENT_GBN','RENT_AREA','RENT_GTN','RENT_FEE','BLDG_NM','BUILD_YEAR','HOUSE_GBN_NM'])     
df0 = df0.drop(0, axis=0)
st.write(df0.dtypes)
st.write(df0)

# cs.execute('SELECT * FROM tbl_PublicAPI')
# test = cs.fetchall()
# st.write(test)

cs.close()
dbConn.close()