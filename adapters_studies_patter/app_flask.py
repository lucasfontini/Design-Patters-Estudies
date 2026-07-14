from flask import Flask, request

from adapters.flask_adapter import FlaskRequestAdapter

app = Flask(__name__)

@app.post("/users")
def users():

    req = FlaskRequestAdapter(request).to_dict()
    # to_dict it return`s regardless of adapter same output data
    print(req)

    return {
        "framework": "Flask",
        "request": req
    }

if __name__ == "__main__":
    app.run(debug=True)