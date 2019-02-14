# 1. Import Flask

import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Stations = Base.classes.station
Measurement = Base.classes.measurement
# Create our session (link) from Python to the DB
session = Session(engine)

# 2. Create an app
app = Flask(__name__)


# 3. Define static routes
@app.route("/")
def index():
      return (
        f"Welcome!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>"
    )  


@app.route("/api/v1.0/precipitation")
def precipitation():
  # """Return a list of all preps and dates"""
    # Query all preps and dates
    results = session.query(Measurement.prcp).all()

    # Convert list of tuples into normal list
    all_temps = list(np.ravel(results))

    return jsonify(all_temps)


@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Stations.name).all()

    # Convert list of tuples into normal list
    all_stations = list(np.ravel(results))

    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():   
    results = session.query(Measurement.tobs).all()

    # Convert list of tuples into normal list
    all_tobs = list(np.ravel(results))

    return jsonify(all_tobs)

#@app.route("/api/v1.0/<start>")
#def start():

#@app.route("/api/v1.0/<start>/<end>")
#def end():


# 4. Define main behavior
if __name__ == "__main__":
    app.run(debug=True)
