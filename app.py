from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_cors import CORS
from datetime import timedelta
from dotenv import load_dotenv
import os
from extensions import db, migrate
from models import User, JournalEntry

load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "https://bettyjournal.netlify.app/"}})

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_journal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["JWT_SECRET_KEY"] = os.getenv(
    "JWT_SECRET_KEY", "your_default_jwt_secret_key")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=10)

db.init_app(app)
migrate.init_app(app, db)
jwt = JWTManager(app)


@app.route("/")
def home():
    return jsonify({"message": "Welcome to the My Journal API!"}), 200


@app.route("/user/sign-up", methods=["POST"])
def user_signup():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    age = data.get('age')
    gender = data.get('gender')

    if not name or not email or not password:
        return jsonify({"message": "All fields are required."}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"message": "Email is already registered."}), 400

    new_user = User(name=name, email=email, age=age, gender=gender)
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User sign-up successful."}), 201


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    user = User.query.filter_by(email=email).first()

    if not user or not user.check_password(password):
        return jsonify({"error": "Invalid email or password"}), 400

    access_token = create_access_token(
        identity={"id": user.id, "email": user.email})
    return jsonify({"access_token": access_token, "user": {"id": user.id, "email": user.email}}), 200


@app.route("/journal", methods=["POST"])
@jwt_required()
def create_journal_entry():
    current_user = get_jwt_identity()
    data = request.get_json()

    title = data.get('title')
    content = data.get('content')

    if not title or not content:
        return jsonify({"message": "Title and content are required."}), 400

    new_journal = JournalEntry(
        title=title.strip(), content=content.strip(), user_id=current_user['id'])
    db.session.add(new_journal)
    db.session.commit()

    return jsonify({"message": "Journal entry created successfully."}), 201


@app.route("/journal", methods=["GET"])
@jwt_required()
def get_journals():
    current_user = get_jwt_identity()
    journals = JournalEntry.query.filter_by(user_id=current_user['id']).all()
    return jsonify([{
        "id": journal.id,
        "title": journal.title,
        "content": journal.content,
        "created_at": journal.created_at,
        "updated_at": journal.updated_at
    } for journal in journals]), 200


@app.route("/journal/<int:id>", methods=["PUT", "DELETE"])
@jwt_required()
def manage_journal_entry(id):
    current_user = get_jwt_identity()
    journal = JournalEntry.query.filter_by(
        id=id, user_id=current_user['id']).first()

    if not journal:
        return jsonify({"message": "Journal entry not found."}), 404

    if request.method == "PUT":
        data = request.get_json()
        journal.title = data.get('title', journal.title)
        journal.content = data.get('content', journal.content)
        db.session.commit()
        return jsonify({"message": "Journal entry updated successfully."}), 200

    elif request.method == "DELETE":
        db.session.delete(journal)
        db.session.commit()
        return jsonify({"message": "Journal entry deleted successfully."}), 200


@app.route("/journal/calendar", methods=["GET"])
@jwt_required()
def get_calendar_entries():
    current_user = get_jwt_identity()
    journals = JournalEntry.query.filter_by(user_id=current_user['id']).all()

    calendar_entries = [
        {
            "date": journal.created_at.strftime("%Y-%m-%d"),
            "title": journal.title,
            "content": journal.content,
        }
        for journal in journals
    ]

    return jsonify(calendar_entries), 200


@app.route("/user/theme", methods=["PUT"])
@jwt_required()
def toggle_theme():
    current_user = get_jwt_identity()
    user = User.query.get(current_user['id'])

    if not user:
        return jsonify({"message": "User not found."}), 404

    user.theme = "dark" if user.theme == "light" else "light"
    db.session.commit()

    return jsonify({"message": f"Theme updated to {user.theme}."}), 200


if __name__ == '__main__':
    app.run(debug=True)
