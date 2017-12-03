from flask import Flask, render_template, request
from utils import time_deficit_calculator

app = Flask(__name__)
app.secret_key = 'physics_calculator'

@app.route("/")
def main(methods = ["GET"]):
        if "clock_type" in request.args:
                if request.args["clock_type"] == "equatorial":
                        clock = time_deficit_calculator.calculate_time_deficit(1)
                elif request.args["clock_type"] == "satellite":
                        radius = request.args["radius"]
                        if radius == "" or not time_deficit_calculator.valid_satellite_radius(radius):
                                error = "Please enter a valid radius (must be greater than or equal to the Earth's radius: 6.371e6 meters)."
                                return render_template("index.html", error = error)
                        clock = time_deficit_calculator.calculate_time_deficit(2, float(radius))
                return render_template("index.html", clock_type = clock.clock_type, results = clock.get_time_deficit_results())
        
        return render_template("index.html")

if __name__ == '__main__':
        app.debug = True
        app.run()

