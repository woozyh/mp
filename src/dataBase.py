#!/usr/bin/python3.12.3

import sqlite3


class DataBase(object):

    def __init__(self,) -> None:
        """initializing the DataBase class."""

        try:
            self.db = sqlite3.connect("./playLists.db")
            self.cursor = self.db.cursor()

            self.cursor.execute("CREATE TABLE IF NOT EXISTS Global ( path TEXT PRIMARY KEY )")
            self.cursor.execute("CREATE TABLE IF NOT EXISTS Favorites (path TEXT PRIMARY KEY )")
            
        except sqlite3.Error as er:
            print(f"Error: error on connecting to playLists database, this will make issues. {er}")
            
    def executeQuery(self, query: list, info: dict = dict()) -> list:
        """query handler of DataBase class."""

        result: list = None
        
        try:
            match query:

                case ["Create"]:
                    self.cursor.execute(
                        f"CREATE TABLE IF NOT EXISTS '{info['TABLE']}' ( path TEXT PRIMARY KEY );"
                    )
                
                case ["Insert"]:
                    self.cursor.executemany(
                        f"INSERT OR IGNORE INTO '{info['TABLE']}' VALUES (?)",
                        info['VALUES'],
                    )
                    
                case ["Select", "song"]:
                    result = (
                        path[0] for path in self.cursor.execute(
                            f"SELECT path FROM '{info['TABLE']}'"
                        ).fetchall()
                    )

                case ["Select", "playList"]:
                    result = (
                        name[0] for name in self.cursor.execute(
                            "SELECT name FROM sqlite_master WHERE type='table'",
                        ).fetchall()
                    )
                case ["Delete", "song"]:
                    self.cursor.execute(
                        f"DELETE FROM '{info['TABLE']}' WHERE path='{info['PATH']}'"
                    )

                case ["Delete", "playList"]:
                    self.cursor.execute(
                        f"DROP TABLE '{info['TABLE']}'"
                    )
                    
                case _:
                    print(f"Unvalid query {query}.")

        except sqlite3.Error as er:
            print(f"Error: error on executing {query} query. {er}")

        self.db.commit()

        return result

