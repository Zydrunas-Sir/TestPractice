from DatabaseContextManager import DatabaseContextManager


def create_table_group():
    query = """CREATE TABLE `group`(
    `id` integer NOT NULL AUTO_INCREMENT,
    `grouping_id` integer,
    `expenditures` DECIMAL(50, 2),
    `description` varchar(255),
    PRIMARY KEY (id),
    FOREIGN KEY (grouping_id) REFERENCES grouping(id));"""
    with DatabaseContextManager() as db:
        cursor = db.cursor()
        cursor.execute(query)


def create_table_groupings():
    query = """CREATE TABLE `grouping`(
    `id` integer NOT NULL AUTO_INCREMENT,
    `group_id` integer,
    `user_id` integer,
    PRIMARY KEY (id),
    FOREIGN KEY (group_id) REFERENCES group(id),
    FOREIGN KEY (user_id) REFERENCES user(id));"""
    with DatabaseContextManager() as db:
        cursor = db.cursor()
        cursor.execute(query)


def create_group(grouping_id, expenditures, description):
    query = """INSERT INTO group
                (grouping_id, expenditures, description)
                    VALUES(%s, %s, %s)
    """
    parameters = [grouping_id, expenditures, description]
    with DatabaseContextManager() as db:
        cursor = db.cursor()
        cursor.execute(query, parameters)


def create_grouping(group_id, user_id):
    query = """INSERT INTO group
                (group_id, user_id)
                    VALUES(%s, %s)
    """
    parameters = [group_id, user_id]
    with DatabaseContextManager() as db:
        cursor = db.cursor()
        cursor.execute(query, parameters)


def get_group():
    query = """SELECT * FROM group"""
    with DatabaseContextManager() as db:
        cursor = db.cursor()
        cursor.execute(query)
        print(cursor.fetchall())


def get_grouping():
    query = """SELECT * FROM grouping"""
    with DatabaseContextManager() as db:
        cursor = db.cursor()
        cursor.execute(query)
        print(cursor.fetchall())


def delete_group(group_id):
    query = """DELETE FROM group
                WHERE id = ?"""
    parameters = [group_id]
    with DatabaseContextManager() as db:
        db.execute(query, parameters)


def delete_grouping(grouping_id):
    query = """DELETE FROM grouping
                WHERE id = ?"""
    parameters = [grouping_id]
    with DatabaseContextManager() as db:
        db.execute(query, parameters)


def get_user_group(user_id):
    query = """SELECT expenditures FROM group 
                JOIN grouping ON group.id = group_id
                JOIN user ON user_id = user.id
                WHERE user.id = ?"""
    parameters = [user_id]
    with DatabaseContextManager() as db:
        cursor = db.cursor()
        cursor.execute(query, parameters)
        print(cursor.fetchall())
