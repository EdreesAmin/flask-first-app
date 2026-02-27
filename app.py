from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "Hello, Flask!"

    @app.route("/api/health")
    def health():
        return jsonify(status="ok")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)