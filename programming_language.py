class ProgrammingLanguage:
    obj = 0
    """ Initial variable """
    def __init__(self, language, typing, reflection, year):
        self.language = language
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.obj += 1

    """ check whether is language dynamic """
    def is_dynamic(self):
        return self.typing == "Dynamic"

    """ print the value """
    def __str__(self):
        return "{self.language}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}".format(self=self)



