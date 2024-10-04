import firebase_admin
from firebase_admin import credentials, db
import time
import socket
from mfrc522 import SimpleMFRC522

#firebase credentials and database url
cred = credentials.Certificate("start-rfid-firebase-adminsdk-htwny-5ac4737aef.json")
firebase_admin.initialize_app(cred, {'databaseURL' : 'https://start-rfid-default-rtdb.firebaseio.com'})

#reference to the RFID path in the database
rfid_ref = db.reference('/rfid_data')

#initialize RFID reader
rfid_reader = SimpleMFRC522()

#function to print local ip address of raspberry pi
def get_local_ip():
    try:
        return socket.gethostbyname(socket.gethostname())
    except:
        return "Unable to get IP"
 #function to read RFID card
    
def read_rfid():
    try:
        print("place your RFID card...")
        rfid_id,text = rfid_reader.read()
        print(f"RFID ID: {rfid_id}, Text: {text.strip()}")
        return rfid_id, text.strip()
    except Exception as e:
        print(f"Error reading RFID: {e}")
        return None, None
    
#Function to upload RFID Data to firebase
    
def upload_rfid_data(rfid_id, rfid_text):
    rfid_ref.child(str(rfid_id)).set({'id': rfid_id, 'text': rfid_text, 'timestamp': time.strftime("%Y-%m-%d %H:%M:%S)})
    print(f"RFID data uploaded to firebase: ID = {rfid_id}, Text = {rfid_text}")

#Function to get RFID data from Firebase
def get_rfid_data(rfid_id):
    rfid_data = rfid_ref.child(str(rfid_id)).get()
    if rfid_data:
        print(f"Retrieved RFID data from Firebase: {rfid_data}")
    else:
        print(f"No data found for RFID ID: {rfid_id}")

  
#print connection information
    
print("Connected to wifi with IP:",get_local_ip())


#main loop

while True:
    rfid_id, rfid_text = read_rfid()
    
   
    if rfid_id is not None:
        
        #upload RFID data to Firebase
        
        upload_rfid_data(rfid_id, rfid_text)
        
        bool_value = (count % 2 ==0)
        ref.child('bool').set(bool_value)
        print(f'Set bool: {bool_value}')
        
        #Retrieve and display the RFID data from firebase
        get_rfid_data(rfid_id)
    
    time.sleep(5) #delay to avoid too frequent reads 
        
        
                               
