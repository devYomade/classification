from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

def is_armstrong(n: int) -> bool:
    """Check if the absolute value of n is an Armstrong number."""
    digits = [int(d) for d in str(abs(n))]
    power = len(digits)
    return abs(n) == sum(d ** power for d in digits)

def is_prime(n: int) -> bool:
    """Determine if n (using its integer part) is a prime number.
       Negative numbers and 0,1 are not considered prime.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    """Check if n is a perfect number.
       Only positive integers can be perfect numbers.
    """
    if n <= 0:
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

def digit_sum(n: int) -> int:
    """Return the sum of the digits of n (using its absolute value)."""
    return sum(int(d) for d in str(abs(n)) if d.isdigit())

def get_fun_fact(n: int) -> str:
    """Fetch a fun fact about the number using the Numbers API."""
    try:
        url = f"http://numbersapi.com/{n}/math?json"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data.get("text", f"No fun fact available for {n}.")
        else:
            return f"No fun fact available for {n}."
    except Exception:
        return f"No fun fact available for {n}."

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    # Retrieve the 'number' parameter from the query string
    number_str = request.args.get("number", None)
    if number_str is None:
        return jsonify({"error": True, "message": "Missing 'number' parameter"}), 400

    try:
        # Accept the input as a float (this covers integers, negatives, and floating-point numbers)
        num = float(number_str)
    except ValueError:
        return jsonify({"error": True, "number": number_str}), 400

    # For property calculations, use the integer part of the number
    n_int = int(num)

    prime_flag = is_prime(n_int)
    perfect_flag = is_perfect(n_int)
    armstrong_flag = is_armstrong(n_int)

    # Determine parity using the integer part
    parity = "even" if n_int % 2 == 0 else "odd"
    # Build the properties list based on whether it's Armstrong and its parity
    properties = []
    if armstrong_flag:
        properties.append("armstrong")
    properties.append(parity)

    result = {
        "number": num,
        "is_prime": prime_flag,
        "is_perfect": perfect_flag,
        "properties": properties,
        "digit_sum": digit_sum(n_int),
        "fun_fact": get_fun_fact(n_int)
    }

    # Return a valid JSON response
    return jsonify(result), 200

if __name__ == '__main__':
    # Run the app on all interfaces so that it is accessible externally
    app.run(host="0.0.0.0", port=5000)
