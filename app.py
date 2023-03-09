#1.objetivo - criar api recirsos de cosulta,criação,edição e exclusão
#2.url base - local host
#3.endpoints - 
# - localhost/livros (POST) criar livro
# - localhost/livros (GET) pega odos livros
# - localhost/livros/id (GET) pega um livro
# - localhost/livros/id (PUT) alterar livro por id
# - localhost/livros/id (DELETE) deletar livro pela id
#4.recursos - Livros

# control K C comentario

from flask import Flask, jsonify, request
# request acessa ida e vinda dos dados de reqisição
# jsonify lib para json

app = Flask(__name__) # nome do projeto com o nome do arquivo atual

livros = [
        {
            'id':1,
            'titulo':'Senhor dos anéis',
            'autor': 'Tolkien'
        },
        {
            'id':3,
            'titulo':'Harry Potter',
            'autor': 'Howling'
        },
        {
            'id':3,
            'titulo':'James Clear',
            'autor': 'Hábitos Atômicos'
        }
    ]
#consultar todos
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)

#consultar 1
@app.route('/livros/<int:id>',methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
    
#editar
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
#criar
@app.route('/livros',methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)
#excluir
@app.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
            return jsonify(livros)

app.run(
    port=5000,
    host='localhost',
    debug=True
)