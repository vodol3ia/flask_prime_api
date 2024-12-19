from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes import bp
    app.register_blueprint(bp)

    # Global error handler
    @app.errorhandler(Exception)
    def handle_exception(e):
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

    return app
