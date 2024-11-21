from entidades.libro import Libro
from typing import List
import json
class RepositorioLibros:
    __rutaArchivo = "datos/libros.json"
    def __init__(self, libros: List [Libro]):
        self.__libros = self.__cargarTodos()

    def __cargarTodos(self):
        """Esta función se encarga de cargar todos los libros desde un archivo JSON"""
        lista_diccionarios = []
        lista_objetos = []
        try:
            with open(RepositorioLibros.__rutaArchivo, "r", encoding="UTF-8") as file:
                lista_diccionarios = json.load(file)
        except:
            print("Error al cargar datos del archivo libros.json")
        for dicc in lista_diccionarios:
            lista_objetos.append(Libro.fromDiccionario(dicc))
        return lista_objetos
    
    def __guardarTodos(self):
        """Esta función se encarga de guardar todos los libros en un archivo JSON """
        lista_diccionarios = []
        for libro in self.__libros:
            if isinstance(libro, Libro):
                lista_diccionarios.append(libro.toDiccionario())
        with open(RepositorioLibros.__rutaArchivo, "w", encoding="utf-8") as file:
            json.dump(lista_diccionarios, file, indent=4)
        
    def obtenerTodos(self)->List[Libro]:
        return self.__libros
    
    def obtenerLibroPorIsbn(self, isbn: int)->"Libro":
        for libro in self.__libros:
            if libro.obtenerIsbn() == isbn:
                return libro
        return None
    
    def existeLibro(self, libro: Libro)->bool:
        return libro in self.__libros
    
    def existeIsbn(self, isbn: int)->bool:
        for libro in self.__libros:
            if libro.obtenerIsbn() == isbn:
                return True
        return False
    
    def agregar(self, libro: Libro):
        if not self.existeLibro(libro):
            self.__libros.append(libro)
            self.__guardarTodos()
        else:
            print("El libro ya existe en el repositorio.")
    
    def modificarPorIsbn(self, isbn: int, titulo: str, autor: str, genero: str, anio_publicacion: int):
        for libro in self.__libros:
            if libro.obtenerIsbn() == isbn:
                libro.cambiarDatos(isbn, titulo, autor, genero, anio_publicacion)
                self.__guardarTodos()
                return True
        return False

    def eliminarPorIsbn(self, isbn:int):
        for libro in self.__libros:
            if libro.obtenerIsbn() == isbn:
                self.__libros.remove(libro)
                self.__guardarTodos()
                return True
        return False