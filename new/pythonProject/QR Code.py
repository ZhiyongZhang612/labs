from flask import Flask, render_template, request
import segno
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form['data']

        qr = segno.make(data)

        qr_path = os.path.join('static', 'qr_code.png')
        qr.save(qr_path)

        return render_template('index.html', img_path=qr_path, user_data=data)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
