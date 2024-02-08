#!/usr/bin/python3
import requests
import sys

def brute(site):
	try:
		with open('/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt', 'r', encoding='ISO-8859-1') as file:
			lines = file.readlines()
			clean_lines = [line.strip() for line in lines if "#" not in line]
			for linha in clean_lines:
				nov = linha.strip()
				nov_url = site + nov
				for extensao in [".php", ".html", ".txt", ".text", ".pdf"]:
					url_mod = f"{nov_url}{extensao}"
					brute_onion(nov_url, url_mod)	
			
	except FileNotFoundError:
		print('Wordlist não encontrada, verifique se o arquivo directory-list-2.3-medium.txt exista.')
	except IOError as e:
		print('Erro:', e)
def brute_select(site, wordlist):
	try:
		with open('wordlist', 'r', encoding='ISO-8859-1') as file:
			lines = file.readlines()
			clean_lines = [line.strip() for line in lines if "#" not in line]
			for linha in clean_lines:
				nov = linha.strip()
				nov_url = site + nov
				for extensao in [".php", ".html", ".txt", ".text", ".pdf"]:
					url_mod = f"{nov_url}{extensao}"
					brute_onion(nov_url, url_mod)	
			
	except FileNotFoundError:
		print('Wordlist não encontrada, verifique se o arquivo directory-list-2.3-medium.txt exista.')
	except IOError as e:
		print('Erro:', e)

def onion_verif(site):
	session = requests.session()
	session.proxys = {}
	
	session.proxys['http'] = 'sockets5h://localhost:9050'
	session.proxys['https'] = 'sockets5h://localhost:9050'
	
	user_agent = {"user_agent": "Windows 11 pro"}
	
	resp = session.get(site, headers=user_agent)
	try:
		if resp.status_code == 200:
			print('Servidor respondendo.')
			return resp.status_code
		else:
			pass
	except Exception as erro:
		print('Erro ao acessar o servidor.', erro)
		

def brute_onion(word, word_mod):		
	session = requests.session()
	session.proxys = {}
	
	session.proxys['http'] = 'sockets5h://localhost:9050'
	session.proxys['https'] = 'sockets5h://localhost:9050'
	
	user_agent = {"user_agent": "Windows 11 pro"}
	
	resp = session.get(word, headers=user_agent)
	resp_mod = session.get(word_mod, headers=user_agent)
	try:
		if resp.status_code == 200:
			print(f'URL descoberta: {word}')
		else:
			pass
	except Exception as erro:
		print('Erro ao acessar o servidor:', erro)	
	try:	
		if resp_mod.status_code == 200:	
			print(f'URL decoberta: {word_mod}')
		
	except Exception as erro:
		print("Erro ao acessar o servidor:", erro)
	
def main():
	op = len(sys.argv)
	
	if op < 2:
		print('Coloque sua URL como argumento, ou -d para selecionar wordlist\n'
		      'Exemplo: \n<enum.py> https://youtube.com/\n<enum.py> -D https://youtube.com/ /usr/share/wordlists/(arquivo)')
	
	elif op == 2:
		url = sys.argv[1]
		try:
			resp = onion_verif(url)
			if resp == 200:
				brute(url)
			else:
				exit()
		except KeyboardInterrupt:
			print('\nSaindo...')
			exit()
	elif op == 3:
		print('Coloque os argumentos corretamente.')
	
	elif op == 4:
		if sys.argv[2] in ['-W', '-w', '--wordlist']:
			site = sys.argv[2]
			wordlist = sys.argv[3]
			try:
				resp = onion_verif(url)
				if resp == 200:
					brute_select(site, wordlist)
			except KeyboardInterrupt:
				print('\nSaindo...')
if __name__ == "__main__":
	main()

