def load_text(input:str)->str:
    '''
    Lee el archivo con las palabras
    y devuelve una string con el contenido
    '''
    with open (input, "r", encoding='utf-8') as f:
        text = f.read()

        return text


def str_to_dict (input_string:str)->dict:
    '''
    Recibe una cadena lo transforma en lista
    y devuelve un diccionario donde podemos ver
    cuantas veces se repite cada palabra en el string original
    '''

    new_list = input_string.split(" ") # Convierto a lista
    animals = {}
    for animal in new_list:
        if animal not in animals:
            animals[animal] = 1
        else:
            animals[animal] += 1
        
    return animals


def dict_to_str(animals_dict: dict)->str:
    '''
    Recibe un dicionario y crea un string donde
    se concatena clave y valor del diccionario.
    '''

    result_animals= ""
    for key, value in animals_dict.items():
        result_animals += key + str(value)

    return result_animals



if __name__ == "__main__":

    file_path = "input.txt"

    load_text(file_path)

    result_1 = str_to_dict(load_text(file_path))

    print(dict_to_str (result_1))
