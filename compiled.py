from tkinter import *
from random import randint
import time

couleur_raquette1 = 'black'
couleur_raquette2 = 'black'
couleur_balle = 'black'

def balle_mouvement(canvas, vitesse):
	J1 = 0
	J2 = 0

	julie = canvas.find_withtag('julie')
	raquette_2 = canvas.find_withtag('raquette_2')
	balle = canvas.find_withtag('balle')

	ballex0, balley0, ballex1, balley1 = canvas.coords(balle)
	if balley0 <= 0 or balley1 >= 720:
		vitesse['y'] *= -1

	if ballex0 < (canvas.coords(julie)[2]) and balley1 > (canvas.coords(julie)[1]) and balley0 < (canvas.coords(julie)[3]):
		vitesse['x'] *= -1

	if ballex1 > (canvas.coords(raquette_2)[0]) and balley0 < (canvas.coords(raquette_2)[3]) and balley1 > (canvas.coords(raquette_2)[1]):
		vitesse['x'] *= -1

	ballex0 += vitesse['x']
	ballex1 += vitesse['x']
	balley0 += vitesse['y']
	balley1 += vitesse['y']
    
	if canvas.coords(balle)[0] <= 0:
		J2 += 3
	
	if canvas.coords(balle)[2] >= 1200:
		J1 += 3		
	
	
	Textgame = StringVar()

	#score = Label(app, textvariable = Textgame, bg = "blue").pack()
	#Textgame.set("Score J1 : {}".format(J1)+" Score J2 : {}".format(J2))
	#canvas.create_text(600, 10, text = 'Score J1 = {} Score J2 = {}'.format(J1, J2), fill = 'blue', tags = 'point')
	#canvas.delete('point')


	canvas.coords(balle, ballex0, balley0, ballex1, balley1)
	canvas.after(10, balle_mouvement, canvas, vitesse)

def raquette_movement(canvas):
	julie = canvas.find_withtag('julie')
	raquette_2 = canvas.find_withtag('raquette_2')
	def player_1_up(event):
		canvas.move(julie,0,-30)
	def player_1_down(event):
		canvas.move(julie,0,30)
	def player_2_up(event):
		canvas.move(raquette_2,0,-30)
	def player_2_down(event):
		canvas.move(raquette_2,0,30)
	move_1_down = canvas.bind_all('<s>',player_1_down)
	smove_1_up = canvas.bind_all('<z>',player_1_up)
	move_2_down =  canvas.bind_all('<Down>', player_2_down)
	move_2_up = canvas.bind_all('<Up>', player_2_up)


def game(master):
	global couleur_balle,couleur_raquette1,couleur_raquette2
	winner = ""
	image = Frame(master)

	canvas = Canvas(image, width = 1200, height = 720)
	canvas.pack()


	taille_cercle = 25
	
	x0, y0 = randint(0, 500-50), randint(0, 500-50)
	x1 = x0 + taille_cercle
	y1 = y0 + taille_cercle
	balle = canvas.create_oval(x0, y0, x1, y1, fill = couleur_balle, tags = 'balle')
	julie = canvas.create_rectangle(10,240,25,480,fill=couleur_raquette1, tags = 'julie')
	raquette_2 = canvas.create_rectangle(1175,240,1190,480,fill=couleur_raquette2, tags = 'raquette_2')
	vitesse = {'x': 3, 'y': 3}
	raquette_movement(canvas)

	canvas.after(10, balle_mouvement, canvas, vitesse)
	return image



def menu(master):
	image = Frame(master)
	Label(image, text ='PONG 2600').pack(fill = BOTH)
	Button(image, text = 'Jouer', command = lambda: change_fenetre('perso_raquette')).pack(fill = BOTH, pady = 3)
	Button(image, text = 'Instruction', command = lambda: change_fenetre('regle')).pack(fill = BOTH, pady = 3)
	Button(image, text = 'Quitter', command = app.quit).pack(fill = BOTH, pady = 3 )
	return image

def regle(master):
	image = Frame(master)
	Label(image, text = 'Le but de PONG est de marqué des points.').pack(fill = BOTH)
	Label(image, text = 'Commande: Joueur 1 Z/S Joueur 2 Flèche haut / Flèche bas').pack(fill = BOTH)
	Button(image, text = 'Jouer', command = lambda: change_fenetre('jeu')).pack(fill = BOTH, pady = 3)
	Button(image, text = 'Revenir au menu', command = lambda: change_fenetre('menu')).pack(fill = BOTH, pady = 2)
	return image

def perso_raquette(master):
	global couleur_raquette1,couleur_raquette2
	image = Frame(master)
	canvas = Canvas(image).pack()
	Label(image, text = 'Ici vous pouvez chosir la couleur de vos raquettes').pack(fill = BOTH)
	Button(image, text = 'Raquette 1 noir').pack(fill = BOTH, side = TOP)
	Button(image, text = 'Raquette 2 noir').pack(fill = BOTH, side = BOTTOM)
	Button(image, text = 'Raquette 1 bleu').pack(fill = BOTH, side = TOP)
	Button(image, text = 'Raquette 2 bleu').pack(fill = BOTH, side = BOTTOM)
	Button(image, text = 'Raquette 1 rouge').pack(fill = BOTH, side = TOP)
	Button(image, text = 'Raquette 2 rouge').pack(fill = BOTH, side = BOTTOM)
	Button(image, text = 'Raquette 1 vert').pack(fill = BOTH, side = TOP)
	Button(image, text = 'Raquette 2 vert').pack(fill = BOTH, side = BOTTOM)
	Button(image, text = 'Continuer', command = lambda: change_fenetre('perso_balle')).pack(fill = BOTH, side = RIGHT, pady = 30)
	return image

def perso_balle(master):
	global couleur_balle
	image = Frame(master)
	canvas = Canvas(image).pack()
	Label(image, text = 'Ici vous pouvez choisir la couleur de la balle').pack(fill = BOTH)
	Button(image, text = 'Balle noir').pack(fill = BOTH, side = TOP) 
	Button(image, text = 'Balle bleu').pack(fill = BOTH, side = TOP)
	Button(image, text = 'Balle rouge').pack(fill = BOTH, side = TOP)
	Button(image, text = 'Balle vert').pack(fill = BOTH, side = TOP)
	Button(image, text = 'jouer', command = lambda: change_fenetre('jeu')).pack(fill = BOTH, side = RIGHT, pady = 30)	
	return image

def endgame(master):
	global time_game, winner
	image = Frame(master)
	canvas = Canvas(image, width = 1200, height = 720)
	canvas.pack()
	Label(image, text = 'vous avez fini la partie en '+str(time_game))
	Label(image, text = 'Le '+str(winner)+'a gagné la partie')
	Button(image, text = 'Retour au menu', command = lambda: change_fenetre('menu')).pack(fill = BOTH, pady = 3)	
	return image

def change_fenetre(nom_fenetre):
	suite = app.winfo_children()
	image = suite[0]
	image.destroy()
	image_function = usine_image[nom_fenetre]
	nouv_image = image_function(app)
	nouv_image.pack()

app = Tk()
usine_image = {'jeu': game, 'menu': menu, 'regle': regle, 'endgame': endgame, 'perso_raquette': perso_raquette, 'perso_balle': perso_balle}
image = menu(app)
image.pack()
app.mainloop()
