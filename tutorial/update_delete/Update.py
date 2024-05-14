from sqlalchemy import update

from tutorial.Insert.Insert import user_table

stmt = (
    update(user_table).where(user_table.c.name == 'patrick').
    values(fullname = 'Patrick the Star')
)

print(stmt)

stmt = (
    update(user_table).
    values(fullname="Username: " + user_table.c.name)
)

print(stmt)

