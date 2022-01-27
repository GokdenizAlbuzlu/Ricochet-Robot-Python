
	# Supposant qu'on a une classe Robot et que Robot possede un string 'color'
	# //Cobstructeur prend parametre un caractere et affecte ce caractere a la couleur du robot
	# Robot (string color) --> color="B"

	# Robot RB("B") --> color="B"
	# Robot RV("V") --> color="V"
	# Robot RR("R") --> color="R"
	# Robot RJ("J") --> color="J"
	


def victoire(target,tableau,winningRobot):
	if target =="MC":
		for r in winningRobot:
			if target == tableau[r.y][r.x].objectif :
	
				return True
		
	else:
		if target == tableau[winningRobot.y][winningRobot.x].objectif :
	
				return True
	

   
    


