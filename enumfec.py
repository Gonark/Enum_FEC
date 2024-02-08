#!/usr/bin/python3

#importando a biblioteca requests
import requests

#criando a função de verificar url
def verifica_url(url):
	#Ele vai tentar fazer as tentativas da função
	try:	
		#aqui ele vai fazer uma requisição do tipo get, utilizando a url, mudando apenas o headers e cookies
		req = requests.get(url, headers=user_agent, cookies=cookie)
		#aqui se a resposta da requisição for 200, ele irá retornar a url
		if req.status_code == 200:
			print(f'URL descoberta: {url}\n -------------------------------------------------------------------------------------------')
		#caso ele não corresponda com status de 200 ele retorna False
		else:
            		return False
        #caso a tentativa não funcionar ele vai mostrar o erro que ocorreu e sairá do programa    		
	except requests.RequestException as erro:
		print(f'Ocorreu um erro ao acessar {url}: {erro}')
		exit()
#aqui vamos criar diarios retornando em uma variavel para mudar a forma de requisição que será enviada
user_agent = {"user_agent": "Windows 11 pro"}
cookie = {"cookie": "rsrs"}
#faremos um laço para evitar graças durante o programa
while True:
	print('SEJA BEM-VINDO AO PROGRAMA DE ENUMERAÇÃO!')
	#aqui vamos fazer a generica pergunta sobre começar o programa, ele vai usar strip e upper para apenas pegar o ultimo carectere e evitar problemas, retornando para a variavel "escolha"
	escolha = input('Vamos começar? S/N --> ').strip().upper()[0]
	#caso a escolha for igual a "S", ele irá fazer as proximas perguntas
	if escolha == 'S':
		#aqui vamos saber se a requisição será mandada para a porta 80 ou 443 (http ou https)
		http = input('Seu alvo é http ou https? ')
		#vamos também escolher o dominio que será o alvo, independe se o dominio for com numeros int ou float (caso de ctf's) ou dominios com str
		dominio = input('Qual é o domínio que deseja fazer a enumeração? ')
		#então escolheremos a wordlist desejada, o qual a mesma irá ser escolhida pelo usuario
		wordlist = input('digite sua wordlist que usara ---> ')
		#aqui vamos juntar ambas variantes "http" e "dominio" para que faça a url corretamente e evitar problemas
		url = f'{http}://{dominio}/'
		#faremos uma tentativa
		try:
			#usaremos o requests para fazer a requisição get com a url e retornando tudo para o "req"
			req = requests.get(url,
				   	  headers=user_agent,
				   	  cookies=cookie)
			#se o valor de "req" for igual a "200" (resposta que ele tem acesso sem problemas na url) ele irá abrir a wordlists
			if req.status_code == 200:
				#então vamos dar um with e abriremos o arquivo da "wordlist" lendo ele, o retornando em file
				with open(wordlist, 'r', encoding='ISO-8859-1') as file:
					#vamos ler linha por linha usando readlines em file, retornando na variavel lines
					lines = file.readlines()
					#aqui iremos retirar todos os comentarios da wordlists para evitar problemas no funcionamento retornando em "clean_lines"
					clean_lines = [line.strip() for line in lines if "#" not in line]
					
					print('\nFazendo o Scan, aguarde...: \n -----------------------------------------------------')
					#aqui faremos for e in para ler linha por linha e jogar na variavel "linha"
					for linha in clean_lines:
							#aqui vamos retorar espaços na na variavel "linha" e retornar em verif
							verif = linha.strip()
							#então vamos juntar a "url" jutamente com o "verif" e assim criando uma nova url para testar
							util = url + verif
							verifica_url(util)
							#assim todo o arquivo que for testado, ele terá um teste em varias extensções ao mesmo tempo, para saber se terá um diretorio oculto nele, mesmo que o processo demore um pouco mais
							util_php = util + ".php"
							verifica_url(util_php)
							util_html = util + ".html"
							verifica_url(util_html)
							util_txt = util + ".txt"
							verifica_url(util_txt)
							util_text = util + ".text"
							verifica_url(util_text)
							util_pdf = util + ".pdf"
							verifica_url(util_pdf)
					#aqui por fim da wordlist irá parar o programa		
					break
					print('Wordlist finalizada.')
			#se a requisição for diferente de 200 ele irá retornar a falha que ocorreu e sairá do programa
			else:
		    		print(f'A requisição falhou com código de status: {req.status_code}')
			exit()
		#caso a tentativa não der certo, ele irá retornar o problema que ocorreu com o programa e assim irá sair do programa
		except requests.RequestException as erro:
			print(f'Ocorreu um erro no momento: {erro}')
		exit()
	#se a "escolha" for igual a N ele irá sair do programa
	elif escolha == 'N':
		print('Até uma proxima, saindo....')
		exit()
