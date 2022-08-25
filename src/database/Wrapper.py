from Database import Database

class Wrapper(Database):
    def add_user_if_missing(
        self,
        telegram_user_id: int,
        username: str,
        first_name: str,
        last_name: str
    ):
        self.execute(
            'INSERT INTO users (telegram_id, first_name, last_name, username) VALUES (%s, %s, %s, %s)',
            [
                telegram_user_id,
                username,
                first_name,
                last_name
            ]
        )
        self.connection.commit()
        