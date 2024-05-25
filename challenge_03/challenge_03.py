def load_text(input:str)->str:
    '''
    Lee el archivo con las palabras
    y devuelve una string con el contenido
    '''
    with open (input, "r", encoding='utf-8') as f:
        text = f.read()

        return text
    

def token_str(input):

    n_list = [ ]
    for element in input.split('\n'):
        token = element.replace("-", " ").replace(":", "")
        final_token = token.split(" ")

        n_list.append(final_token)

    return n_list

    
def codify(code):
    invalid = []
    for part in code:
        count = 0
        min = int(part[0])
        max = int(part[1])
        for letter in part[3]:
            if letter == part[2]:
                count += 1
        if count > max or count < min:
            invalid.append(part[3])

    return invalid[41]





if __name__ == "__main__":

    file_path = "input_03.txt"

    token_str(load_text(file_path))

    print(codify(token_str(load_text(file_path))))
