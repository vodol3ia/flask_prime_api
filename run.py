from app import create_app

app = create_app()

if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(debug=True)
