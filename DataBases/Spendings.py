from DataBases.DatabaseContextManager import DatabaseContextManager


def create_table_spending():
    query = """CREATE TABLE `spending`(
    `id` integer NOT NULL AUTO_INCREMENT,
    `user_id` integer,
    `category` varchar(255),
    `monthly_expenditures` DECIMAL(50, 2),
    `yearly_expenditures` DECIMAL(50, 2),
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES user(id));"""
    with DatabaseContextManager() as db:
        cursor = db.cursor()
        cursor.execute(query)


def create_spending(user_id, category, monthly_expenditures, yearly_expenditures):
    query = """INSERT INTO spending
                (user_id, category, monthly_expenditures, yearly_expenditures)
                    VALUES(%s, %s, %s, %s)
    """
    parameters = [user_id, category, monthly_expenditures, yearly_expenditures]
    with DatabaseContextManager() as db:
        cursor = db.cursor()
        cursor.execute(query, parameters)


def get_spending():
    query = """SELECT * FROM spending"""
    with DatabaseContextManager() as db:
        cursor = db.cursor()
        cursor.execute(query)
        print(cursor.fetchall())


def delete_spending(spending_id):
    query = """DELETE FROM spending
                WHERE id = ?"""
    parameters = [spending_id]
    with DatabaseContextManager() as db:
        db.execute(query, parameters)


def get_user_monthly_spending():
    query = """SELECT monthly_expenditures FROM spending
               JOIN user
                ON spending.user_id = user.id"""
    with DatabaseContextManager() as db:
        cursor = db.cursor()
        cursor.execute(query)
        print(cursor.fetchall())


def get_user_yearly_spending():
    query = """SELECT yearly_expenditures FROM spending
               JOIN user
                ON spending.user_id = user.id"""
    with DatabaseContextManager() as db:
        cursor = db.cursor()
        cursor.execute(query)
        print(cursor.fetchall())
