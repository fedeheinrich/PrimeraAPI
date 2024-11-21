from modelos.repos.repositorioLibros import RepositorioLibros

repo_libros = None

def obtenerRepoLibros()-> RepositorioLibros:
    global repo_libros
    if repo_libros is None:
        repo_libros = RepositorioLibros()
    return repo_libros

