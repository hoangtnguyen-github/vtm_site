from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/estimate')
def estimate():
    return render_template('estimate.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/TotalPrice', methods=['POST'])
def TotalPrice():
    if request.method == 'POST':
        form = request.form
        radius = float(form['radius'])
        height = float(form['height'])
        pi = 3.14
        areaOfTankTop = pi * (radius**2)
        areaOfTankSide = 2 * (pi*(radius*height))
        totalPrice = 35 * (areaOfTankSide + areaOfTankTop)
        formattedTotalPrice = "${:,.2f}".format(totalPrice)
        
        print(radius)
        print(height)
        print(areaOfTankTop)
        print(areaOfTankSide)
        print(totalPrice)

        return render_template('estimate.html', TotalPrice = formattedTotalPrice)
        
    return render_template('estimate.html')

if __name__  == '__main__':
    app.run(debug=True)