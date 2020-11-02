import os
from flask import Flask, render_template, request

app = Flask(__name__)


def dir_last_updated(folder='static/'):
    return str(max(os.path.getmtime(os.path.join(root_path, f)) for root_path, dirs, files in os.walk(folder) for f in files))


def calc_bmi(h, w, hu, wu):
    h, w = float(h), float(w)
    if (hu == "inches"):
        h *= 2.54
    if (wu == "lb"):
        w /= 2.20462
    b = w/((h/100)**2)
    if(b <= 18.5):
        s = 'Thin'
    elif(18.5 < b <= 25):
        s = "Healthy"
    elif(25 < b <= 30):
        s = "Overweight"
    elif(b > 30):
        s = "Obese"
    return round(b, 2), s


@app.route('/', methods=['GET', 'POST'])
def home():
    name = ""
    height = 0
    weight = 0
    bmi = 0
    hunit = ""
    wunit = ""
    status = ""
    if request.method == 'POST' and 'username' in request.form:
        name = request.form.get('username')
        height = request.form.get('height')
        weight = request.form.get('weight')
        hunit = request.form.get('heightunits')
        wunit = request.form.get('weightunits')
        bmi, status = calc_bmi(height, weight, hunit, wunit)
    return render_template('index.html', name=name, bmi=bmi, state=status, last_updated=dir_last_updated())


if __name__ == "__main__":
    app.run(debug=True)
