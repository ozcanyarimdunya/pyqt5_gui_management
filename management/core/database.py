import os
import sqlite3

from management.utils import get_root_dir


class ProjectsModel:

    def __init__(self):
        self.__connection = sqlite3.connect(os.path.join(get_root_dir(), 'database.db'))
        self.__cursor = self.__connection.cursor()

        self.__create_table__()

    def __del__(self):
        self.__connection.commit()
        self.__connection.close()

    def __create_table__(self):
        self.__cursor.execute(
            """CREATE TABLE IF NOT EXISTS PROJECTS(
            Id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Company TEXT, 
            CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, UpdatedAt TIMESTAMP)""")

    def get_projects(self):
        self.__cursor.execute(
            """SELECT * FROM PROJECTS""")

        headers = list(map(lambda x: x[0], self.__cursor.description))
        data = self.__cursor.fetchall()
        return headers, data

    def get_project(self, _id):
        self.__cursor.execute(
            """SELECT * FROM PROJECTS WHERE Id = ?""",
            (_id,)
        )

        data = self.__cursor.fetchone()
        return data

    def add_project(self, name, company):
        self.__cursor.execute(
            """INSERT INTO PROJECTS(Name, Company) VALUES (?,?)""",
            (name, company)
        )

        self.__connection.commit()

    def update_project(self, _id, name, company):
        self.__cursor.execute(
            """UPDATE PROJECTS SET Name = ?, UpdatedAt = CURRENT_TIMESTAMP, Company = ? WHERE Id = ?""",
            (name, company, _id)
        )

        self.__connection.commit()

    def delete_project(self, _id):
        self.__cursor.execute(
            """DELETE FROM PROJECTS WHERE Id = ?""",
            (_id,)
        )

        self.__connection.commit()
