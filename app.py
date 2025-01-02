from flask import Flask, request, render_template

app = Flask(__name__)

# Hardcoded credentials for testing
stored_username = "admin"
stored_password = "password123"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Check credentials
        if username == stored_username and password == stored_password:
            return "Login Successful!"
        else:
            return "Login Failed. Try Again."

    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)


