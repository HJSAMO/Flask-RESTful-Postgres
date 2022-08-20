import os

from api import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host=os.getenv("WEB_HOST"), port=os.getenv("WEB_PORT"), debug=True)
