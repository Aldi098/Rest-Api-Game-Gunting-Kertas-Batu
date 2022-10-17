from flask import Flask,request,jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import random, requests, json

app=Flask(__name__)
api=Api(app)

CORS(app)

rand_poin = int(random.choice(["5","10","15","20"]))
rand_soal_1 = int(random.randint(199,599))
rand_soal_2 = int(random.randint(39,59))
class Bot_Gunting_Kertas_Batu(Resource):
	def post(self):
		if request.form.get('user'):
			if request.form.get('poin'):
				if request.form.get('game'):
					user = request.form.get('user')
					poin = int(request.form.get('poin'))
					game = request.form.get('game')
					bot = random.choice(["batu","gunting","kertas"])
					if game.lower() in bot:
						return jsonify({
							"user": user,
							"poin": poin,
							"results": {
								"user": f"anda memilih {game.capitalize()}",
								"bot": f"bot memilih {bot.capitalize()}"
							},
							"message": "hasil seri",
							"author": "Xenzi Ganz"
						})

					elif game.lower() in 'batu' and bot in 'gunting':
						tam_poin = poin + rand_poin
						return jsonify({
							"user": user,
							"poin": tam_poin,
							"hadiah": f"poin anda di tambahkan +{rand_poin}",
							"results": {
								"user": f"anda memilih {game.capitalize()}",
								"bot": f"bot memilih {bot.capitalize()}"
							},
							"message": "hasil anda menang",
							"author": "Xenzi Ganz"
						})
					elif game.lower() in 'gunting' and bot in 'kertas':
						tam_poin = poin + rand_poin
						return jsonify({
							"user": user,
							"poin": tam_poin,
							"hadiah": f"poin anda di tambahkan +{rand_poin}",
							"results": {
								"user": f"anda memilih {game.capitalize()}",
								"bot": f"bot memilih {bot.capitalize()}"
							},
							"message": "hasil anda menang",
							"author": "Xenzi Ganz"
						})
					elif game.lower() in 'kertas' and bot in 'batu':
						tam_poin = poin + rand_poin
						return jsonify({
							"user": user,
							"poin": tam_poin,
							"hadiah": f"poin anda di tambahkan +{rand_poin}",
							"results": {
								"user": f"anda memilih {game.capitalize()}",
								"bot": f"bot memilih {bot.capitalize()}"
							},
							"message": "hasil anda menang",
							"author": "Xenzi Ganz"
						})
					elif game.lower() in 'gunting' and bot in 'batu':
						min_poin = poin - rand_poin
						return jsonify({
							"user": user,
							"poin": min_poin,
							"hadiah": f"poin anda di kurangi -{rand_poin}",
							"results": {
								"user": f"anda memilih {game.capitalize()}",
								"bot": f"bot memilih {bot.capitalize()}"
							},
							"message": "hasil anda kalah",
							"author": "Xenzi Ganz"
						})
					elif game.lower() in 'kertas' and bot in 'gunting':
						min_poin = poin - rand_poin
						return jsonify({
							"user": user,
							"poin": min_poin,
							"hadiah": f"poin anda di kurangi -{rand_poin}",
							"results": {
								"user": f"anda memilih {game.capitalize()}",
								"bot": f"bot memilih {bot.capitalize()}"
							},
							"message": "hasil anda kalah",
							"author": "Xenzi Ganz"
						})
					elif game.lower() in 'batu' and bot in 'kertas':
						min_poin = poin - rand_poin
						return jsonify({
							"user": user,
							"poin": min_poin,
							"hadiah": f"poin anda di kurangi -{rand_poin}",
							"results": {
								"user": f"anda memilih {game.capitalize()}",
								"bot": f"bot memilih {bot.capitalize()}"
							},
							"message": "hasil anda kalah",
							"author": "Xenzi Ganz"
						})
					else:
						return jsonify({
							"message": "masukan batu,gunting, atau kertas",
							"author": "Xenzi Ganz"
						})
				else:
					return jsonify({
						"message": "masukan data game dengan benar",
						"author": "Xenzi Ganz"
					})
			else:
				return jsonify({
					"message": "masukan data poin dengan benar",
					"author": "Xenzi Ganz"
				})
		else:
			return jsonify({
				"message": "masukan data user dengan benar",
				"author": "Xenzi Ganz"
			})

api.add_resource(Bot_Gunting_Kertas_Batu, "/game/batu-gunting-kertas")
if __name__ == '__main__':
	app.run(debug=True)
