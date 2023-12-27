import sqlite3
import time
from os.path import exists
import utils
import models
db = "db.sqlite"
while not exists(db):
    print(db, "-- > doesnot exists")
    time.sleep(1)

connection = sqlite3.connect("db.sqlite")
cursor = connection.cursor()

def commit(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        connection.commit()
        return result
    return wrapper




create_user_table_sql = """
    create table if not exists users(
        id integer primary key autoincrement,
        username varchar(40) unique not null,
        password varchar(60) not null,
        status varchar(20) not null,
        role varchar(20) not null,
        login_try_count int default 0
    )
"""
create_todo_sql ="""
    create table if not exists todos(
        id integer primary key autoincrement,
        name varchar(30) not null,
        type varchar(20) not null,
        completed bool default false,
        user_id int references users(id)
)
"""
@commit
def init():
    cursor.execute(create_user_table_sql)
    cursor.execute(create_todo_sql)

inser_into_sql = """
    insert into users(username, password, status, role) values (?,?,?,?)
"""
@commit
def create_admin():
    cursor.execute(inser_into_sql, ("john",
                                    utils.encode_passrord("123"),
                                    models.UserStatus.ACTIVE.value,
                                    models.UserRole.ADMIN.value
                                    ))


def increase_user_try_count(username):
    increase_try_count_sql = """update users set login_try_count=login_try_count+1 where username=? """
    cursor.execute(increase_try_count_sql, (username,))
def get_user_by_username(username:str):
    get_user_sql = "select id, username, password, status, role, login_try_count from users where username=?"
    cursor.execute(get_user_sql, (username, ))
    user_data = cursor.fetchone()
    return user_data
# if __name__ == '__main__':
    # init()
    # create_admin()
    # print(get_user_by_username("john"))