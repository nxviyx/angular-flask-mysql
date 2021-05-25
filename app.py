from flask import Flask,render_template, request, jsonify
from flask_compress import Compress

# initialize flask application
app = Flask(__name__,static_url_path='',static_folder='dist',template_folder='dist')
Compress(app)


@app.route('/')
def test():
    return render_template("index.html")


if __name__ == '__main__':
    # run web server
    app.run()