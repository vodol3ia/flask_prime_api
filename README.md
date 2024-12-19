# Flask Prime API

This is a minimal Flask API that computes the n-th prime number.

## Endpoints

- `GET /prime/<int:n>`: Returns the n-th prime number in JSON format.

## Requirements

- Python 3.x
- Flask

## Setup

```bash
git clone <repo_url>
cd flask_prime_api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```


# Security Headers and CORS:
 For extra security headers or cross-origin access, consider using Flask-CORS and Flask-Talisman.
## Frontend Styling Library: 
For a React UI under a strict Content Security Policy (CSP), I would prefer Chakra UI because it provides a good balance between flexibility and security, and it has built-in support for accessibility.