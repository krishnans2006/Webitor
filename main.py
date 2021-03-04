from src import create_app

app = create_app()


if __name__ == '__main__':
    app.run(host="0.0.0.0")#where is the you dont have to put app.route check views.py in src it's cleaner and easier to have it like that