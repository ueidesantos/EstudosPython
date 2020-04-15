arquivo = open("testeArquivo.txt")

# linhas = arquivo.readlines()

# for linha in linhas:
#     print(linha)

texto_completo = arquivo.read()
arquivo.close()
print(texto_completo)




#Criando arquivos
arquivo_novo = open("ArquivoNovo.txt", "a") # W:Direito de escrita. Caso já exista, o arquivo será apagado e um novo arquivo será criado

arquivo_novo.write("MEU ARQUIVOOOOOOO1\n")

arquivo_novo.close()
