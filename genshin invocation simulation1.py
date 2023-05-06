import random

#infomations brutes :
# un item (personnage ou armes) 5 étoiles tout les 90 invocations
#Pour cette bannière ou le personnage mis en avant est Albédo : En prenant en compte qu'on a invoqué un item 5 étoiles, 50% de chance d'obtenir Albédo
# En prenant en compte que l'item n'est pas Albédo, le prochain personnage 5 étoiles sera forcément Albédo (Garantie)
#utiliser class pour perso 5 étoiles / 4 étoiles vers la fin ?


#proba brutes :
#taux de drop d'un perso 5 étoiles  : 0,600%, 1,600% lorsque 90 voeux sont fait depuis le dernier personnage 5 étoiles optenu.
# Dans ces personnages 5 stars, 50% de chance de tomber sur Albédo. Si le personnage optenu n'est pas Albédo, le prochain 5 stars sera forcément Albédo.

#Taux d'optenir un perso 4 stars = 2,550% pour arme = 2, 550 donc taux d'optenir un item 4 stars = 5,100% L'optention d'un item 4 stars est garanti tout les 10 voeux effectués (cet item compris)
#proba d'avoir un objet 4 stars avzc garantie  =99, 400

#Chercher rajouter les proba des autres personnages, parmi les 50% restants !
#chercher comment sont réparties les proba des perso
#je cherche à savoir comment introduire des probabilités en python

def banniere1():    
    invoc = random.choices(["5star", "4star", "3star"], weights=[0.600, 2.500, 96.900], k=1)[0]
    print(invoc)