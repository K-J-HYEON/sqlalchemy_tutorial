from sqlalchemy import insert, select

from tutorial.Engine import engine
from tutorial.select.ORM import user_table, address_table

stmt = insert(user_table).values(name = 'sample1', fullname = 'sample11')

with engine.connect() as conn:
    result = conn.execute(
        insert(user_table),
        [
            {"name" : "sandy", "fullname": "Sandy Cheeks"},
            {"name" : "patrick", "fullname": "Patrick Star"}
        ]
    )

    conn.commit()

select_stmt = select(user_table.c.id, user_table.c.name + "@aol.com")
insert_stmt = insert(address_table).from_select(
    ["user_id", "email_address"], select_stmt
)
print(insert_stmt)

insert_stmt = insert(address_table).returning(address_table.c.id, address_table.c.email_address)
print(insert_stmt)