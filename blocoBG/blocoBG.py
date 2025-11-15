# Nome do arquivo
nome_arquivo = "mensagem.txt"

# Conteúdo a ser escrito
conteudo = "Bom dia"

# Abre (ou cria) o arquivo e escreve o conteúdo
with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.write(conteudo)

print(f"Arquivo '{nome_arquivo}' criado com sucesso!")
