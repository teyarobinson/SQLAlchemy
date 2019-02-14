# 1. Import Flask
from flask import Flask


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
  


@app.route("/api/v1.0/stations")
def stations():

@app.route("/api/v1.0/tobs")
def tobs():   

@app.route("/api/v1.0/<start>")
def start():

@app.route("/api/v1.0/<start>/<end>")
def end():


# 4. Define main behavior
if __name__ == "__main__":
    app.run(debug=True)
