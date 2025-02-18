import os

# App configurations
SQLALCHEMY_DATABASE_URI = 'sqlite:///C:/Users/Lenovo/HotelProject/instance/database.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.environ.get('SECRET_KEY', 'Jaskirat')

