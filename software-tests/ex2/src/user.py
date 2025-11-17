class User:

    def __init__(self, name: str, mail: str):
        self.name = name
        self.mail = mail

    def to_dict(self):
        return {"name": self.name, "mail": self.mail}

    def from_dict(data: dict):
        if data:
            return User(name=data.get('name'), mail=data.get('mail'))
        return None
