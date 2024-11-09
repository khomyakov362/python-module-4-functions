import re
def get_reg_data():
    name_reg = re.compile(r'^[a-zA-Zа-яА-ЯёЁ]+$')
    number_reg = re.compile(r'^\+\d{1,3}\(\d{2}\)\d{7}$')
    email_reg = re.compile(r'^[a-zA-Z0-9]+@yandex\.ru$')
    return {
        'name' : name_reg,
        'sur-name' : name_reg,
        'surname' : number_reg,
        'e-mail' : email_reg
        }   

def reg_check(key, dictionary, data_list):
    def is_unique(data, data_list):
        return not (data in data_list)
    
    reg = dictionary[key]

    data = input(f'Please enter your {key}: ')
    if reg.match(data) and is_unique(data, data_list):
        print(f'The {key} is accepted.')
        return data
    else:
        print('''
Invalid input!
The data must be unique.
The name and surname must only contain letters of Russian or English alphabet.
The phone number must follow a pattern  +***(**)*******, where * is any digit.
The email must end with  @yandex.ru and cannot contain characters other than Latin letters or digits.''')
        return reg_check(key, dictionary, data_list)
