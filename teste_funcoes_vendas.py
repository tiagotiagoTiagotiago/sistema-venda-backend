from funcoes_vendas import lancar_venda_como_documento, controle_preco, cadastrar_produto, efetivar_venda

# Teste da função para lançar uma venda como documento
produtos_venda_documento = {1: 2, 2: 1}  
lancar_venda_como_documento(produtos_venda_documento)

# Teste da função para controle de preço
id_produto = 1
novo_preco = 15.99
controle_preco(id_produto, novo_preco)

# Teste da função para cadastrar um novo produto
nome_novo_produto = "calça"
preco_novo_produto = 48.60
estoque_novo_produto = 13
sku_novo_produto = "Azul"
cadastrar_produto(nome_novo_produto, preco_novo_produto, estoque_novo_produto, sku_novo_produto)

# Teste da função para efetivar uma venda
venda_id = 13  # Substitua pelo ID da venda lançada como documento
efetivar_venda(venda_id)

print("Testes concluídos.")
