from sqlalchemy import insert, engine
from tutorial.select.ORM import user_table
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String

stmt = insert(user_table).values(name = 'sample1', fullname = 'sample1 squarepants')
print(stmt)

metadata = MetaData()
user_table = Table(
    'user_account',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(30)),
    Column('fullname', String),
)

compiled = stmt.compile()
print(compiled.params)


with engine.connect() as conn:
    result = conn.execute(stmt)
    conn.commit()

result.inserted_primary_key