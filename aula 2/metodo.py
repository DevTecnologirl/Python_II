#parametros
exemplo = "Ctrl+Play - Escola de programação e robotica"
#coloca em maiusculo
print(exemplo.upper())
#coloca tudo em minusculo
print(exemplo.lower())
#divide o string nos espaços em branco
cadaPalavra = exemplo.split()
print(cadaPalavra[2])
#divide em um elemento especifico (nao inclui o elemento que foi dividido)
cadaPalavra = exemplo.split("-")
print(cadaPalavra[1])
