def load_text(input:str)->str:
    '''
    Lee el archivo con las palabras
    y devuelve una string con el contenido
    '''
    with open (input, "r", encoding='utf-8') as f:
        text = f.read()

        return text
    
def equal_strings (str1:str, str2:str)->bool:
    '''
    Compara si dos cadenas son iguales
    '''
    return str1 == str2
    

def token_str(input)->str:
    count = 0
    result = None
    
    for element in input.split('\n'):
        line = element.split('-')
        part = line[0]
        non_repeated_letters = ''

        for letter in part:
            if part.count(letter) == 1:
                non_repeated_letters += letter
            
        if equal_strings(non_repeated_letters, line[1]):
            count += 1

        if count == 33:
            result = line[1]

    return result
            
if __name__ == "__main__":

    file_path = "input_04.txt"

    print(token_str(load_text(file_path)))
