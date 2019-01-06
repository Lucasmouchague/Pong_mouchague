from tkinter import *
from random import randint
import time

couleur_raquette1 = 'white'
couleur_raquette2 = 'white'
couleur_balle = 'white'
J1 = 0
J2 = 0
winner = ""

def balle_mouvement(canvas, vitesse):#Gestion des variable dans la fenetre game
	global J1, J2, winner

	julie = canvas.find_withtag('julie')
	raquette_2 = canvas.find_withtag('raquette_2')
	balle = canvas.find_withtag('balle')
	score = canvas.find_withtag('score')

	ballex0, balley0, ballex1, balley1 = canvas.coords(balle)#rebonds sur les bords
	if balley0 <= 0 or balley1 >= 720:
		vitesse['y'] *= -1

	if ballex0 < (canvas.coords(julie)[2]) and balley1 > (canvas.coords(julie)[1]) and balley0 < (canvas.coords(julie)[3]):#rebonds sur la raquette J1
		vitesse['x'] *= -1

	if ballex1 > (canvas.coords(raquette_2)[0]) and balley0 < (canvas.coords(raquette_2)[3]) and balley1 > (canvas.coords(raquette_2)[1]):#rebonds sur la raquette J2
		vitesse['x'] *= -1
	
	ballex0 += vitesse['x']
	ballex1 += vitesse['x']
	balley0 += vitesse['y']
	balley1 += vitesse['y']
    
	if canvas.coords(balle)[0] <= 0:#gestion des points J2
		J2 += 1
		if J2 == 3:
			winner = "Joueur 2"
			Button(canvas, text = 'Le {} a gagné avec {} a {}, cliquer pour retourner au menu'.format(winner, J2, J1), command = lambda: change_fenetre('menu')).pack()
			return 1
		else:
			canvas.delete('score')
			taille_cercle = 25
			ballex0 = 600
			balley0 = randint(0, 720)
			ballex1 = ballex0 + taille_cercle
			balley1 = balley0 + taille_cercle
			vitesse['x'] = 3
			vitesse['y'] = 3
			score = canvas.create_text(600, 10, fill = 'blue', text = 'Score J1 : {} Score J2 = {} '.format(J1, J2), tags = 'score')
			time.sleep(1)
			
	if canvas.coords(balle)[2] >= 1200:#gestion des points J1
		J1 += 1
		if J1 == 3:
			winner = "Joueur 1"
			Button(canvas, text = 'Le {} a gagné avec {} a {}, cliquer pour retourner au menu'.format(winner, J1, J2), command = lambda: change_fenetre('menu')).pack()
			return 1
		else:
			canvas.delete('score')
			taille_cercle = 25
			ballex0 = 600
			balley0 = randint(0, 720)
			ballex1 = ballex0 + taille_cercle
			balley1 = balley0 + taille_cercle
			vitesse['x'] = -3
			vitesse['y'] = -3
			score = canvas.create_text(600, 10, fill = 'blue', text = 'Score J1 : {} Score J2 = {} '.format(J1, J2), tags = 'score')
			time.sleep(1)

	canvas.coords(balle, ballex0, balley0, ballex1, balley1)
	canvas.after(10, balle_mouvement, canvas, vitesse)

def raquette_movement(canvas):#assignement des touches
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


def game(master):#initialisation de la fenetre de jeu
	global couleur_balle, couleur_raquette1, couleur_raquette2, J1, J2
	
	image = Frame(master)
	canvas = Canvas(image, width = 1200, height = 720, bg = 'black')
	canvas.pack()


	taille_cercle = 25
	
	x0, y0 = randint(150, 720-150), randint(150, 720-150)
	x1 = x0 + taille_cercle
	y1 = y0 + taille_cercle
	balle = canvas.create_oval(x0, y0, x1, y1, fill = couleur_balle, tags = 'balle')
	julie = canvas.create_rectangle(10,240,25,480,fill=couleur_raquette1, tags = 'julie')
	raquette_2 = canvas.create_rectangle(1175,240,1190,480,fill=couleur_raquette2, tags = 'raquette_2')


	score = canvas.create_text(600, 10, fill = 'blue', text = 'Score J1 : {} Score J2 = {} '.format(J1, J2), tags = 'score')
	

	vitesse = {'x': 3, 'y': 3}
	raquette_movement(canvas)

	canvas.after(10, balle_mouvement, canvas, vitesse)
	return image



def menu(master):#Menu du jeux
	image = Frame(master)
	Label(image, text ='PONG 2600').pack(fill = BOTH)
	Button(image, text = 'Jouer', command = lambda: change_fenetre('inter')).pack(fill = BOTH, pady = 3)
	Button(image, text = 'Instruction', command = lambda: change_fenetre('regle')).pack(fill = BOTH, pady = 3)
	Button(image, text = 'Quitter', command = app.quit).pack(fill = BOTH, pady = 3 )
	return image

def regle(master):#Fenetre de regle
	image = Frame(master)
	Label(image, text = 'Le but de PONG est de marqué des points dans le camps adverse.').pack(fill = BOTH)
	Label(image, text = 'Commande: Joueur 1 Z/S Joueur 2 Flèche haut / Flèche bas').pack(fill = BOTH)
	Button(image, text = 'Jouer', command = lambda: change_fenetre('inter')).pack(fill = BOTH, pady = 3)
	Button(image, text = 'Revenir au menu', command = lambda: change_fenetre('menu')).pack(fill = BOTH, pady = 2)
	return image

def inter(master):
	image = Frame(master)
	Label(image, text ='La raquette du J1 est a gauche et celle du J2 est a droite, le match est en 3 points').pack(fill = BOTH)
	Button(image, text = 'Allons-y', command = lambda: change_fenetre('jeu')).pack(fill = BOTH)
	Button(image, text = 'Revenir au menu', command = lambda: change_fenetre('menu')).pack(fill = BOTH)
	return image 

def change_fenetre(nom_fenetre):#Gestion de fenetre automatique et évolutif
	suite = app.winfo_children()
	image = suite[0]
	image.destroy()
	image_function = usine_image[nom_fenetre]
	nouv_image = image_function(app)
	nouv_image.pack()

app = Tk()
usine_image = {'jeu': game, 'menu': menu, 'regle': regle, 'inter': inter}
image = menu(app)
image.pack()
app.mainloop()