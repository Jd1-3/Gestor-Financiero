import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("gestor-financiero-52c68-firebase-adminsdk-equ8r-3bd471c29d.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://gestor-financiero-52c68-default-rtdb.firebaseio.com/' 
})
