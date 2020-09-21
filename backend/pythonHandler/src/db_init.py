if __name__ == "__main__":
    # Initialize database object
    from src import db, create_app

    db.create_all(app=create_app())