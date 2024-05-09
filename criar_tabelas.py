from conexao_banco import conectar_banco
def criar_tabelas():
    try:
        conexao = conectar_banco()
        if conexao:
            cursor = conexao.cursor()

            # Criar tabela Produtos
            cursor.execute("CREATE TABLE IF NOT EXISTS Produtos (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), preco DECIMAL(10,2), estoque INT, sku VARCHAR(50))")

            # Criar tabela Vendas
            cursor.execute("CREATE TABLE IF NOT EXISTS Vendas (id INT AUTO_INCREMENT PRIMARY KEY, data DATE, total DECIMAL(10,2), efetivada BOOLEAN DEFAULT FALSE)")

            # Criar tabela Itens_Venda
            cursor.execute("CREATE TABLE IF NOT EXISTS Itens_Venda (id INT AUTO_INCREMENT PRIMARY KEY, id_venda INT, id_produto INT, quantidade INT, subtotal DECIMAL(10,2), FOREIGN KEY (id_venda) REFERENCES Vendas(id), FOREIGN KEY (id_produto) REFERENCES Produtos(id))")

            print("Tabelas criadas com sucesso!")
            cursor.close()
            conexao.close()
    except Exception as e:
        print("Erro ao criar tabelas:", e)

# Chamada da função para criar as tabelas
criar_tabelas()
