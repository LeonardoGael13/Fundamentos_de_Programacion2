import json

biblioteca = {
    "978-84-376-0494-7": {
        "título": "Cien años de soledad",
        "autor": ["Gabriel García Márquez"],
        "géneros": ["Realismo mágico", "Novela histórica"]
    },
    "978-84-204-1625-5": {
        "título": "Don Quijote de la Mancha",
        "autor": ["Miguel de Cervantes Saavedra"],
        "géneros": ["Novela de caballería", "Sátira"]
    },
    "978-84-376-1234-5": {
        "título": "La sombra del viento",
        "autor": ["Carlos Ruiz Zafón"],
        "géneros": ["Misterio", "Drama", "Thriller histórico"]
    },
    "978-84-376-5678-9": {
        "título": "Pedro Páramo",
        "autor": ["Juan Rulfo"],
        "géneros": ["Realismo mágico", "Novela corta"]
    },
    "978-84-204-7890-1": {
        "título": "Rayuela",
        "autor": ["Julio Cortázar"],
        "géneros": ["Novela", "Experimental", "Surrealismo"]
    }
}

isbn = "978-84-376-5678-9"   # Puedes cambiar este ISBN para probar otro
info_libro = biblioteca.get(isbn)          
print("\nInformación del libro:", info_libro)