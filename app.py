from flask import Flask, render_template, redirect, request
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")

@app.route("/")
def index():
    marsData = mongo.db.mars.find_one()
    
    return render_template("index.html", mars_dict=marsData)

@app.route("/scrape")
def scraper():
    
    
    mars_data = scrape_mars.scrape_all()
    
    mongo.db.mars.update({}, mars_data, upsert=True)
    return redirect("/", code=302)





if __name__ == "__main__":
    app.run(debug=True)
