from app.telegram.client import app

with app:
    me = app.get_me()
    print(f"Connected as: {me.first_name}")