from create_tables import Workers, Session
import random

def main():

    session = Session()
    workers = session.query(Workers).all()

    to_delete = random.choice(workers)
    print(to_delete)
    session.delete(to_delete)
    session.commit()

    result = session.query(Workers).get(to_delete.id)
    assert result is None, "Worker wasn't deleted."


if __name__ == "__main__":
    main()