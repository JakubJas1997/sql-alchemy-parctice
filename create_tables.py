import datetime
from sqlalchemy import Column, Integer, String, create_engine, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:qwerty@localhost:3306/practice")

Session = sessionmaker(bind=engine)
Base = declarative_base(bind=engine)


class Workers(Base):
    __tablename__ = "workers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    salary = Column(Float, default=0, nullable=False)
    hire_date = Column(
        DateTime,
        default=datetime.datetime.now,
        nullable=False
    )

    def __repr__(self):
        return f"Worker id: {self.id}, name: {self.first_name}, salary: {self.salary}"


Base.metadata.create_all()








