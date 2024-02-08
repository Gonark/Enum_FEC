#!/usr/bin/python3
import requests
import sys
import colorama
from time import sleep

dicionario_color = {
	'amarelo': colorama.Fore.YELLOW,
	'vermelho': colorama.Fore.RED,
	'azul': colorama.Fore.BLUE,
	'verde': colorama.Fore.GREEN,
	'magenta': colorama.Fore.MAGENTA,
	'reset': colorama.Fore.RESET,
}

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
					brute_onion(nov_url, url_mod, site)	
			
	except FileNotFoundError:
		print('Wordlist não encontrada, verifique se o arquivo directory-list-2.3-medium.txt exista.')
	except IOError as e:
		print('Erro:', e)
def brute_select(site, wordlist):
	try:
		with open(wordlist, 'r', encoding='ISO-8859-1') as file:
			lines = file.readlines()
			clean_lines = [line.strip() for line in lines if "#" not in line]
			for linha in clean_lines:
				nov = linha.strip()
				nov_url = site + nov
				for extensao in [".php", ".html", ".txt", ".text", ".pdf"]:
					url_mod = f"{nov_url}{extensao}"
					brute_onion(nov_url, url_mod, site)	
			
	except FileNotFoundError:
		print('Wordlist não encontrada, verifique se o arquivo directory-list-2.3-medium.txt exista.')
	except IOError as e:
		print('Erro:', e)

def onion_verif(site):
	session = requests.session()
	session.proxys = {}
	
	session.proxys['http'] = 'sockts5h://localhost:9050'
	session.proxys['https'] = 'sockts5h://localhost:9050'
	
	user_agent = {"user_agent": "Windows 11 pro"}
	
	resp = session.get(site, headers=user_agent)
	try:
		if resp.status_code == 200:
			print(f"=====================================================\n{dicionario_color['azul']}Servidor respondendo.{dicionario_color['reset']}")
			return resp.status_code
		else:
			pass
	except Exception as erro:
		print('Erro ao acessar o servidor.', erro)
		

def brute_onion(word, word_mod, site):		
	if word == site or word_mod == site:
		pass
	else:
		session = requests.session()
		session.proxys = {}
		
		session.proxys['http'] = 'sockts5h://localhost:9050'
		session.proxys['https'] = 'sockts5h://localhost:9050'
		
		user_agent = {"user_agent": "Windows 11 pro"}
		
		resp = session.get(word, headers=user_agent)
		resp_mod = session.get(word_mod, headers=user_agent)
		try:
			if resp.status_code == 200:
				
				print(f"=====================================================\n{dicionario_color['verde']}URL descoberta: {word}{dicionario_color['reset']}")
		except Exception as erro:
			print('Erro ao acessar o servidor:', erro)	
		try:	
			if resp_mod.status_code == 200:	
				print(f"=====================================================\n{dicionario_color['verde']}URL descoberta: {word}{dicionario_color['reset']}")
			
		except Exception as erro:
			print("\n=====================================================\n{dicionario_color['vermelho']}Erro ao acessar o servidor: {dicionario_color['reset']}", erro)
	
	
def aprenset():
	z = """
	=====[!!] Seja bem-vindo [!!]====
=====================================================
		  Automatic CTF's
-----------------------------------------------------
	          Criado por FEC
-----------------------------------------------------
  Fazendo a verificação da conexão... Um momento...
"""
	for e in z:
		sys.stdout.write(e)
		sys.stdout.flush()
		sleep(0.02)
	
def main():
	op = len(sys.argv)
	
	if op < 2:
		print('=================================\nColoque o site que deseja\n'
		      'Exemplo: <enumfec.py> https://exemplo.com/\n'
		      'Coloque o -d ou -D para selecionar sua wordlist\n'
		      'Exemplo: <enumfec.py> https://exemplo.com /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt')
	
	elif op == 2:
		url = sys.argv[1]
		
		if sys.argv[1] in ['-h', '-hh', '--help']:
			print('=================================\nColoque o site que deseja\n'
		      	      'Exemplo: <enumfec.py> https://exemplo.com/\n'
		              'Coloque o -d ou -D para selecionar sua wordlist\n'
		              'Exemplo: <enumfec.py> https://exemplo.com /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt')
		else:
			try:
				aprenset()
				resp = onion_verif(url)
				if resp == 200:
					brute(url)
			except KeyboardInterrupt:
				print(f"\n=====================================================\n{dicionario_color['vermelho']}Saindo... {dicionario_color['reset']}")
	elif op == 3:
		print('Coloque os argumentos corretamente. Dê "-h" para verificar os argumentos disponiveis')
	
	elif op == 4:
		if sys.argv[1] in ['-W', '-w', '--wordlist']:
			site = sys.argv[2]
			wordlist = sys.argv[3]
			try:
				aprenset()
				resp = onion_verif(site)
				if resp == 200:
					brute_select(site, wordlist)
			except KeyboardInterrupt:
				print(f"\n=====================================================\n{dicionario_color['vermelho']}Saindo... {dicionario_color['reset']}")
		else:
			print('Coloque os argumentos corretamente. Dê "-h" para verificar os argumentos disponiveis')
if __name__ == "__main__":
	main()
