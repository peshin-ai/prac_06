from programming_language import ProgrammingLanguage

def main():
    """ create 3 object base on class ProgrammingLanguage """
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    """ create the array to store 3 object """
    array = [ruby, python, visual_basic]
    print("The dynamically typed languages are:")

    """ print value if the language is dynamic"""
    for item in array:
        if item.is_dynamic():
            print(item.language)

if __name__ == '__main__':
    main()