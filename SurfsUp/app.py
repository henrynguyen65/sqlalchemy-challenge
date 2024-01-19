# Import the dependencies.
from flask import Flask, jsonify

# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
base = automap_base()

# reflect the tables
base.prepare(engine, reflect=True)

# Save references to each table
measurement = base.classes.measurement
station = base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

# Flask Setup
app = Flask(__name__)


# Flask Routes

@app.route("/")
def welcome():
    return (
        f"Welcome to the Climate App API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start_date<br/>"
        f"/api/v1.0/start_date/end_date"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Add your precipitation query logic here
    return jsonify({})

@app.route("/api/v1.0/stations")
def stations():
    # Add your stations query logic here
    return jsonify({})

@app.route("/api/v1.0/tobs")
def tobs():
    # Add your temperature observations query logic here
    return jsonify({})

@app.route("/api/v1.0/start_date")
def start_date():
    # Add your start date query logic here
    return jsonify({})

@app.route("/api/v1.0/start_date/end_date")
def start_end_date():
    # Add your start and end date query logic here
    return jsonify({})
