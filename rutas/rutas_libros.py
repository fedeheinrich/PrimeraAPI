from flask import Blueprint, request, jsonify
from modelos.repos.repositorios import obtenerRepoLibros
from modelos.entidades.libro import Libro 

repo_libros = obtenerRepoLibros()

bp_libros = Blueprint("bp_libros", __name__)

@bp_libros.route("/libros", methods=["GET"])
def obtener_todos():
    lista_dicc = []
    for libro in repo_libros.obtenerTodos():
        lista_dicc.append(libro.toDiccionario())
    return jsonify(lista_dicc)

@bp_libros.route("/libros/<isbn>", methods=["GET"])
def obtener_libro_por_isbn(isbn):
    libro_encontrado = repo_libros.obtenerLibroPorIsbn()
    if libro_encontrado != None:
        return jsonify({"mensaje": "Libro encontrado", "libro": libro_encontrado.toDiccionario()}), 200
    else:
        return jsonify({"mensaje": "Libro no encontrado"}), 404

@bp_libros.route("/libros", methods=["POST"])    
def agregar():
    if request.is_json():
        diccDatos = request.get_json()
        if "isbn" in diccDatos and "titulo" in diccDatos and "autor" in diccDatos and "genero" in diccDatos and "anio_publicacion" in diccDatos:
            libro_creado = Libro.fromDiccionario(diccDatos)
            # alumno_creado_V2 = Alumno(diccDatos["legajo"]
            if repo_libros.existeIsbn(libro_creado.obtenerIsbn()):
                respuesta = {"mensaje": "El ISBN ingresado ya existe"}
                codigoRespuesta = 400
            else:
                repo_libros.agregar(libro_creado)
                respuesta = {"mensaje": "Libro agregado correctamente", "libro": libro_creado.toDiccionario()}
                codigoRespuesta = 201
        else:
            respuesta = {"mensaje": "Faltan datos en el JSON"}
            codigoRespuesta = 400
    else:
        respuesta = {"mensaje": "Los datos deben estar en formato JSON"}
        codigoRespuesta = 400
    return jsonify(respuesta), codigoRespuesta

@bp_libros.route("/libros/<int:isbn>", methods =["PUT"])  
def modificar(isbn):
    if request.is_json:
        diccDatos = request.get_json()
        if "titulo" in diccDatos and "autor" in diccDatos and "genero" in diccDatos and "anio_publicacion" in diccDatos:
            if repo_libros.existeIsbn(isbn):
                repo_libros.modificarPorIsbn(isbn,diccDatos["titulo"],diccDatos["autor"],diccDatos["genero"],diccDatos["anio_publicacion"])
                respuesta ={"mensaje":"Libro modficado"}
                codigoRespuesta = 200
            else:
                respuesta ={"mensaje":"Libro no encontrado"}
                codigoRespuesta = 404
        else:
            respuesta = {"mensaje":"faltan datos en el json"}
            codigoRespuesta = 400
    else:
        respuesta =  {"mensaje":"Los datos deben estar en formato json"}
        codigoRespuesta=400
    return jsonify(respuesta), codigoRespuesta

@bp_libros.route("/libros/<int:isbn>", methods =["DELETE"])
def borrar(isbn):
    if repo_libros.existeIsbn(isbn):
        repo_libros.eliminarPorIsbn(isbn)
        return jsonify({"mensaje":"Libro eliminado"}), 200
    else:
        return jsonify({"mensaje":" Libro no encontrado"}), 404
