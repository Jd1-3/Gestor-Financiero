import firebase_admin
from firebase_admin import credentials, db

# Inicializa la app de Firebase con las credenciales y URL de Realtime Database
cred = credentials.Certificate('gestor-financiero-52c68-firebase-adminsdk-equ8r-d9ad691e4a.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://gestor-financiero-52c68-default-rtdb.firebaseio.com/'
})

# Obtén una referencia a la base de datos de Realtime Database
database = db.reference()
# ref = db.reference('/gastos')

# ref.push ({
#     'id_gasto' : '2',
#     'origen_gasto' : 'pasajes',
#     'valor_gasto' : '200000',
#     'fecha_gasto' : '2024-07-20',
#     'categoria' : 'Transporte'
# })