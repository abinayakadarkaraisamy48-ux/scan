from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/scan", methods=["POST"])
def scan():
    if "dress" not in request.files:
        return "No file part"

    file = request.files["dress"]

    if file.filename == "":
        return "No file selected"

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    # Temporary fixed color (same as your current project)
    color = "red"

    accessories_path = os.path.join("static", "accessories", color)
    accessories = os.listdir(accessories_path)

    return render_template(
        "result.html",
        dress_image=filepath,
        accessories=accessories,
        color=color
    )

if __name__ == "__main__":
    app.run(debug=True)