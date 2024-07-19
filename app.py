from flask import Flask, render_template, request, redirect, url_for, make_response
from firebasepy import database, db 
from datetime import datetime

app = Flask(__name__)


#INDEX----------------------------------------------------------------------------------------------------

#funcion raiz
@app.route("/", methods = ["GET"])
def raiz():
    
    lista_gasto = []
    fecha_gasto = []
    lista_ingreso = []
    fecha_ingreso = []

    # Suponiendo que `database` es tu conexión o acceso a la base de datos
    data_table1 = database.child('gastos').get()
    data_table2 = database.child('ingresos').get()

    # Recolectar datos de gastos
    for key, value in data_table1.items():
        lista_gasto.append(int(value['valor_gasto']))  # Convertir a entero
        fecha_gasto.append(value['fecha_gasto'])

    # Recolectar datos de ingresos
    for key, value in data_table2.items():
        lista_ingreso.append(int(value['valor_ingreso']))  # Convertir a entero
        fecha_ingreso.append(value['fecha_ingreso'])

    # Función para convertir fecha en formato mes-año
    def formato_mes_año(fecha):
        dt = datetime.strptime(fecha, '%Y-%m-%d')
        return dt.strftime('%B-%Y')

    # Diccionario para almacenar los totales por mes y año
    totales_por_mes = {}

    # Calcular totales de ingresos por mes y año
    for ingreso, fecha in zip(lista_ingreso, fecha_ingreso):
        mes_año_actual = formato_mes_año(fecha)
        if mes_año_actual not in totales_por_mes:
            totales_por_mes[mes_año_actual] = {'ingresos': 0, 'gastos': 0}
        totales_por_mes[mes_año_actual]['ingresos'] += ingreso

    # Calcular totales de gastos por mes y año
    for gasto, fecha in zip(lista_gasto, fecha_gasto):
        mes_año_actual = formato_mes_año(fecha)
        if mes_año_actual not in totales_por_mes:
            totales_por_mes[mes_año_actual] = {'ingresos': 0, 'gastos': 0}
        totales_por_mes[mes_año_actual]['gastos'] += gasto

    # Calcular saldo restante por mes y año
    for mes_año_actual, totales in totales_por_mes.items():
        totales['saldo'] = totales['ingresos'] - totales['gastos']

    # Crear un diccionario con la información solicitada
    resultado_final = {}
    for mes_año_actual, totales in totales_por_mes.items():
        resultado_final[mes_año_actual] = {
            'ingresos_totales': totales['ingresos'],
            'gastos_totales': totales['gastos'],
            'dinero_restante': totales['saldo']
        }

    return render_template('index.html', resultado_final=resultado_final)


#GASTOS----------------------------------------------------------------------------------------------------

#funcion get gastos, para llenar las tablas con informacion 

@app.route("/Gastos", methods=["GET"])
def gastos():
    
    data_gastos = database.child('gastos').get()
    gast = []
    keys = []
    for key,value in data_gastos.items(): 
        
        keys.append(key)
        gast.append(value)
        
    
    return render_template("gastos.html", gast = gast, keys = keys)

#funcion crear gastos

@app.route("/Gastos/Crear", methods = ["GET","POST"])
def crear_gastos():
    
    if request.method == "POST":
        
        origen_gasto = request.form['origen_gasto']
        fecha_gastos = request.form['fecha_gastos']
        valor_gastos = request.form['valor_gastos']
        cat_gasto = request.form['cat_gasto']
        
        ref = db.reference('/gastos')

        ref.push({
            'origen_gasto' : origen_gasto,
            'valor_gasto' : valor_gastos,
            'fecha_gasto' : fecha_gastos,
            'categoria' : cat_gasto 
        }) 
        return redirect(url_for('gastos'))
    
    return render_template('blocks/Crud_Gastos/crear.html')

#funcion actualizar gastos

