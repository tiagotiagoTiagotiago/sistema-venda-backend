from conexao_banco import conectar_banco
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def lancar_venda_como_documento(produtos):
    try:
        conexao = conectar_banco()
        if conexao:
            cursor = conexao.cursor()

            print("Produtos para a venda (documento):", produtos)
            
            # Inserir a venda como documento na tabela Vendas
            cursor.execute("INSERT INTO Vendas (data, total, efetivada) VALUES (NOW(), 0, 0)")
            venda_id = cursor.lastrowid
            
            print("ID da venda (documento):", venda_id)
            
            # Verificar se os produtos existem na tabela Produtos
            for produto_id in produtos.keys():
                cursor.execute("SELECT COUNT(*) FROM Produtos WHERE id = %s", (produto_id,))
                resultado = cursor.fetchone()[0]
                if resultado == 0:
                    raise Exception(f"Produto com ID {produto_id} não encontrado na tabela Produtos.")
            
            # Inserir os itens da venda como documento na tabela Itens_Venda
            for produto_id, quantidade in produtos.items():
                cursor.execute("INSERT INTO Itens_Venda (id_venda, id_produto, quantidade, subtotal) VALUES (%s, %s, %s, 0)", (venda_id, produto_id, quantidade))
            
            # Commit das alterações no banco de dados
            conexao.commit()
            
            print("Venda lançada como documento com sucesso!")
            cursor.close()
            conexao.close()
            return venda_id
    except Exception as e:
        print("Erro ao lançar venda como documento:", e)
        # Rollback em caso de erro
        conexao.rollback()

def efetivar_venda(venda_id):
    try:
        conexao = conectar_banco()
        if conexao:
            cursor = conexao.cursor()

            # Atualizar a venda para efetivada na tabela Vendas
            cursor.execute("UPDATE Vendas SET efetivada = 1 WHERE id = %s", (venda_id,))
            
            # Buscar os itens da venda
            cursor.execute("SELECT id_produto, quantidade FROM Itens_Venda WHERE id_venda = %s", (venda_id,))
            itens_venda = cursor.fetchall()
            
            # Atualizar o estoque dos produtos vendidos na tabela Produtos
            for item in itens_venda:
                produto_id, quantidade = item
                cursor.execute("UPDATE Produtos SET estoque = estoque - %s WHERE id = %s", (quantidade, produto_id))
            
            # Commit das alterações no banco de dados
            conexao.commit()
            
            print("Venda efetivada com sucesso!")
            cursor.close()
            conexao.close()
    except Exception as e:
        print("Erro ao efetivar venda:", e)
        # Rollback em caso de erro
        conexao.rollback()

def controle_preco(id_produto, novo_preco):
    try:
        conexao = conectar_banco()
        if conexao:
            cursor = conexao.cursor()

            # Atualizar o preço do produto na tabela Produtos
            cursor.execute("UPDATE Produtos SET preco = %s WHERE id = %s", (novo_preco, id_produto))
            
            # Commit das alterações no banco de dados
            conexao.commit()
            
            print("Preço do produto atualizado com sucesso!")
            cursor.close()
            conexao.close()
    except Exception as e:
        print("Erro ao atualizar o preço do produto:", e)
        # Rollback em caso de erro
        conexao.rollback()

def cadastrar_produto(nome, preco, estoque, sku):
    try:
        conexao = conectar_banco()
        if conexao:
            cursor = conexao.cursor()

            # Inserir um novo produto na tabela Produtos
            cursor.execute("INSERT INTO Produtos (nome, preco, estoque, sku) VALUES (%s, %s, %s, %s)", (nome, preco, estoque, sku))
            
            # Commit das alterações no banco de dados
            conexao.commit()
            
            print("Novo produto cadastrado com sucesso!")
            cursor.close()
            conexao.close()
    except Exception as e:
        print("Erro ao cadastrar novo produto:", e)
        # Rollback em caso de erro
        conexao.rollback()

def gerar_pdf_venda(venda_id, produtos_vendidos, nome_arquivo):
    try:
        # Criar o documento PDF
        c = canvas.Canvas(nome_arquivo, pagesize=letter)
        c.drawString(100, 750, f"Venda ID: {venda_id}")

        y = 700
        for produto_id, quantidade in produtos_vendidos.items():
            # Buscar informações do produto no banco de dados
            conexao = conectar_banco()
            cursor = conexao.cursor()
            cursor.execute("SELECT nome, preco, sku FROM Produtos WHERE id = %s", (produto_id,))
            produto = cursor.fetchone()
            cursor.close()
            conexao.close()
            
            nome_produto, preco_produto, sku_produto = produto
            
            # Adicionar informações do produto ao PDF
            c.drawString(100, y, f"Produto: {nome_produto}, SKU: {sku_produto}, Quantidade: {quantidade}, Preço: R${preco_produto:.2f}")
            y -= 20

        # Fechar o documento PDF
        c.save()

        print(f"PDF da venda {venda_id} gerado com sucesso: {nome_arquivo}")
    except Exception as e:
        print("Erro ao gerar PDF da venda:", e)
