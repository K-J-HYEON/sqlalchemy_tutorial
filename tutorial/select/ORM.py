import where
import importlib
from sqlalchemy import Column, Integer, String, ForeignKey, Table, select
from sqlalchemy.orm import relationship
from sqlalchemy.sql.elements import and_
from sqlalchemy.sql.functions import user
from sqlalchemy import MetaData
from tutorial.Engine import engine
from tutorial.Registry import Base, mapper_registry
from sqlalchemy import func
from sqlalchemy import ForeignKey
from importlib.metadata import version
import importlib.metadata as importlib_metadata

metadata = MetaData()

user_table = Table(
    'user_account', # 데이터베이스에 저장될 table 이름입니다.
    metadata,
    Column('id', Integer, primary_key=True), # 이 테이블에 들어갈 컬럼
    Column('name', String(30)),
    Column('fullname', String)
)

# some_table = Table("some_table", metadata, autoload_with=engine)

# print(select(func.count('*')).select_func(user_table))

class User(Base):
    # 데이터베이스에서 사용할 테이블 이름입니다.
    __tablename__ = 'user_account'

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String)

    address = relationship("Address", back_populates="user")

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r}"


address_table = Table(
    "address",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', ForeignKey('user_account.id'), nullable=False), # ForeignKey 객체로 외래 키를 선언합니다.
    Column('email_address', String, nullable=False)
)


class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('user_account.id'))

    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"

# sandy = User(name = "sandy", fullname = "Sandy Cheeks")
# sandy
#
mapper_registry.metadata.create_all(engine)
Base.metadata.create_all(engine)

# print(user_table.c.name == 'squidward')

# print(address_table.c.user_id > 10)

# print(select(user_table).where(user_table.c.name == 'squidward'))

# print(
#     select(address_table.c.email_address),
#     where(user_table.c.name == 'squidward'),
#     where(address_table.c.user_id == user.table.c.id)
# )

# print(
#     select(address_table.c.email_address),
#         where(
#                 and_(
#                 user_table.c.name == 'squidward'
#         # Address_table.c.user_id == User.id
#             )
#         )
# )

# print(select(user_table.c.name))
# print(select(user_table.c.name, address_table.c.email_address))

print(
    select(user_table.c.name, address_table.c.email_address).
    join_from(user_table, address_table)
)

# print(
#     select(address_table.c.table.c.email_address).
#     select_from(user_table).
#     join(address_table, user_table.c.id == address_table.c.user_id)
# )

print(select(user_table).order_by(user_table.c.name))

print(select(User).order_by(User.fullname.desc()))

