from funcoes_vendas import lancar_venda_como_documento, efetivar_venda, gerar_pdf_venda

# Teste da função para lançar uma venda como documento
produtos_venda_documento = {1: 2, 2: 1}  
venda_id = lancar_venda_como_documento(produtos_venda_documento)

# Teste da função para efetivar uma venda
efetivar_venda(venda_id)

# Gerar PDF da venda
nome_arquivo = f"venda_{venda_id}.pdf"
produtos_vendidos = produtos_venda_documento  # Substitua pelos produtos vendidos
gerar_pdf_venda(venda_id, produtos_vendidos, nome_arquivo)
