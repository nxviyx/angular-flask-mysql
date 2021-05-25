# from flask import Flask,render_template, request, jsonify
# from flask_compress import Compress

# # initialize flask application
# app = Flask(__name__,static_url_path='',static_folder='dist',template_folder='dist')
# Compress(app)


# @app.route('/')
# def test():
#     return render_template("index.html")


# if __name__ == '__main__':
#     # run web server
#     app.run()


from flask import Flask

app = Flask(__name__, static_url_path='', static_folder='dist')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/<path:path>')
def static_proxy(path):
    # send_static_file will guess the correct MIME type
    return app.send_static_file(path)