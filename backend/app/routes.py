from flask import Flask, jsonify
from app.tasks.math import generate_math_problem

app = Flask(__name__)

@app.route('/math/problem', methods=['GET'])
def math_problem():
    problem = generate_math_problem()
    return jsonify(problem)

if __name__ == '__main__':
    app.run(debug=True)