@app.route('/Gastos/Actualizar/<codigo>', methods = ["GET", "POST"])
def actualizar_gastos(codigo):
    
    data = database.child('gastos').child(codigo).get()
    
    if request.method == "POST":
        
        origen_gasto = request.form['origen_gasto']
        fecha_gastos = request.form['fecha_gastos']
        valor_gastos = request.form['valor_gastos']
        cat_gasto = request.form['cat_gasto']
        
        ref = db.reference('/gastos/{0}'.format(codigo))

        ref.update({
            'origen_gasto' : origen_gasto,
            'valor_gasto' : valor_gastos,
            'fecha_gasto' : fecha_gastos,
            'categoria' : cat_gasto 
        }) 
        return redirect(url_for('gastos'))
    
    return render_template('/blocks/Crud_Gastos/actualizar.html', data = data, codigo = codigo )

#funcion eliminar gastos

@app.route('/Gastos/Eliminar/<codigo>', methods = ["GET","POST"])
def eliminar_gastos(codigo):

    try: 
        database.child('gastos').child(codigo).delete()
        return make_response('Ingreso eliminado correctamente', 200)
    except Error as err:

        print(f"Error al eliminar ingreso: {err}")
        return make_response('Error al eliminar ingreso', 404)
        
    return response, redirect(url_for('gastos'))
    
#INGRESOS----------------------------------------------------------------------------------------------------

#funcion get ingresos, para llenar las tablas con informacion 

@app.route("/Ingresos", methods=["GET"])
def ingresos():
    
    data_ingresos = database.child('ingresos').get()
    
    ingre = []
    keys = []
    for key,value in data_ingresos.items(): 
        
        keys.append(key)
        ingre.append(value)
        

    return render_template("ingresos.html", ingre = ingre, keys = keys)

#funcion crear ingresos

@app.route("/Ingresos/Crear", methods = ["GET","POST"])
def crear_ingresos():
    
    if request.method == "POST":
        valor_ingreso = request.form['valor_ingresos']
        fuente_ingreso = request.form['fuente_ingresos']
        fecha_ingreso = request.form['fecha_ingresos']
        
        ref = db.reference('/ingresos')

        ref.push({
            'fecha_ingreso' : fecha_ingreso, 
            'fuente_ingreso' : fuente_ingreso,
            'valor_ingreso' : valor_ingreso,
        }) 
        return redirect(url_for('ingresos'))
    return render_template('blocks/Crud_Ingresos/crear.html', )

# funcion actualizar ingresos

@app.route('/Ingresos/Actualizar/<codigo>', methods = ["GET", "POST"])
def actualizar_ingresos(codigo):
    
    data = database.child('ingresos').child(codigo).get()
    
    if request.method == "POST":
        
        valor_ingreso = request.form['valor_ingresos']
        fuente_ingreso = request.form['fuente_ingresos']
        fecha_ingreso = request.form['fecha_ingresos']
        
        ref = db.reference('/ingresos/{0}'.format(codigo))

        ref.update({
            'fecha_ingreso' : fecha_ingreso, 
            'fuente_ingreso' : fuente_ingreso,
            'valor_ingreso' : valor_ingreso,
        }) 
        return redirect(url_for('ingresos'))
    
    return render_template('/blocks/Crud_Ingresos/actualizar.html', data = data, codigo = codigo )

#funcion eliminar ingresos

@app.route('/Ingresos/Eliminar/<codigo>', methods = ["GET","POST"])
def eliminar_ingresos(codigo):
    
    try: 
        database.child('ingresos').child(codigo).delete()
        return make_response('Ingreso eliminado correctamente', 200)
    except Error as err:

        print(f"Error al eliminar ingreso: {err}")
        return make_response('Error al eliminar ingreso', 404)
        
    return response, redirect(url_for('ingresos'))

#Se ejecuta la aplicacion
if __name__ == "__main__":
    app.run(debug = True, port = 5000)

