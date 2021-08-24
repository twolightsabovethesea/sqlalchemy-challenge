# import Flask

from flask import Flask

# create an app using __name__

app = Flask(__name__)

#create home route

@app.route("/")
def home():
    print("Server recieved request for 'home' page")

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