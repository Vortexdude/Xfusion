import os

class dir:
    def __init__(self):
        self.pwd = os.getcwd()

    @property
    def output(self):
        dir = f"{self.pwd}/output"
        os.makedirs(f"{self.pwd}/output", exist_ok=True)
        return dir

    @property
    def proccesed(self):
        dir = f"{self.pwd}/proccessed"
        os.makedirs(f"{self.pwd}/proccessed", exist_ok=True)
        return dir