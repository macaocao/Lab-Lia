from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works')
def works():
    return render_template('work.html')

@app.route('/UpperCase', methods=['GET', 'POST'])
def Uppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/areaOfcircle', methods=['GET', 'POST'])
def areaOfcircle():
    result_area = None
    if request.method == 'POST':
        input_number = request.form.get('inputNumber',0)
        input_diameter = request.form.get('inputDiameter',0)

        try:
            input_number = float(input_number)
            input_diameter = float(input_diameter)
        except ValueError:
            # Handle invalid input (non-numeric input) here
            pass
        except TypeError:
            # Handle invalid input (non-numeric input) here
            pass

        if input_diameter > 0:
            result_area = (math.pi * (input_diameter ** 2)) /4
        elif input_number > 0:
            result_area = math.pi * (input_number ** 2)
        else:
            result_area = None

    return render_template('areaOfcircle.html', result=result_area)

@app.route('/areaOfTriangle', methods=['GET', 'POST'])
def areaOfTriangle():
    result_area = None
    if request.method == 'POST':
        input_Base = request.form.get('inputBase', '')
        input_Height = request.form.get('inputHeight','')
        result_area = (int(input_Height)*int(input_Base))/2
    return render_template('areaOfTriangle.html', result=(str(result_area)+" squared unit"))

# Initialize a global list to store contacts
contact_info = []

@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        input_Name = request.form.get('inputName', '')
        input_Number = request.form.get('inputNumber', '')
        input_Email = request.form.get('inputEmail','')
        result_contact = {"Name": input_Name,
                          "Number": input_Number,
                          "Email": input_Email}

        contact_info.append(result_contact)

    return render_template('contact.html', result=contact_info)

if __name__ == "__main__":
    app.run(debug=True)
