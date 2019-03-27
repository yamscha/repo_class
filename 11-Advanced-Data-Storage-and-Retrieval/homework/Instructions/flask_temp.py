import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#create a connection to a sqlite database 
engine = create_engine('sqlite:///hawaii2.sqlite')

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
ME = Base.classes.measurement

ST = Base.classes.stations

# Create our session (link) from Python to the DB
session = Session(engine)

app = Flask(__name__)

# Flask Routes
# Flask Routes
@app.route("/api/v1.0/precipitation")
def names():
    tobs_list =[]
    tob_12 = session.query(ME.date,ME.tobs).\
             filter((ME.date >='2016-08-23') & (ME.date <='2017-08-23')).\
             order_by(ME.date).all()
    
    for i in tob_12:
        tobs_dict ={}
        tobs_dict['date'] = i.date
        tobs_dict['tobs'] =i.tobs
        tobs_list.append(tobs_dict)
    
    return jsonify(tobs_list)

#* Return a json list of stations from the dataset.
@app.route("/api/v1.0/stations")
def stations():
    stations_query = session.query(ST.station,ST.name).all()
                     
    # Convert list of tuples into normal list
    station_list = list(np.ravel(stations_query))

    return jsonify(station_list)   

@app.route("/api/v1.0/start")
def start_date():
    temp_query = session.query(ME.date,func.min(ME.tobs),func.max(ME.tobs),func.avg(ME.tobs)).\
                 filter(ME.date =='2017-08-15').\
                 order_by(ME.date).all()
    temp_list = list(np.ravel(temp_query))   
    return jsonify(temp_list)

@app.route("/api/v1.0/startdategreater")
def startdate_greater():
    temp_query1 = session.query(ME.date,func.min(ME.tobs),func.max(ME.tobs),func.avg(ME.tobs)).\
                 filter(ME.date >='2017-08-15').\
                 order_by(ME.date).all()
    temp_list1 = list(np.ravel(temp_query1))   
    return jsonify(temp_list1)
        
@app.route("/api/v1.0/startenddate")

def start_end_date():
    temp_query2 = session.query(ME.date,func.min(ME.tobs),func.max(ME.tobs),func.avg(ME.tobs)).\
                 filter((ME.date >='2017-08-01') & (ME.date <= '2017-08-23')).\
                 order_by(ME.date).all()
    temp_list2 = list(np.ravel(temp_query2))  
   
    return jsonify(temp_list2)
                 

if __name__ == '__main__':
    app.run(debug=True)

 
