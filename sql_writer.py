import requests
import json
import click
from flask.cli import with_appcontext
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import psycopg2 



#FLASKSETUP
app=Flask(__name__)
#sqlite is working
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

#PostgreSQL isn't working
#app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:741852963Ugur@localhost:52150/fortest'

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db=SQLAlchemy(app)
migrate = Migrate(app, db)

class ads(db.Model):
    id=db.Column('id', db.Integer,primary_key=True,unique=True)
    ad_id=db.Column('ad_id',db.Integer,unique=True)
    currency=db.Column('currency',db.String) 
    Name=db.Column('Name',db.String) 
    developer_id=db.Column('developer_id',db.Integer)
    total_land=db.Column('total_land',db.Integer)
    total_units=db.Column('total_units',db.Integer)
    city_id=db.Column('city_id',db.String)
    latitude=db.Column('latitude',db.Integer)
    longitude=db.Column('longitude',db.Integer)
    max_unit_price=db.Column('max_unit_price',db.Integer)
    min_unit_price=db.Column('min_unit_price',db.Integer)
    district_id=db.Column('district_id',db.String)
    rt_score=db.Column('rt_score',db.Integer)


@click.command(name='create_tb')
@with_appcontext
def create_tb():
    
    db.create_all()

app.cli.add_command(create_tb)




@click.command(name='adparse')
@with_appcontext
def adparse():
   
   first=int(input("Choose start page="))
   limit=int(input("Choose page limit="))

   page_id=first
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
       

        add=ads(ad_id=f"{ad_id}",currency=f"{currency}",Name=f"{Name}",developer_id=f"{developer_id}",total_land=f"{total_land}",total_units=f"{total_units}",city_id=f"{city_id}",latitude=f"{latitude}",longitude=f"{longitude}",max_unit_price=f"{max_unit_price}",min_unit_price=f"{min_unit_price}",district_id=f"{district_id}",rt_score=f"{rt_score}")
        db.session.add(add)
        db.session.commit()
       
        ad+=1

     page_id+=1
app.cli.add_command(adparse)