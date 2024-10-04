import firebase_admin
from firebase_admin import credentials, db
import time
import socket

#firebase credentials and database url
cred = credentials.Certificate("start-rfid-firebase-adminsdk-htwny-5ac4737aef.json")
firebase_admin.initialize_app(cred, {'databaseURL' : 'https://start-rfid-default-rtdb.firebaseio.com'})

#reference to database path
ref = db.reference('/rfid')

#function to print local ip address of raspberry pi
def get_local_ip():
    try:
        return socket.gethostbyname(socket.gethostname())
    except:
        return "Unable to get IP"
#print connection information
    
print("Connected to wifi with IP:",get_local_ip())

count = 0
send_data_prev_time = 0

#main loop

while True:
    current_time = time.time()
    
    #perform firebase operation every 15 sec
    if current_time - send_data_prev_time >15:
        send_data_prev_time = current_time
        
        #setting bool value in firebase
        
        bool_value = (count % 2 ==0)
        ref.child('bool').set(bool_value)
        print(f'Set bool: {bool_value}')
        
        #Get bool value
        
        bool_from_firebase = ref.child('bool').get()
        print(f'Get bool: {bool_from_firebase}')
        
        #set string value
        
        string_value = "Hello world"
        ref.child('string').set(string_value)
        print(f"Set string : {string_value}")
        
        #Get string
        
        string_from_firebase = ref.child('string').get()
        print(f"Get string : {string_from_firebase}")
        
        
        #set json
        
        if count == 0:
            json_value = {
                'value': {
                    'round' : {str(count):'cool!'},
                    'ts': {'sv' : 'timestamp'}
                    }
                }
            ref.child('json').set(json_value)
            print(f"Set JSON: {json_value}")
        else:
            json_value = {str(count):'smart!'}
            ref.child('json/value/round').update(json_value)
            print(f"Update JSON node: {json_value}")
    count += 1
    print()
time.sleep(1)

    
                               