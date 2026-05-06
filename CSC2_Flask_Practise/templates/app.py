from operator import index

from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'your_secret_key'

if __name__ == '__main__':
    app.run(debug=True)

    @app.route('/')
    def index():
        return render_template('index.html')