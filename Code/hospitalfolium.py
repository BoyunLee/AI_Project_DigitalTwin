import folium
import folium as g
import webbrowser
import base64
import pandas as pd
import sqlite3

#기준이 되는 map 설정 및 크기 설정
m = folium.Map(location=[37.567418,126.967106],
               zoom_start=12)

# SQLite3 데이터베이스 연결
df = pd.read_excel("C:\\project1\\응급실_목록_서울.xlsx")

for i in range(df.shape[0]):
    folium.Marker([df.iloc[i]['위도'], df.iloc[i]['경도']], # 위도, 경도
                  popup = f'<strong>{df.iloc[i]["병원명"]}</strong>', #마우스 클릭시 표기되는 문구
                  tooltip="click").add_to(m)

m.save('hospital.html')
webbrowser.open_new_tab('hospital.html')
# # 데이터에서 위치 정보 추출하고 지도에 마커 추가하기
# for item in data:
#     lat = item[0]
#     lon = item[1]
#     popup = item[2]
#     folium.Marker([lat, lon], popup=popup).add_to(m)

# latlon=[
#     [35.134032, 129.1031735],
#     [35.11756677459287, 129.09057651986794],
#     [35.1380363, 129.0924108]
#   
# ]
   

# pic = base64.b64encode(open('sum.jpg', 'rb').read()).decode()
# image_tag = '<img src="data:image/jpeg;base64,{}">'.format(pic)
# iframe = folium.IFrame(image_tag, width=230, height=100)
# popup = folium.Popup(iframe, max_width=650)

# for i in range(len(latlon)):
#     folium.Marker(latlon[i],
#                   popup = 'popup',
#                   tooltip="부경대학교").add_to(m)

#webbrowser 활성화
# m.save('filename.html')
# webbrowser.open_new_tab('filename.html')