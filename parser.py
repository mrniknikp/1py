def parse_all(path):
    file = open(path, "r")
    data = file.read()
    
    
parse_all("data/users")


"""

TODO: Парсим файлы.
1. Файл для User_model
структура: 
    |
    |-ID
    |
    |-Name
    | 
    |-Link to file parsed for Players
    |
    |-Link to file
    |
    |-Link to alliance


Файл для Players
структура:
    |
    |-ID
    |
    |-HP
    |
    |-Armor
    |
    |-Attack
    |
    |-Link to User

"""

