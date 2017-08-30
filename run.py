"""
Commands to start the flask server
"""
from app import app

if __name__ == '__main__':
    app.run('', port=5000)
