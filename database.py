import json

class DBHandler :
    
    # When initiating the object means to make new profile or edit a profile
    def __init__(self, username, master_password, email) :
        
        self.username = username
        self.password = master_password
        self.email = email

        profiles_buffer = DBHandler.load_db('profilesdb.json')

        profiles_buffer.update({self.username : { 'email': self.email, 'password': self.password}})

        DBHandler.save_db(profiles_buffer, 'profilesdb.json')

        
    def load_db(db_name):
        try:
            with open(f'db/{db_name}', 'r') as db_file:
                db = json.load(db_file)
                db_file.close()
                return db
        except FileNotFoundError as err :
            return err

    def save_db(db_buffer_to_save, db_name):
        try:
            with open(f'db/{db_name}', 'w') as db_file:
                json.dump(db_buffer_to_save, db_file, indent=4)
                db_file.close()
        except NameError as err :
            return err
    
    def get_all_profile_names(db_to_query):
        try:
            with open(f'db/{db_to_query}', 'r') as db_file:
                profile_names = json.load(db_file).keys()
                db_file.close()
                return profile_names
        except FileNotFoundError as err :
            return err

    def get_password(username):
        try:
            with open(f'db/profilesdb.json', 'r') as db_file:
                password = json.load(db_file)[username]['password']
                db_file.close()
                return password
        except FileNotFoundError as err :
            return err

    def save_secret(profilename, website, db_buffer_to_save):

        secrets_buffer = DBHandler.load_db('secretdb.json')

        if not profilename in DBHandler.get_all_profile_names(db_to_query='secretdb.json') :
            secrets_buffer.update({profilename:{}})

        secrets_buffer[profilename][website] = db_buffer_to_save

        DBHandler.save_db(secrets_buffer, 'secretdb.json')

