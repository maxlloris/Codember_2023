def load_text(input:str)->str:
    '''
    Lee el archivo con las palabras
    y devuelve una string con el contenido
    '''
    with open (input, "r", encoding='utf-8') as f:
        text = f.read()

        return text


def mini_compiler (input_data):
    '''
    Recibe una cadena con unos simbolos
    y lo decodifica en valores numericos siguiendo
    una serie de condiciones
    '''
    code = ""
    accum = 0
    for symbol in input_data:

        if symbol == "&" and len(code) == 0:
            code = "0"
        elif symbol == "#":
            accum = accum + 1
        elif symbol == "@":
            accum = accum - 1
        elif symbol == "*":
            accum = accum*accum
        else:
            accum = accum
            code = code + str(accum)
    
    return code



if __name__ == "__main__":

    file_path = "input_02.txt"

    games = load_text(file_path)

    print(mini_compiler(load_text(file_path)))