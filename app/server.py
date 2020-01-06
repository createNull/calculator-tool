import os

from flask import Flask, render_template, request, redirect
from utils import run_algorithm

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<algorithm_name>/', methods=["GET", "POST"])
def algorithm_calculator(algorithm_name: str):
    if request.method == 'GET' and algorithm_name in ("Fibonacci", "Ackermann", "Factorial"):
        return render_template('algorithm.html', name=algorithm_name)

    elif request.method == 'POST':
        user_input = [request.form.get('parameter')]
        if algorithm_name == 'Ackermann':
            user_input.append(request.form.get('second-parameter'))

        result, exec_time = run_algorithm(algorithm_name, user_input)
        if exec_time:
            return render_template('algorithm.html', name=algorithm_name, result=result, exec_time=exec_time)
        return render_template('algorithm.html', name=algorithm_name, error_message=result)

    else:
        return redirect('/'), 404, {"Refresh": "3; url=/"}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
