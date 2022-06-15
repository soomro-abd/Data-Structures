from black import Line
from platformdirs import user_cache_dir
from Task2 import LinearProbing
from Task1_A import get_hashcode, div_compression

class StorePasswords(LinearProbing):
    def __init__(self, capacity):
        self.password_table = LinearProbing(capacity)
        self.all_users = {}
    
    def store_password(self, username, password_tuple): 
        '''
        Arguments:
        username: String e.g. "Ali"
        password_tuple: Tuple e.g. ("honeyword1", "true_password", "honeyword2", 1)
                       where last index will indicate the index of the true password.
        
        Returns: Nothing
        '''

        pass_list = list(password_tuple[0:3])
        self.all_users[username] = [get_hashcode(i) for i in pass_list]

        pass_index = password_tuple[-1]
        true_pass = pass_list.pop(pass_index)
        
        self.password_table.insert_word(true_pass, False)
        
        for item in pass_list:
            self.password_table.insert_word(item, True)
    
    def find_password(self, password):
        '''
        Arguments:
        password: String 
        
        Returns: Tuple
        If the password is not found: (“login_failed”)
        If the password is the true password: (username, “successful_login”)
        If the password is a honeyword: (username, “hack_alert”)
        '''

        hash = get_hashcode(password)
        result = self.password_table.lookup_word(password)

        # print(f"The result is : {result}")

        for u_name, pass_list in self.all_users.items():
            if hash in pass_list:
                username =  u_name
                # print(f"Username: {username}")

        
        if result == None:
            # print("I am here")
            return ("login_failed")

        # print(f"Honeyword is : {result.honeyword}")
        if result.honeyword == True:
            return (username, "hack_alert")
        elif result.honeyword == False:
            return (username, "successful_login")

        # return ("login_failed")
    
    def update_password(self, old_password, new_password):
        '''
        Arguments:
        old_password: String 
        new_password: String 
        
        Returns: Tuple
        If the password is not found: (“login_failed”)
        If the password is the true password: (username, “successful_password_update”)
        If the password is a honeyword: (username, “hack_alert”)
        '''

        result = self.find_password(old_password)
        hashed_pass = get_hashcode(old_password)


        if result == ("login_failed"):
            return result

        if result[1] == "successful_login":

            #updating the dict
            user = result[0]

            pass_index = self.all_users[user].index(hashed_pass)

            self.all_users[user][pass_index] = get_hashcode(new_password)

            #updating the hash table
            self.password_table.delete_word(old_password)
            self.password_table.insert_word(new_password, False)

            return (user, "successful_password_update")

        if result[1] == "hack_alert":
            return result

        pass
    
