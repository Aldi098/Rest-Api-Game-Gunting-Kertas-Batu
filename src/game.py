import os, time, requests, json, datetime

date_object = datetime.date.today()

def poin():
	os.system("clear")
	print ('''
+===============================+
 Author : Xenzi Ganz | Aldi098
+===============================+
	''')
	print (f'[+] Kalender : {date_object}')
	print (f'\n[+] Masukan nama anda ')
	nama = input(f"[+] Name : ")
	if nama in "":
		exit('[!] masukan nama dengan benar')
	print (f'\n[+] Masukan poin anda contoh : 50,100')
	poin = input(f"[+] Poin : ")
	if poin in "":
		exit('[!] masukan poin dengan benar')
	open("Config.json","w").write(json.dumps({"nama":nama,"poin":poin}))
	time.sleep(2)
	game()

def main():
	gamee = input('[?] Inggin main lagi Y/T : ')
	if gamee in ["y","Y"]:
		game()
	else:
		os.remove("Config.json")
		exit('[!] terimakasih sudah memakai script saya >_<')

def game():
	try:
		config = json.loads(open("Config.json","r").read())
	except FileNotFoundError:
		print ('[!] nama dan poin tidak terdeteksi silahkan isi nama dan poin anda')
		time.sleep(2)
		poin()
	os.system("clear")
	print ('''
+===============================+
 Author : Xenzi Ganz | Aldi098
+===============================+
	''')
	print (f'[+] nama : {config["nama"]} ')
	print (f'[+] poin : {config["poin"]} ')
	print (f'[+] Kalender : {date_object} ')
	print (f'\n[+] Catatan : cara main gamenya sangat simpel anda harus pilih salah satu dari gunting, batu dan kertas')
	game = input(f"[+] game : ")
	res = requests.post("http://127.0.0.1:5000/game/batu-gunting-kertas",
		data={
			"user":config["nama"],
			"poin":config["poin"],
			"game":game
		}).json()
	if res["message"] in "hasil anda menang":
		print (f'\n[+] {res["results"]["user"]}')
		print (f'[+] {res["results"]["bot"]}')
		print (f'[+] Pesan : anda menang, {res["hadiah"]}')
		print (f'[+] Poin anda : {res["poin"]}')
		open("Config.json","w").write(json.dumps({"nama":res["user"],"poin":res["poin"]}))
	elif res["message"] in "hasil anda kalah":
		print (f'\n[!] {res["results"]["user"]}')
		print (f'[!] {res["results"]["bot"]}')
		print (f'[!] Pesan : anda kalah, {res["hadiah"]}')
		print (f'[!] Poin anda : {res["poin"]}')
		open("Config.json","w").write(json.dumps({"nama":res["user"],"poin":res["poin"]}))
	elif res["message"] in "hasil seri":
		print (f'\n[!] {res["results"]["user"]}')
		print (f'[!] {res["results"]["bot"]}')
		print (f'[!] Pesan : seri >_< ')
		print (f'[!] Poin anda : {res["poin"]}')
		open("Config.json","w").write(json.dumps({"nama":res["user"],"poin":res["poin"]}))
	else:
		exit(f'[!] Pesan : masukan kata gunting, batu dan kertas')
	main()
game()
