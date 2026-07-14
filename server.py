from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/secret")
def autoriz():
    return render_template("main/secret.html")

@app.route("/post", methods=["POST"])
def post():
    data = request.get_json()
    print(data)
    user = data["user"]
    password = data["password"]
    if user == "admin" and password == "password":
        return jsonify({"is": "OK", "site": "secret/sobaka"}), 200
    else:
        return jsonify({"is": "NO", "site": "/secret"}), 200
    
@app.route("/secret/sobaka")
def hidden():
    return render_template("secret/sobaka.html")

if __name__ == '__main__':
    app.run(debug=True)
