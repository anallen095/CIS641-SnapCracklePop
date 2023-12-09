from flask import Flask
from snap_flask.routes import app

if __name__ == '__main__':
    app.run(debug=True)
