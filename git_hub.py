def print_words_numbers():
    """
    This function generates a list of numbers from 1 to 100, but for multiples of three, 
    it appends "git" instead of the number and for the multiples of five, it appends "hub". 
    For numbers which are multiples of both three and five, it appends "github".
    
    Returns:
        list: A list of strings representing the modified numbers from 1 to 100.
    """
    output = []
    for i in range(1, 101):
        result = ''
        if i % 3 == 0:
            result += "git"
        if i % 5 == 0:
            result += "hub"
        if not result:
            result += str(i)
        output.append(result)
    return output

new_list = print_words_numbers()
print(*new_list, sep='\n')

