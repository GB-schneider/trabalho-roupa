from flask import Flask, render_template, request, redirect, url_for

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
    }
]

# Redireciona a raiz para a página de login
@app.route('/')
def root():
    return redirect(url_for('login'))

# Página de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Login
        if username == "admin" and password == "1234":
            return redirect(url_for('index'))
        else:
            return render_template('login.html', erro="Usuário ou senha incorretos")
    
    return render_template('login.html')

# Página inicial com os produtos
@app.route('/index')
def index():
    return render_template('index.html', produtos=produtos)

# Página de detalhes do produto
@app.route('/produto/<int:produto_id>')
def produto(produto_id):
    produto = next((p for p in produtos if p["id"] == produto_id), None)
    if produto:
        return render_template('produto.html', produto=produto)
    return "Produto não encontrado", 404

if __name__ == '__main__':
    app.run(debug=True)
