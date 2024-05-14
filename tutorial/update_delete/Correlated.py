from turtle import update

from sqlalchemy import select

from tutorial.select.ORM import address_table, user_table

scalar_subq = (
    select(address_table.c.email_address).
    where(address_table.c.user_id == user_table.c.id).
    order_by(address_table.c.id).
    limit(1).
    scalar_subquery()
)

update_stmt = update(user_table).values(fullname=scalar_subq)
print(update_stmt)