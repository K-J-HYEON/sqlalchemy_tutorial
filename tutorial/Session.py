from sqlalchemy import text
from sqlalchemy.orm import Session

from tutorial.Engine import engine

stmt = text("SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y").bindparams(y=6)

# Session 객체에 Engine 객체의 인스턴스를 넘겨 데이터베이스와 상호작용할 수 있는 인스턴스를 얻는다.
with Session(engine) as session:
    # Session.execute() 메서드로 쿼리 실행
    result = session.execute(
        text("UPDATE some_table SET y=:y SET y=:y WHERE x=:x"),
        [{"x": 9, "y":11}, {"x":13, "y": 15}]
    )
    session.commit()
    # for row in result:
    #     print(f"x: {row.x} y: {row.y}")