# import Flask

from flask import Flask, jsonify

#import other dependencies

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

import numpy as np
import pandas as pd
import datetime as dt

# create engine to hawaii.sqlite
engine = create_engine("sqlite:///hawaii.sqlite", echo=False)

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables

Base.prepare(engine, reflect=True)

# View all of the classes that automap found

Base.classes.keys()

# Save references to each table

Measurement = Base.classes.measurement

Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

##
# include query for precitipation route

one_year = dt.date(2017,8,23) - dt.timedelta(days=365)

one_year

q = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= one_year)
q_dict = {}
for i in q:
    q_dict[i[0]]=i[1]

##
# include query for stations route

stationdata = session.query(Measurement.station, func.count(Measurement.station)).\
group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).all()
stationdata_dict = {}
for s in stationdata:
    stationdata_dict[s[0]] = s[1]

##
# include query for temperature observations route

temps = session.query(Measurement.date, Measurement.tobs).\
    filter(Measurement.station == 'USC00519281').\
    filter(Measurement.date >= one_year)
temps_dict = {}
for temp in temps:
    temps_dict[temp[0]] = temp[1]
    



# create an app using __name__

app = Flask(__name__)

#create home route

@app.route("/")
def home():
    print("Server recieved request for 'home' page")
    return(
        f"Welcome to the Hawaii Climate API!<br>"
        f"Available routes: <br>"
        f"<br>"
        f"Precipitation - return Hawaii precipitation data in JSON format: <br>"
        f"/api/v1.0/precipitation"
        f"<br>"
        f"Stations - return a list of stations in JSON format: <br>"
        f"/api/v1.0/stations"
        f"<br>"
        f"Observed Temperatures - return observed temperatures for a single station for one year in JSON format: <br>"
        f"/api/v1.0/tobs" 
        f"<br>"
        f"Start From - return min, max, and average temperatures in JSON format given a specified starting date: <br>"
        f"/api/v1.0/<start>" 
        f" <br>"
        f"Start-End - return min, max, and average temperatures in JSON format from a specified time period using start and end dates: <br>"
        f"/api/v1.0/<start>"
    )

#create precitipation route

@app.route("/api/v1.0/precipitation")
def precipitation():
    print("Server recieved request for 'precipitation' page")
    return jsonify(q_dict)
    
#create stations route

@app.route("/api/v1.0/stations")
def stations():
    print("Server recieved request for 'precipitation' page")
    return jsonify(stationdata_dict)
    

    
# create tobs route

@app.route("/api/v1.0/tobs")
def tobs():
    print("Server recieved request for 'tobs' page")
    return jsonify(temps_dict)

#create start route

@app.route("/api/v1.0/<start>")
def start(start.strptime()):
    print("Server recieved request for 'start' page")
    start_temps_dict = {}
    start_temps = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
    filter(Measurement.date >= start).all()
    for k in start_temps:
        start_temps_dict['TMIN'] = k[0]
        start_temps_dict['TMAX'] = k[1]
        start_temps_dict['TAVG'] = k[2]
    
#create start/end route

@app.route("/api/v1.0/<start>/<end>")
def start_end(start.strptime(),end.strptime()):
    print("Server recieved request for 'start_end' page")
    start_end_dict = {}
    start_end = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
    filter(Measurement.date >= start)
    filter(Measurement.date <= end).all()
    for d in start_temps:
        start_temps_dict['TMIN'] = d[0]
        start_temps_dict['TMAX'] = d[1]
        start_temps_dict['TAVG'] = d[2]
    
if __name__ == "__main__":
    app.run(debug=True)