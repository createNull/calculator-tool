from flask import Flask, render_template, request, abort
from timeout_decorator import timeout, TimeoutError

from utils import run_algorithm

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<algorithm_name>/', methods=["GET", "POST"])
@timeout(3)
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
        abort(404)


@app.errorhandler(404)
def handle_file_not_found(e):
    error_code = '404'
    error_name = 'File Not Found'
    error_text = "Oops, the page you're looking for doesn't exist."
    return render_template('error.html', error_code=error_code, error_name=error_name, error_text=error_text), 404


@app.errorhandler(TimeoutError)
def handle_timeout(e):
    error_code = '408'
    error_name = 'Request Timeout'
    error_text = 'Looks like the server is taking too long to respond, please try again later.'
    return render_template('error.html', error_code=error_code, error_name=error_name, error_text=error_text), 408


if __name__ == "__main__":
    app.run(debug=True)
