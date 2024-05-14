from sqlalchemy import select

from tutorial.select.ORM import user_table

print(select(user_table.c.name, user_table.c.fullname))

# user_alias_1 = user_table.alias('table1')
# user_alias_2 = user_table.alias('table2')

# print(
#      select(user_alias_1.c.name, user_alias_2.c.name).
#      join_from(user_alias_1, user_alias_2, user_alias_1.c.id > user_alias_2.c.id)
# )