import requests
import json,sys

#給定中央氣象局API key
authorization = "xxxx"
#給定要測試的url,這邊是使用全台灣一週天氣預報
url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-091"
#給定要查詢的城市
city_to_show = ["臺北市","臺中市"]

#發出request 確定狀態, 若status code 非 200 表示有問題 結束程式
res = requests.get(url,{"Authorization" : authorization})
if res.status_code == 200:
    print("url請求成功 獲取資料")
    data = res.json()
else:
    sys.exit("url請求失敗 請檢查")	 

#處理對象url返回給我們的內容
#這邊是用一開始給定的city_to_show, 找出指定的城市以及其平均溫度,並且打印出來
data = res.json()
cities = data["records"]["locations"][0]["location"]
for city in cities:
    for item in city_to_show:
        if item == city["locationName"]:
            print( city["locationName"] + " 一週的天氣預報 ")
            weatherelements = city["weatherElement"]
            for weatherelement in weatherelements:
                if weatherelement["elementName"] == "T":
                    #print(weatherelement["description"])
                    timedicts = weatherelement["time"]
                    for timedict in timedicts:
                        print(timedict["startTime"] + " 至 " + timedict["endTime"] + " 平均溫度為 " + timedict["elementValue"][0]["value"])
