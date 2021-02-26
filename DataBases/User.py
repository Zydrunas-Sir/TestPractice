from DatabaseContextManager import DatabaseContextManager


def create_table_user():
    query = """CREATE TABLE `user`(
    `id` integer NOT NULL AUTO_INCREMENT,
    `spending_id` integer,
    `grouping_id` integer,
    `name` varchar(255),
    `salary` DECIMAL(50, 2),
    `balance` DECIMAL(50, 2),
    PRIMARY KEY (id),
    FOREIGN KEY (spending_id) REFERENCES spending(id),
    FOREIGN KEY (grouping_id) REFERENCES grouping(id));"""
    with DatabaseContextManager() as db:
        cursor = db.cursor()
        cursor.execute(query)


def create_user(spending_id, grouping_id, name, salary, balance):
    query = """INSERT INTO user
                (spending_id, grouping_id, name,salary, balance)
                    VALUES(%s, %s, %s, %s, %s)
    """
    parameters = [spending_id, grouping_id, name, salary, balance]
    with DatabaseContextManager() as db:
        cursor = db.cursor()
        cursor.execute(query, parameters)


def get_user():
    query = """SELECT * FROM user"""
    with DatabaseContextManager() as db:
        cursor = db.cursor()
        cursor.execute(query)
        print(cursor.fetchall())


def delete_user(user_id):
    query = """DELETE FROM user
                WHERE id = ?"""
    parameters = [user_id]
    with DatabaseContextManager() as db:
        db.execute(query, parameters)



