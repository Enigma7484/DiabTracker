from flask import Flask
import subprocess
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def run_other_file():
    try:
        result = subprocess.run(["python", "DiabTracker.py"], capture_output=True, text=True)
        output = result.stdout
        error_output = result.stderr
        response_text = f"<pre>{output}</pre>"
        return response_text
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)