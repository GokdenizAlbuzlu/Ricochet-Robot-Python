
from classe import *
import random
#Permet de choisir une cible
def choose_target():
    target_list=["EB","ER","EV","EJ","CB","CR","CV","CJ","TB","TR","TV","TJ","PB","PR","PV","PJ","MC"]


    target=random.choice(target_list)
    target_list.pop(target_list.index(target))
    return target

