"""
A Sample Web-DB Application for DB-DESIGN lecture
Copyright (C) 2022 Yasuhiro Hayashi
"""
from psycopg2 import sql, connect, ProgrammingError
import flaskdb.var as v
from flaskdb.models import Item

class DataAccess:

    # Constractor called when this class is used. 
    # It is set for hostname, port, dbname, useranme and password as parameters.
    def __init__(self, hostname, port, dbname, username, password):
        self.dburl = "host=" + hostname + " port=" + str(port) + \
                     " dbname=" + dbname + " user=" + username + \
                     " password=" + password

    # This method is used to actually issue query sql to database. 
    def execute(self, query, autocommit=True):
        with connect(self.dburl) as conn:
            if v.SHOW_SQL:
                print(query.as_string(conn))
            conn.autocommit = autocommit #自動で接続
            with conn.cursor() as cur: #カーソルを取得
                cur.execute(query) #SQLコマンドを実行
                if not autocommit: 
                    conn.commit() #実行結果を反映 ただし、autocommit=Trueの場合必要ない
                try:
                    return cur.fetchall() #実行結果を配列として取得する
                except ProgrammingError as e:
                    return None

    # For mainly debug, This method is used to show sql to be issued to database. 
    def show_sql(self, query):
        with connect(self.dburl) as conn:
            print(query.as_string(conn))

    # search item data
    def search_tasks(self): #DBの中身を表示
        query = sql.SQL("""
            SELECT * FROM \"tasks\" 
        """)
        # self.show_sql(query)
        results = self.execute(query, autocommit=True)
        item_list = [] 
        for r in results:
            item = Item()
            item.id = r[0]
            #item.user_id = r[1]
            item.category = r[1]
            item.task = r[2]
            item.role = r[3]
            item.start_date = r[4]
            item.final_date = r[5]
            item_list.append(item)
        return item_list

    # search item data by category
    def search_tasks_by_category(self, category):
        query = sql.SQL("""
            SELECT * FROM \"tasks\" WHERE category LIKE {category}
        """).format(
            category = sql.Literal(category) 
        ) #where = 条件
        # self.show_sql(query)
        results = self.execute(query, autocommit=True)
        item_list = []
        for r in results:
            item = Item()
            item.id = r[0]
            #item.user_id = r[1]
            item.category = r[1]
            item.task = r[2]
            item.role = r[3]
            item.start_date = r[4]
            item.final_date = r[5]
            item_list.append(item)
        return item_list

    def add_item(self, item): #DBに追加
        query = sql.SQL("""
            INSERT INTO \"tasks\" ( {fields} ) VALUES ( {values} )
        """).format(
            tablename = sql.Identifier("tasks"),
            fields = sql.SQL(", ").join([
                sql.Identifier("category"),
                sql.Identifier("task"),
                sql.Identifier("role"),
                sql.Identifier("start_date"),
                sql.Identifier("final_date")
            ]),
            values = sql.SQL(", ").join([
                sql.Literal(item.category),
                sql.Literal(item.task),
                sql.Literal(item.role),
                sql.Literal(item.start_date),
                sql.Literal(item.final_date)
            ])
        )
        self.execute(query, autocommit=True)
