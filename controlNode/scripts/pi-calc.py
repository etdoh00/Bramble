import random
import sys
import time

from flask import Flask

app = Flask(__name__)

@app.route("/")
def calculate_pi():
    num_samples = int(sys.argv[1])
    inside_circle = 0
    for i in range(num_samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
    pi = 4 * inside_circle / num_samples
    return f"Estimated value of Pi: {pi:.6f}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)


#this script uses the flask framework to create a server that repsonds to http requests by
#running a monte carlo sim
