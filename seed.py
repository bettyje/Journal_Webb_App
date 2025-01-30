from app import app
from extensions import db
from models import User, JournalEntry


def seed_data():
    with app.app_context():
        # Create test users
        user1 = User(name="John Doe", email="john@example.com")
        user1.set_password("password123")

        user2 = User(name="Jane Doe", email="jane@example.com")
        user2.set_password("password123")

        user3 = User(name="mike jill", email="mike@example.com")
        user3.set_password("password123")

        # Create test journals
        journal1 = JournalEntry(
            title="First Entry", content="This is my first journal entry.", user_id=1)
        journal2 = JournalEntry(
            title="Second Entry", content="This is my second journal entry.", user_id=2)

        journal3 = JournalEntry(
            title="third Entry", content="This is my third journal entry.", user_id=3)

        db.session.add_all([user1, user2, user3, journal1, journal2, journal3])
        db.session.commit()


if __name__ == "__main__":
    seed_data()
