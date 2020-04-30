from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'


@app.route('/', methods=['POST', 'GET'])
def index():
    return redirect("/calories")


def calculate_bmr(gender, weight, height, age, body_type):
    if gender == 'female':
        return round((weight * 9.99) + (height * 6.25) - (age * 4.92) + body_type - 161)
    if gender == 'male':
        return round((weight * 9.99) + (height * 6.25) - (age * 4.92) + body_type + 5)


def calulate_strength_training(intensity, frequency, duration):
    return round(intensity * frequency * duration)


@app.route('/calories', methods=['GET', 'POST'])
def calories():
    if request.method == 'POST':
        # - Person's details ------------------------------------------
        gender = (request.form['gender'])
        age = int(request.form['age'])
        height = int(request.form['height'])
        weight = int(request.form['weight'])
        body_type = int(request.form['body_type'])
        bmr = calculate_bmr(gender, weight, height, age, body_type)

        # - Strength training details ----------------------------------
        intensity = int(request.form['intensity'])
        frequency = int(request.form['frequency'])
        duration = int(request.form['duration'])
        training = calulate_strength_training(intensity, frequency, duration)

        # - Render the results page -----------------------------------
        html = render_template('results.html',
                               age=age,
                               body_type=body_type,
                               duration=duration,
                               frequency=frequency,
                               gender=gender,
                               height=height,
                               bmr=bmr,
                               intensity=intensity,
                               training=training,
                               weight=weight
                               )

        return html
    else:
        return render_template('calories.html')


if __name__ == "__main__":
    app.run(debug=True)
