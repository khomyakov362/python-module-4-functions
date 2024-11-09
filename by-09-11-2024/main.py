import utils
user_list = [] 

while len(user_list) < 4:
    user = []
    for key in utils.get_reg_data():
        user_list.append(utils.reg_check(key, utils.get_reg_data(), user_list))
    user_list.append(user)

for user in user_list:
    print(user)