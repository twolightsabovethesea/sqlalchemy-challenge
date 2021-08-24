# import Flask

from flask import Flask

# create an app using __name__

app = Flask(__name__)

#create home route

@app.route("/")
def home():
    

