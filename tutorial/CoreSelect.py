# https://soogoonsoogoonpythonists.github.io/sqlalchemy-for-pythonist/tutorial/1.%20%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC%20%EA%B0%9C%EC%9A%94.html#%E1%84%80%E1%85%A2%E1%84%8B%E1%85%AD

from sqlalchemy import select
from sqlalchemy.orm import Session
from tutorial.Engine import engine
from tutorial.select.ORM import User, user_table

stmt = select(user_table).where(user_table.c.name == 'sampleName')

print(stmt)

with engine.connect() as conn:
    for row in conn.execute(stmt):
        print(row)

# with Session(engine) as session:
#     for row in session.execute(stmt):
#         print(row)

with Session(engine) as session:
    row = session.execute(select(User.name.User.fullname)).first()
    print(row)

print(select(user_table.c.name, user_table.c.fullname))
print(select(User))
print(select(user_table))

stmt = select(User).where(User.name == 'sampleName')

with Session(engine) as session:
    for row in session.execute(stmt):
        print(row)

print(select(user_table).where(user_table.c.name == 'squidward'))