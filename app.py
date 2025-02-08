from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # This enables CORS for all routes

def is_armstrong(n):
    """
    Check if n is an Armstrong number.
    An Armstrong number is equal to the sum of its digits each raised to the power of the number of digits.
    """
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return n == sum(d ** power for d in digits)

def is_prime(n):
    """
    Simple prime check: Returns False for numbers less than 2 and checks divisibility for others.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    """
    Check if n is a perfect number.
    A perfect number equals the sum of its proper divisors.
    """
    if n < 2:
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

def digit_sum(n):
    """
    Return the sum of the digits of n.
    """
    return sum(int(d) for d in str(abs(n)))  # abs() handles negative numbers

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number_str = request.args.get('number', None)
    if number_str is None:
        return jsonify({"error": True, "message": "Missing 'number' parameter"}), 400

    # Validate input: must be an integer
    try:
        number = int(number_str)
    except ValueError:
        return jsonify({"number": number_str, "error": True}), 400

    # Calculate mathematical properties
    armstrong = is_armstrong(number)
    prime = is_prime(number)
    perfect = is_perfect(number)
    sum_digits = digit_sum(number)
    parity = "odd" if number % 2 != 0 else "even"

    # Determine the 'properties' field based on Armstrong and parity:
    # - If Armstrong, include "armstrong" along with "odd" or "even"
    # - Otherwise, include just the parity.
    if armstrong:
        properties = ["armstrong", parity]
    else:
        properties = [parity]

    # Retrieve a fun fact from the Numbers API (using the 'math' type)
    try:
        api_url = f'http://numbersapi.com/{number}/math?json'
        response = requests.get(api_url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            fun_fact = data.get('text', f'No fun fact available for {number}.')
        else:
            fun_fact = f'No fun fact available for {number}.'
    except Exception:
        fun_fact = f'No fun fact available for {number}.'

    # Build the JSON response
    return jsonify({
        "number": number,
        "is_prime": prime,
        "is_perfect": perfect,
        "properties": properties,
        "digit_sum": sum_digits,
        "fun_fact": fun_fact
    }), 200

if __name__ == '__main__':
    # For production, use a WSGI server (e.g., gunicorn) instead of the Flask built-in server.
    app.run(host='0.0.0.0', port=5000, debug=False)
