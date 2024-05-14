from sqlalchemy import select

from tutorial.Engine import engine
from tutorial.select.ORM import user_table
from tutorial.Registry import Base

Base.metadata
# Metadata()

stmt = (
    select(
        ("Username: " + user_table.c.name).label("username"),
    ).order_by(user_table.c.name)
)

with engine.connect() as conn:
    for row in conn.execute(stmt):
        print(f"{row.username}")