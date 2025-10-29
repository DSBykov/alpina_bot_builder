from dotenv import dotenv_values

class Credentials:
    def __init__(self):
        storage = dotenv_values(".env")
        for key, value in storage.items():
            setattr(self, key, value)

credentials = Credentials()