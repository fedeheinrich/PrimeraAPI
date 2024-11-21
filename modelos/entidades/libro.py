class Libro:
    @classmethod
    def fromDiccionario(cls, dic: dict)->"Libro":
        return cls(dic["isbn"], dic["titulo"], dic["autor"], dic["genero"], dic["anio_publicacion"], dic["cantidad_ejemplares"])
    def __init__(self, isbn: int, titulo: str, autor: str, genero: str, anio_publicacion: int, cantidad_ejemplares: int = 1):
        if not isinstance(isbn, int):
            raise ValueError("El ISBN debe ser un número entero.")
        if not isinstance(titulo, str):
            raise ValueError("El título debe ser una cadena.")
        if not isinstance(autor, str):
            raise ValueError("El autor debe ser una cadena.")
        if not isinstance(genero, str):
            raise ValueError("El género debe ser una cadena.")
        if not isinstance(anio_publicacion, int):
            raise ValueError("El año de publicación debe ser un número entero.")
        if not isinstance(cantidad_ejemplares, int) and cantidad_ejemplares<0:
            raise ValueError("La cantidad de ejemplares debe ser 0 o Positivo.")
        self.__isbn = isbn
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__anio_publicacion = anio_publicacion
        self.__cantidad_ejemplares = cantidad_ejemplares

    def cambiarDatos(self, isbn, titulo, autor, genero, anio_publicacion):
        if not isinstance(isbn, int):
            raise ValueError("El ISBN debe ser un número entero.")
        if not isinstance(titulo, str):
            raise ValueError("El título debe ser una cadena.")
        if not isinstance(autor, str):
            raise ValueError("El autor debe ser una cadena.")
        if not isinstance(genero, str):
            raise ValueError("El género debe ser una cadena.")
        if not isinstance(anio_publicacion, int):
            raise ValueError("El año de publicación debe ser un número entero.")
        self.__isbn = isbn
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__anio_publicacion = anio_publicacion

    def obtenerIsbn(self)->int:
        return self.__isbn
    
    def obtenerTitulo(self)->str:
        return self.__titulo
    
    def obtenerAutor(self)->str:
        return self.__autor
    
    def obtenerGenero(self)->str:
        return self.__genero
    
    def obtenerAnioPublicacion(self)->int:
        return self.__anio_publicacion
    
    def obtenerCantidadEjemplares(self)->int:
        return self.__cantidad_ejemplares
    #
    def esIgual(self, otro: "Libro")->bool:
        return self.__isbn == otro.obtenerIsbn()
    
    def __str__(self)->str:
        return f"Libro: ISBN {self.__isbn}, Título: {self.__titulo}, Autor: {self.__autor}, Género: {self.__genero}, Año de Publicación: {self.__anio_publicacion}, Cantidad de Ejemplares: {self.__cantidad_ejemplares}"
    
    def toDiccionario(self)->dict:
        return {"isbn": self.__isbn, "titulo": self.__titulo, "autor": self.__autor, "genero": self.__genero, "anio_publicacion": self.__anio_publicacion, "cantidad_ejemplares": self.__cantidad_ejemplares}