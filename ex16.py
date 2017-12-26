from sys import argv

# recebe as variáveis na linha de comando, antes de executar o script
script, filename = argv

# sessão de avisos iniciais
print(f"Se o arquivo ja existir, o novo conteúdo será adicionado a ele, caso vocẽ prossiga.")

# abrindo o arquivo
target = open(filename, 'a')

# inicio da edição
print("Pressione 'q' e 'Enter' para graver seu texto e sair do editor.")
while True:
	line = input("> ")
	if line == "q":
		# caso o user tecle 'q', sai do laço sem gravar a letra
		target.close()
		break
	else:
		# grava a linha atual e continua 
		target.write(f"{line}\n")

print("O conteúdo e {filename} foi atualizado.")
print("Fechando o arquivo.")
target.close()
# abre o arquivo no modo somente leitura
filename_content = open(filename, 'r')
# exibe o conteúdo do arquivo na tela
print(filename_content.read())
target.close()
