from create_tables import Session, Workers
from faker import Faker

def create_workers(count=50):
    fake = Faker()
    return [
        Workers(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            salary=fake.pyfloat(
                min_value=5000,
                max_value=10000
            )
        )
        for _ in range(count)
    ]

def main():
    session = Session()
    workers = create_workers()
    session.add_all(workers)

    session.commit()



if __name__ == "__main__":
    main()