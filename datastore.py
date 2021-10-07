from generator import create_a_phone


class User:

    def __init__(self):
        self.phone = create_a_phone()
        self.token = None


class DataStore:

    def __init__(self):
        self.user = User()


