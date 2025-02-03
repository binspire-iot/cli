import psycopg2


class Database:
    def __init__(self, connection_string) -> None:
        self.connection_string = connection_string
        self.connection = None
        self.cursor = None

    def connect(self):
        if self.connection_string is None:
            print("Connection string is not set")
            return

        try:
            self.connection = psycopg2.connect(self.connection_string)
            self.cursor = self.connection.cursor()
            print("Successfully connected to the database")
        except Exception as e:
            print(f"Failed to connect to the database: {e}")

    def disconnect(self):
        try:
            if self.cursor and self.connection:
                self.cursor.close()
                self.connection.close()
                print("Database connnection closed")
        except Exception as e:
            print(f"Failed to close database connection: {e}")

    def query(self, query, params=None):
        if not self.cursor or not self.cursor:
            print("No active database connection")
            return

        try:
            self.cursor.execute(query, params)
            if self.connection:
                self.connection.commit()
        except Exception as e:
            print(f"Failed to execute query: ${e}")
            if self.connection:
                self.connection.rollback()
