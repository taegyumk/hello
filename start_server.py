from flask import Flask, render_template

app = Flask(__name__)

@app.route("/recipe")
def email():
    return render_template('recipe.html')

@app.route("/checking")
def index():
    return render_template('sending.html')

if __name__ == "__main__":
    app.run()

