import os

from flask import Flask, render_template, request
from utils import get_result

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<algorithm_name>/', methods=["GET", "POST"])
def algorithm_calculator(algorithm_name, result='', exec_time=''):
    if request.method == 'GET' and algorithm_name in ("Fibonacci", "Ackermann", "Factorial"):
        return render_template('algorithm.html', name=algorithm_name, result=result, exec_time=exec_time)

    if request.method == 'POST':
        user_input = [request.form.get('parameter')]
        if algorithm_name == 'Ackermann':
            user_input.append(request.form.get('second-parameter'))
        try:
            result, exec_time = get_result(f'{algorithm_name}', user_input)
        except ValueError:
            result = get_result(f'{algorithm_name}', user_input)
            return render_template('algorithm.html', name=algorithm_name, error_message=result)

        return render_template('algorithm.html', name=algorithm_name, result=result, exec_time=exec_time)


if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5000)))
