import json


profile_db = 'profilesdb.json'
secret_db = 'secretdb.json'

class DBHandler :
    
    # When initiating the object means to make new profile or edit a profile
    def __init__(self, username, master_password, email) :
        
        self.username = username
        self.password = master_password
        self.email = email

        profiles_buffer = DBHandler.load_db(profile_db)

        profiles_buffer.update({self.username : { 'email': self.email, 'password': self.password}})

        DBHandler.save_db(profiles_buffer, profile_db)

        
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

    # profile_db section

    def get_all_profile_names(db_to_query=profile_db):
        try:
            with open(f'db/{db_to_query}', 'r') as db_file:
                profile_names = json.load(db_file).keys()
                db_file.close()
                return profile_names
                
        except FileNotFoundError :
            return 'db-not-found'
 

    def get_profile_password(username, db_to_query=profile_db):
        try:
            with open(f'db/{db_to_query}', 'r') as db_file:
                password = json.load(db_file)[username]['password']
                db_file.close()
                return password

        except FileNotFoundError :
            return 'db-not-found'

    # secret_db handling section

    def get_all_websites(profile, db_to_query=secret_db):
        try:
            with open(f'db/{db_to_query}', 'r') as db_file:
                websites = json.load(db_file)[profile].keys()
                db_file.close()
                return websites

        except KeyError :
            return 'empty-profile'
        except FileNotFoundError :
            return 'db-not-found'

    def get_secret(username, website, db_to_query=secret_db):

        try:
            with open(f'db/{db_to_query}', 'r') as db_file:
                password = json.load(db_file)[username][website]['password']
                db_file.close()
                return password

        except KeyError :
            return 'not-found'
        except FileNotFoundError :
            return 'db-not-found'

    def save_secret(profilename, website, db_buffer_to_save):

        secrets_buffer = DBHandler.load_db(secret_db)

        try :
            if not profilename in DBHandler.get_all_profile_names(db_to_query=secret_db) :
                secrets_buffer.update({profilename:{}})

        except TypeError :
            return '(Error) File <secretdb.json> Not Found'
        except FileNotFoundError :
            return 'db-not-found'
            
        secrets_buffer[profilename][website] = db_buffer_to_save

        DBHandler.save_db(secrets_buffer, secret_db)
        return True

