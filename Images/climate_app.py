# import Flask

from flask import Flask

# create an app using __name__

app = Flask(__name__)

#create home route

@app.route("/")
def home():
    

#create precitipation route

@app.route("/api/v1.0/precipitation")
def precipitation():
    
#create stations route

@app.route("/api/v1.0/stations")
def stations():

    
# create tobs route

@app.route("/api/v1.0/tobs")
def tobs():
    
