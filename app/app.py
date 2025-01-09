from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate_square_area():
    if request.method == 'POST':
        try:
            side_length = float(request.form['side_length'])
            area = side_length ** 2
            return render_template('result.html', side_length=side_length, area=area)
        except ValueError:
            return render_template('index.html', error="Proszę podać poprawną liczbę.")
    
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)