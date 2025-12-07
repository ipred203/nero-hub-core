from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes import bp
    app.register_blueprint(bp)

    # Можно загрузить конфиг
    from config import Config
    app.config.from_object(Config)

    return app
