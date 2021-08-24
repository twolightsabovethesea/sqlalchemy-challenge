# import Flask

from flask import Flask, jsonify

# create an app using __name__

app = Flask(__name__)

#create home route

@app.route("/")
def home():
    print("Server recieved request for 'home' page")
    return(
        f"Welcome to the Hawaii Climate API!"<br>
        f"Available routes:"<br>
        <br>
        f"Precipitation - return Hawaii precipitation data in JSON format:"<br>
        f"/api/v1.0/precipitation" <br>
        <br>
        f"Stations - return a list of stations in JSON format:"<br>
        f"/api/v1.0/stations" <br>
        <br>
        f"Observed Temperatures - return observed temperatures for a single station for one year in JSON format:"<br>
        f"/api/v1.0/tobs" <br>
        <br>
        f"Start From - return min, max, and average temperatures in JSON format given a specified starting date:"<br>
        f"/api/v1.0/<start>" <br>
        <br>
        f"Start-End - return min, max, and average temperatures in JSON format from a specified time period using start and end dates:"<br>
        f"/api/v1.0/<start>" <br>

#create precitipation route

@app.route("/api/v1.0/precipitation")
def precipitation():
    print("Server recieved request for 'precipitation' page")
    
#create stations route

@app.route("/api/v1.0/stations")
def stations():
    print("Server recieved request for 'precipitation' page")

    
# create tobs route

@app.route("/api/v1.0/tobs")
def tobs():
    print("Server recieved request for 'tobs' page")
#create start route

@app.route("/api/v1.0/<start>")
def start():
    print("Server recieved request for 'start' page")
    
#create start/end route

@app.route("/api/v1.0/<start>/<end>")
def start_end():
    print("Server recieved request for 'start_end' page")
    
if name == "__main__":
    app.run(debug=True)