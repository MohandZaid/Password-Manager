import json

class DBHandler :
    
    # When initiating the object means to make new profile or edit a profile
    def __init__(self, username, master_password, email) :
        
        self.username = username
        self.password = master_password
        self.email = email

        profiles_buffer = DBHandler.load_db('profiles.json')

        profiles_buffer.update({self.username : { 'email': self.email, 'password': self.password}})

        DBHandler.save_db(profiles_buffer, 'profiles.json')

        
    def load_db(db_name):
        try:
            with open(f'db/{db_name}', 'r') as db:
                return json.load(db)
        except FileNotFoundError as err :
            return err

    def save_db(db_buffer_to_save, db_name):
        try:
            with open(f'db/{db_name}', 'w') as db:
                json.dump(db_buffer_to_save, db)
        except NameError as err :
            return err
    
    def get_all_profile_names():
        try:
            with open(f'db/profiles.json', 'r') as db:
                return json.load(db).keys()
        except FileNotFoundError as err :
            return err

    def get_password(username):
        try:
            with open(f'db/profiles.json', 'r') as db:
                return json.load(db)[username]['password']
        except FileNotFoundError as err :
            return err

