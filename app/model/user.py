class User:
    def __init__(self, 
        email: str,
        password: str,
        first_name: str,
        last_name: str,
        uuid: str | None = None,
        session_uuid: str | None = None,
        is_verified: bool = False,
        is_active: bool = True,
    ):
        self.uuid = uuid
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.session_uuid = session_uuid
        self.is_verified = is_verified
        self.is_active = is_active

'''
    def save(self, db: Database):
        db.insert(
            "INSERT INTO User (uuid, first_name, last_name, email, password, is_verified, is_active, session_uuid) VALUES (%s, %s, %s, %s, %s, %s);",
            (self.uuid, self.first_name, self.last_name, self.email, self.password, self.is_verified, self.is_active, self.session_uuid)
        )

    def set_password(self, password: str):
        assert isinstance(password, int)
        self.password = 


    def verify(self, db: Database):
        db.insert("UPDATE User SET is_verified=%s WHERE uuid=%s;", (True, self.uuid))

    def refresh_session(self):
        self.session_uuid = uuid4()
'''