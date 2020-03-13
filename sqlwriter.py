import requests
import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#FLASKSETUP
app=Flask(__name__)
#sqlite is working
#app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

#PostgreSQL isn't working
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:741852963Ugur@localhost:52150/fortest'

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db=SQLAlchemy(app)

class ads(db.Model):
    id=db.Column('id', db.Integer,primary_key=True)
    ad_id=db.Column(db.Integer)
    currency=db.Column(db.String) 
    Name=db.Column(db.String) 
    developer_id=db.Column(db.Integer)
    total_land=db.Column(db.Integer)
    total_units=db.Column(db.Integer)
    city_id=db.Column(db.String)
    latitude=db.Column(db.Integer)
    longitude=db.Column(db.Integer)
    max_unit_price=db.Column(db.Integer)
    min_unit_price=db.Column(db.Integer)
    district_id=db.Column(db.String)
    rt_score=db.Column(db.Integer)
    

db.create_all()



#PAGELIMITER
limit=int(input("Choose page limit="))

page_id=1
#PARSING
while page_id<=limit:
    
    url = "https://www.hurriyetemlak.com/projeler/estate/estateforbounds"

    payload = {'some': 'data','page': page_id}
    headers = {'content-type': 'application/json'}

    response = requests.post(url, data=json.dumps(payload,sort_keys=True), headers=headers)

    page=json.loads(response.content)
    data={}

    #AD PARSING
    ad=0
    while ad<=15:
       edited_page=page["ads"]
       json_ad=edited_page[ad]
       
       #AD CONFIG
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
    
       
       ad+=1

    page_id+=1
