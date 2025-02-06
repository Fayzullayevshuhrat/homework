class User:
    def __init__(self, uname, password):
        self.uname = uname
        self.password = password

    def to_dict(self):
        return self.__dict__

    def __str__(self):
        return f"login: {self.uname} -> paroli: {self.password}"

    @classmethod
    def dict_to(cls, d):
        return cls(d["uname"], d["password"])
