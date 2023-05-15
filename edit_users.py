from create_tables import Session, Workers
import random


def main():
    session = Session()
    workers = session.query(Workers).all()

    worker = random.choice(workers)
    print(f"The chosen worker is {worker}")
    print(f"His/Her salay is {worker.salary}")
    old_salary = worker.salary
    worker.salary *= 1.5

    session.add(worker)
    session.commit()

    check = session.query(Workers).get(worker.id)
    assert check.salary > old_salary, "Salary was not correct"


if __name__ == "__main__":
    main()