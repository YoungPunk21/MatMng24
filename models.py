from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Material(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Первичный ключ
    name = db.Column(db.String(255), nullable=False)  # Наименование материала
    type = db.Column(db.String(100), nullable=False)  # Тип материала
    quantity = db.Column(db.Integer, nullable=False)  # Количество
    min_quantity = db.Column(db.Integer, nullable=False)  # Минимальное количество
    price = db.Column(db.Float, nullable=False)  # Цена

class Partner(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Первичный ключ
    name = db.Column(db.String(255), nullable=False)  # Имя партнера
    contact_info = db.Column(db.String(255), nullable=False)  # Контактная информация