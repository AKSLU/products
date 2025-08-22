from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'

    code = Column(String, primary_key=True)
    name = Column(String)
    producer = Column(String)

    def __repr__(self):
        return f"Продукт: {self.name}, Штрих-код: {self.code}, Производитель: {self.producer}"

connect = create_engine('sqlite:///exemple.db', echo=False)
Base.metadata.create_all(connect)

Session = sessionmaker(bind=connect)
session = Session()

p1 = Product(code="1234", name="Milk", producer="producer Milk")
p2 = Product(code="2345", name="Pizza", producer="producer Pizza")
p3 = Product(code="3456", name="Water", producer="producer Water")

session.add(p1)
session.add(p2)
session.add(p3)
session.commit()
all_products = session.query(Product).all()

for i in all_products:
    print(i)

