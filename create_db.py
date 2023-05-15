from sqlalchemy import create_engine

def main():

    engine = create_engine("mysql+pymysql://root:qwerty@localhost:3306/")

    sql_statements = [
        "CREATE SCHEMA IF NOT EXISTS practice;"
    ]

    with engine.connect() as conn:
        for sql in sql_statements:
            conn.execute(sql)


if __name__ == "__main__":
    main()