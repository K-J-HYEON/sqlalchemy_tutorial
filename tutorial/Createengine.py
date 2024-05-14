from sqlalchemy import text
# from CreateConnection import engine

with engine.connect() as conn:
     # 테이블을 생성합니다.
     conn.execute(text("CREATE TABLE some_table (x int, y int)"))
     # 데이터를 삽입합니다.
     conn.execute(
         text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
         [{"x": 1, "y": 1}, {"x": 2, "y": 4}]
     )
     # 위 변경사항을 커밋합니다.
     conn.commit()

