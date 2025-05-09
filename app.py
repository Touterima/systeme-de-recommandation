from flask import Flask, jsonify, render_template
from reco import get_recommendations

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")



@app.route('/api/recommendations/<string:student_name>', methods=['GET'])
def recommendations(student_name):
    data = get_recommendations(student_name)
    if "error" in data:
        return render_template("recommendations.html", student_name=student_name, offres=None)
    return render_template("recommendations.html", student_name=student_name, offres=data)

if __name__ == '__main__':
    app.run(debug=True)
