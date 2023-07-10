# Importar
#  flask
# flask_cors
# flask_sqlalchemy
# flask_marshmallow

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# CREAR LA APP
app = Flask(__name__)

# PERMITIR EL ACCESO DEL FRONTEND A LA RUTAS DE LAS APP
CORS(app)

# CONFIGURACIÓN A LA BASE DE DATOS                    //USER:PASSWORD@LOCALHOST/NOMBRE DB
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root@localhost/club'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False 

# PERMITE MANIPULAR LA BASE DE DATOS DE LA APP
db = SQLAlchemy(app)
ma = Marshmallow(app)

# DEFINIR LA CLASE PRODUCTO (ESTRUCTURA DE LA TABLA DE UNA BASE DE DATOS)
class Jugador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))
    posicion = db.Column(db.Integer)
    imagen = db.Column(db.String(400))

    def __init__(self,nombre, apellido,posicion, imagen):
        self.nombre = nombre
        self.apellido = apellido
        self.posicion = posicion
        self.imagen = imagen



# CÓDIGO QUE CREARÁ TODAS LAS TABLAS
with app.app_context():
    db.create_all()


# CLASE QUE PERMITIRÁ ACCEDER A LOS MÉTODOS DE CONVERSIÓN DE DATOS -  7
class JugadorSchema(ma.Schema):
    class Meta:
        fields = ("id", "nombre", "apellido", "posicion", "imagen")


# CREAR DOS OBJETOS
jugador_schema = JugadorSchema()
jugadores_schema = JugadorSchema(many=True)

# RUTAS 
# '/productos' ENDPOINT PARA RECIBIR DATOS: POST
# '/productos' ENDPOINT PARA MOSTRAR TODOS LOS PRODUCTOS DISPONIBLES EN LA BASE DE DATOS: GET
# '/productos/<id>' ENDPOINT PARA MOSTRAR UN PRODUCTO POR ID: GET
# '/productos/<id>' ENDPOINT PARA BORRAR UN PRODUCTO POR ID: DELETE
# '/productos/<id>' ENDPOINT PARA MODIFICAR UN PRODUCTO POR ID: PUT

# ENDPOINT/RUTA
@app.route("/jugadores", methods=['GET'])
def get_jugadores(): 
    # CONSULTAR TODA LA INFO EN LA TABLA PRODUCTO
    all_jugadores = Jugador.query.all()
    
    return jugadores_schema.jsonify(all_jugadores)


# RUTA CREAR UN NUEVO REGISTRO EN LA TABLA
@app.route("/jugadores", methods=['POST'])
def create_jugador(): 
    """"
    EJEMPLO:
    ENTRADA DE DATOS
    {
        "nombre": "MICROONDAS",
        "precio": 50000,
        "stock": 10,
        "imagen": "https://picsum.photos/200/300?grayscale",
    }

    """
    # RECIBEN LOS DATOS
    nombre = request.json['nombre']
    apellido =request.json['apellido'] 
    posicion =request.json['posicion'] 
    imagen = request.json['imagen']

    # INSERTAR EN DB
    new_jugador = Jugador(nombre, apellido, posicion, imagen)
    db.session.add(new_jugador)
    db.session.commit()

    return jugador_schema.jsonify(new_jugador)

    
# MOSTRAR PRODUCTO POR ID
@app.route('/jugadores/<id>',methods=['GET'])
def get_jugador(id):
    # Consultar por id, a la clase Producto.
    #  Se hace una consulta (query) para obtener (get) un registro por id
    jugador=Jugador.query.get(id)

   # Retorna el JSON de un producto recibido como parámetro
   # Para ello, usar el objeto producto_schema para que convierta con                   # jsonify los datos recién ingresados que son objetos a JSON  
    return jugador_schema.jsonify(jugador)   


# BORRAR
@app.route('/jugadores/<id>',methods=['DELETE'])
def delete_jugador(id):
    # Consultar por id, a la clase Producto.
    #  Se hace una consulta (query) para obtener (get) un registro por id
    jugador=Jugador.query.get(id)
    
    # A partir de db y la sesión establecida con la base de datos borrar 
    # el producto.
    # Se guardan lo cambios con commit
    db.session.delete(jugador)
    db.session.commit()
    return jugador_schema.jsonify(jugador)
# MODIFICAR
@app.route('/jugadores/<id>' ,methods=['PUT'])
def update_jugador(id):
    # Consultar por id, a la clase Producto.
    #  Se hace una consulta (query) para obtener (get) un registro por id
    jugador=Jugador.query.get(id)
 
    #  Recibir los datos a modificar
    nombre=request.json['nombre']
    apellido=request.json['apellido']
    posicion=request.json['posicion']
    imagen=request.json['imagen']

    # Del objeto resultante de la consulta modificar los valores  
    jugador.nombre=nombre
    jugador.apellido=apellido
    jugador.posicion=posicion
    jugador.imagen=imagen
    #  Guardar los cambios
    db.session.commit()
   # Para ello, usar el objeto producto_schema para que convierta con                     # jsonify el dato recién eliminado que son objetos a JSON  
    return jugador_schema.jsonify(jugador)


# BLOQUE PRINCIPAL
if __name__== "__main__":
    app.run(debug=True)