from flask import Flask, jsonify, request, abort

app = Flask(__name__)
#hacer que el JSON salga formateado correctamente
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/')
def index():
    info = {
        "mensaje" : "Bienvenido a la API del Curriculum Vitae de Cristian Candia.",
        "acciones" : [
            "GET /curriculum",
            "POST /mensajes"
        ]
    }
    return jsonify(info)



@app.route('/curriculum', methods=['GET'])
def cv():
    url_imagen = request.host_url + "static/FotoCristian.jpeg"
    cv = {
        "nombre" : "Cristian",
        "apellido" : "Candia",
        "residencia" : "Argentina",
        "experiencia" : [{
            "posicion" : "< describe tu posición >",
            "empresa" : "< describe tu empresa >",
            "desde" : "< cuando empezaste a trabajar >",
            "hasta" : "< si ya no trabajas mas cuándo >",
        }],
        "educacion" : {
            "nivel" : "< nivel de tus estudios >",
            "titulo": "< nombre de la carrera >",
            "institucion" : "< dónde estudiaste >",
            "facultad" : "< mas detalles >",
        },
        "intereses" : ["python" , "apis", "negocios"],
        "redes" : {
            "github" : "https://github.com/criscandia",
        },
        "foto" : url_imagen
    }
    return jsonify(cv)


#tira error porque el navegador solo maneja get, hay que usar postman :(
@app.route('/mensajes', methods=['POST'])
def contacto():
    mensaje = request.get_data()
    if not mensaje:
        abort(400, description="Debe dejar su mensaje en el body del Post.")
    print("MENSAJE DEL CONTACTO: " + str(mensaje))
    return "Gracias por su mensaje."


#(debug-true) para ponerla en testing
if __name__ == '__main__':
    app.run()