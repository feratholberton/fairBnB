from flask import Flask
from app.config import ini_app, db
from app.controllers.user_controller import user_bp

app = Flask(__name__)
ini_app(app)

app.register_blueprint(user_bp, url_prefix='/api')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)