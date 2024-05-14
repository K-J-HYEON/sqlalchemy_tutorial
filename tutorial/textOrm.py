from sqlalchemy import text, select
from tutorial.Engine import engine
from tutorial.select.ORM import user_table, User

stmt = (
    select(
        text("'some phrase'"), user_table.c.name
    ).order_by(user_table.c.name)
)

# with engine.connect() as conn:
#     print(conn.execute(stmt).all())

from sqlalchemy import literal_column
stmt = (
    select(
        literal_column("'some pharse'").label("p"), user_table.c.name
    ).order_by(user_table.c.name)
)

with engine.connect() as conn:
    for row in conn.execute(stmt):
        print(f"{row.p}, {row.name}")

print(select(user_table).order_by(user_table.c.name))
print(select(User).order_by(User.fullname.desc()))