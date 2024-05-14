from sqlalchemy import text

from tutorial.Engine import engine

with engine.connect() as conn:
     # 테이블을 생성합니다.
     conn.execute(text("CREATE TABLE some_table (x int, y int)"))
     # 데이터를 삽입합니다.
     conn.execute(
         text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
         [{"x" : 11, "y" : 12}, {"x" : 13, "y": 14}]
     )

     result = conn.execute(text("SELECT x, y FROM some_table"))
     for row in result:
         print(f"x: {row.x} y: {row.y}")

     # 위 변경사항을 커밋합니다.
     conn.commit()