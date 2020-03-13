import requests
import json
import psycopg2

#CONNECTION DB
con=psycopg2.connect(
       host="127.0.0.1",
       database="fortest",
       user="postgres",
       password="741852963ugur")

cursor= con.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS ads(ad_id uuid,currency varchar,Name varchar,developer_id varchar,total_land INT,total_units smallint,city_id varchar,latitude point,longitude point,max_unit_price numeric,min_unit_price numeric,district_id varchar,rt_score INT)")
con.commit()

limit=int(input("Choose page limit="))

page_id=1

while page_id<=limit:
    
    url = "https://www.hurriyetemlak.com/projeler/estate/estateforbounds"

    payload = {'some': 'data','page': page_id}
    headers = {'content-type': 'application/json'}

    response = requests.post(url, data=json.dumps(payload,sort_keys=True), headers=headers)

    page=json.loads(response.content)
    data={}


    ad=0
    while ad<=15:
       edited_page=page["ads"]
       json_ad=edited_page[ad]
       
       
       ad_id = json_ad["Id"]
       currency = json_ad["CurrentCurrency"]
       Name = json_ad["NameSeo"]
       developer_id = json_ad["DeveloperId"]
       total_land = json_ad["MaxSize"]
       total_units = json_ad["MaxRoomCount"]
       city_id = json_ad["CityName"]
       latitude = json_ad["Latitude"]
       longitude = json_ad["Longitude"]
       max_unit_price = json_ad["MaxPrice"]
       min_unit_price = json_ad["MinPrice"]
       district_id = json_ad["DistrictName"]
       rt_score = json_ad["Quality"]
       
       cursor.execute(f"INSERT INTO ads Values({ad_id},{currency},{Name},{developer_id},{total_land},{total_units},{city_id},{latitude},{longitude},{max_unit_price},{min_unit_price},{district_id},{rt_score})")
       con.commit()
       
       
       ad+=1

    page_id+=1

cursor.close()
con.close()