from io import StringIO

class StringBuilder:

    def __init__(self,str=""):
        self.str = StringIO()
        self.str.write(str)

    def append(self,str):
        self.str.write(str)
        return self

    def __str__(self):
        return self.str.getvalue()

    def to_string(self):
        return self.str.getvalue()
