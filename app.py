from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# Lista de produtos
produtos = [
    {
        "id": 1,
        "nome": "Camiseta Street",
        "imagem": "produto1.png",
        "preco": 79.90,
        "descricao": "Camiseta com estampa street style, feita com algodão premium. Ideal para looks urbanos."
    },
    {
        "id": 2,
        "nome": "Tênis Nike",
        "imagem": "produto2.png",
        "preco": 349.90,
        "descricao": "Tênis Nike com design esportivo, solado antiderrapante e amortecimento Air Max."
    },
    {
        "id": 3,
        "nome": "Camiseta Ferrari",
        "imagem": "produto3.png",
        "preco": 159.90,
        "descricao": "Camiseta oficial da Ferrari, com logo bordado e tecido tecnológico."
    },
    {
        "id": 4,
        "nome": "Boné Preto Nike",
        "imagem": "produto4.png",
        "preco": 89.90,
        "descricao": "Boné ajustável da Nike, perfeito para treinos e uso casual."
    },
    {
        "id": 5,
        "nome": "Tênis Airmax",
        "imagem": "produto5.png",
        "preco": 449.90,
        "descricao": "Tênis Nike Airmax, conforto extremo com visual moderno."
    },
    {
        "id": 6,
        "nome": "Luva da Nike",
        "imagem": "produto6.png",
        "preco": 99.90,
        "descricao": "Luva térmica Nike, ideal para esportes em dias frios."
    },
    {
        "id": 7,
        "nome": "Corrente de Ouro",
        "imagem": "produto7.png",
        "preco": 1299.90,
        "descricao": "Corrente banhada a ouro 18k, elegante e resistente."
    },
    {
        "id": 8,
        "nome": "Shorts Preto",
        "imagem": "produto8.png",
        "preco": 109.90,
        "descricao": "Shorts esportivo preto, leve e confortável para qualquer atividade física."
    },
    # outros produtos...
]

# Página inicial com os produtos


@app.route('/')
def index():
    return render_template('index.html', produtos=produtos)

# Rota para adicionar um produto na lista (dados via lista)


@app.route('/adicionar_produto', methods=['GET', 'POST'])
def adicionar_produto():
    if request.method == 'POST':
        novo_produto = {
            "id": len(produtos) + 1,
            "nome": request.form['nome'],
            "imagem": request.form['imagem'],
            "preco": float(request.form['preco']),
            "sugestao": request.form['sugestao']
        }
        produtos.append(novo_produto)
        return redirect(url_for('index'))  # Redireciona para a página inicial
    return render_template('adicionar_produto.html')  # Renderiza o formulário




@app.route('/novo_produto')
def novo_produto():
    return render_template('adicionar_produto.html')


@app.route('/formulario_produto', methods=['GET'])
def formulario_produto():
    return render_template('formulario_produto.html')


@app.route('/produto/<int:produto_id>')
def produto(produto_id):
    # Verificando o ID recebido e a lista de produtos
    print(f"Procurando produto com id: {produto_id}")
    print("Lista de produtos disponíveis:", produtos)

    # Busca o produto pelo ID na lista de produtos
    produto = next((p for p in produtos if p["id"] == produto_id), None)

    # Se o produto for encontrado, renderiza a página com os dados do produto
    if produto:
        return render_template('produto.html', produto=produto)

    # Caso não encontre o produto
    print(f"Produto com id {produto_id} não encontrado.")
    return "Produto não encontrado", 404


@app.route('/produtos')
def lista_produtos():
    return render_template('produtos.html', produtos=produtos)


if __name__ == '__main__':
    app.run(debug=True)
