"""
Configuration of 'memos' Flask app. 
Edit to fit development or deployment environment.

"""
import random 

### My local development environment
#PORT=5000
#MONGO_PORT=27333 # On gnat, irian
#DEBUG = True
#MONGO_PW = "iremember"
#MONGO_USER = "memo"
##MONGO_URL = "mongodb://{$MONGO_USER}:{$MONGO_PW}@localhost:27333/memos"  # on Gnat
#MONGO_NOAUTH_URL = "mongodb://localhost:27333"   #  Use with 'localhost exception', running MongoDB in 'noauth' mode

GOOGLE_LICENSE_KEY = ".goog_app_key.json"


### On ix.cs.uoregon.edu 
PORT=6928#random.randint(5000,8000)
#SERVER_NAME = "ix.cs.uoregon.edu"

DEBUG = False # Because it's unsafe to run outside localhost
#MONGO_URL =  "mongodb://memo:iremember@localhost:4915/memos"  # on ix
