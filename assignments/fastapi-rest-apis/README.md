# 📘 Assignment: Construindo APIs REST com FastAPI

## 🎯 Objective

Construir uma API REST funcional usando o framework FastAPI para gerenciar uma coleção de recursos, praticando conceitos de endpoints HTTP, validação de dados e documentação automática de APIs.

## 📝 Tasks

### 🛠️ Criar API de Gerenciamento de Livros

#### Description
Crie uma API REST completa para gerenciar uma biblioteca de livros com operações CRUD (Create, Read, Update, Delete) usando FastAPI e validação de dados com Pydantic.

#### Requirements
Completed program should:

- Implementar endpoint GET `/books` para listar todos os livros
- Implementar endpoint GET `/books/{id}` para obter um livro específico
- Implementar endpoint POST `/books` para adicionar um novo livro
- Implementar endpoint PUT `/books/{id}` para atualizar um livro existente
- Implementar endpoint DELETE `/books/{id}` para remover um livro
- Usar modelos Pydantic para validação de dados (título, autor, ano, ISBN)
- Retornar códigos de status HTTP apropriados (200, 201, 404, etc.)
- Incluir documentação automática acessível via `/docs`


### 🛠️ Adicionar Funcionalidades de Busca

#### Description
Estenda a API com funcionalidades de busca e filtro para torná-la mais útil e prática.

#### Requirements
Completed program should:

- Implementar endpoint GET `/books/search` com query parameters para buscar por autor ou título
- Adicionar filtro por ano de publicação
- Retornar lista vazia quando nenhum resultado for encontrado
- Validar e sanitizar os parâmetros de busca
