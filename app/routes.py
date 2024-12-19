from flask import Blueprint, jsonify, abort
from .utils import find_nth_prime

bp = Blueprint('api', __name__)

@bp.route('/prime/<int:n>', methods=['GET'])
def get_nth_prime(n):
    if n < 1:
        return jsonify({"error": "n must be greater than or equal to 1"}), 400
    nth_prime = find_nth_prime(n)
    return jsonify({"n": n, "nth_prime": nth_prime})
