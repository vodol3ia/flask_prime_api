from flask import Blueprint, jsonify, abort, request

bp = Blueprint('api', __name__)

MAX_N = 10000  # Limit for n

def find_nth_prime(n):
    """Finds the n-th prime number using a basic algorithm."""
    primes = []
    candidate = 2

    while len(primes) < n:
        is_prime = all(candidate % p != 0 for p in primes)
        if is_prime:
            primes.append(candidate)
        candidate += 1

    return primes[-1]

def validate_n(n):
    """
    Validates the input parameter 'n' and returns either the integer value
    or an error response with a status code.
    """
    if not n.isdigit():
        return None, jsonify({"error": "Invalid input. 'n' must be a positive integer."}), 400

    n = int(n)

    if n < 1:
        return None, jsonify({"error": "Invalid input. 'n' must be greater than or equal to 1."}), 400

    if n > MAX_N:
        return None, jsonify({"error": f"'n' exceeds the maximum allowed value of {MAX_N}."}), 400

    return n, None, None

@bp.route('/prime/<n>', methods=['GET'])
def get_nth_prime(n=None):
    """
    Handles GET requests to calculate the n-th prime number.

    :param n: Input as part of the URL, representing the n-th prime number to calculate.
    :return: JSON response containing either the calculated prime or an error message.
    """
    if n is None:
        return jsonify({"error": "Invalid input. 'n' must be provided."}), 404

    # Validate the input parameter
    n, error_response, status_code = validate_n(n)
    if error_response:
        return error_response, status_code

    # Calculate the n-th prime
    try:
        nth_prime = find_nth_prime(n)
        return jsonify({"n": n, "nth_prime": nth_prime})
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@bp.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

@bp.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "An unexpected error occurred.", "details": str(error)}), 500