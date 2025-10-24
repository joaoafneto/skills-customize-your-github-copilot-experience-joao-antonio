"""
FastAPI REST API - Starter Code
Sistema de Gerenciamento de Biblioteca

Este código fornece a estrutura básica para construir uma API REST com FastAPI.
Complete as funções conforme as instruções da tarefa.
"""

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import Optional, List

# Inicializar a aplicação FastAPI
app = FastAPI(
    title="Biblioteca API",
    description="API REST para gerenciar uma coleção de livros",
    version="1.0.0"
)

# Modelo Pydantic para validação de dados
class Book(BaseModel):
    """Modelo representando um livro na biblioteca"""
    id: Optional[int] = None
    title: str = Field(..., min_length=1, max_length=200, description="Título do livro")
    author: str = Field(..., min_length=1, max_length=100, description="Nome do autor")
    year: int = Field(..., ge=1000, le=2100, description="Ano de publicação")
    isbn: str = Field(..., min_length=10, max_length=13, description="Código ISBN")

    class Config:
        json_schema_extra = {
            "example": {
                "title": "1984",
                "author": "George Orwell",
                "year": 1949,
                "isbn": "978-0451524935"
            }
        }

# Armazenamento em memória (lista de dicionários)
books_db: List[dict] = []
next_id = 1

# TODO: Implementar os endpoints conforme as instruções

@app.get("/")
def read_root():
    """Endpoint raiz - informações sobre a API"""
    return {
        "message": "Bem-vindo à Biblioteca API",
        "endpoints": {
            "docs": "/docs",
            "books": "/books"
        }
    }

@app.get("/books")
def get_all_books():
    """
    TODO: Implementar endpoint para listar todos os livros
    Retornar a lista completa de livros do books_db
    """
    pass

@app.get("/books/{book_id}")
def get_book(book_id: int):
    """
    TODO: Implementar endpoint para obter um livro específico por ID
    - Buscar o livro pelo ID
    - Se não encontrado, levantar HTTPException com status 404
    - Se encontrado, retornar o livro
    """
    pass

@app.post("/books", status_code=201)
def create_book(book: Book):
    """
    TODO: Implementar endpoint para criar um novo livro
    - Atribuir um ID único ao livro
    - Adicionar o livro ao books_db
    - Retornar o livro criado com o ID
    """
    pass

@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    """
    TODO: Implementar endpoint para atualizar um livro existente
    - Buscar o livro pelo ID
    - Se não encontrado, levantar HTTPException com status 404
    - Atualizar os dados do livro
    - Retornar o livro atualizado
    """
    pass

@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int):
    """
    TODO: Implementar endpoint para deletar um livro
    - Buscar o livro pelo ID
    - Se não encontrado, levantar HTTPException com status 404
    - Remover o livro do books_db
    - Retornar status 204 (sem conteúdo)
    """
    pass

@app.get("/books/search/")
def search_books(
    author: Optional[str] = Query(None, description="Buscar por autor"),
    title: Optional[str] = Query(None, description="Buscar por título"),
    year: Optional[int] = Query(None, description="Filtrar por ano")
):
    """
    TODO: Implementar endpoint de busca com query parameters
    - Filtrar livros por autor (parcial, case-insensitive)
    - Filtrar livros por título (parcial, case-insensitive)
    - Filtrar livros por ano (exato)
    - Retornar lista de livros que correspondem aos critérios
    """
    pass

# Para executar: uvicorn starter-code:app --reload
