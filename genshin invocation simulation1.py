import random

#infomations brutes :
# un item (personnage ou armes) 5 étoiles tout les 90 invocations (89 invocs après la 1ere)
#Pour cette bannière ou le personnage mis en avant est Albédo : En prenant en compte qu'on a invoqué un item 5 étoiles, 50% de chance d'obtenir Albédo
# En prenant en compte que l'item n'est pas Albédo, le prochain personnage 5 étoiles sera forcément Albédo (Garantie)
#utiliser class pour perso 5 étoiles / 4 étoiles vers la fin ?


#proba brutes :
#taux de drop d'un perso 5 étoiles  : 0,600%, 1,600% lorsque 90 voeux sont fait depuis le dernier personnage 5 étoiles optenu.
# Dans ces personnages 5 stars, 50% de chance de tomber sur Albédo. Si le personnage optenu n'est pas Albédo, le prochain 5 stars sera forcément Albédo.

#Taux d'optenir un perso 4 stars = 2,550% pour arme = 2, 550 donc taux d'optenir un item 4 stars = 5,100% L'optention d'un item 4 stars est garanti tout les 10 voeux effectués (cet item compris)
#proba d'avoir un objet 4 stars avzc garantie  =99, 400 et les 0,600 restantes c les chances d'avoir du 5 stars

#Chercher rajouter les proba des autres personnages, parmi les 50% restants !
#chercher comment sont réparties les proba des perso (jpense que c'est aléatoire donc ez) (perma = on peut optenir TOUT les 4 stars)
#je cherche à savoir comment introduire des probabilités en python

# liste perso 5 stars perma = "Keqing" "Mona" "Qiqi" "Diluc" "Jean" "Tighnari" "dehya"

# liste perso 4 stars = TOUS = "Bennet" "Amber" "Lisa" "Kaeya" "Barbara" "Dori" "Xinqyu" "Chongyun" "Xinyan" "Razor" "Noelle" "Ningguang" "Thomas" "Collei" "Candace" "Rosaria" "Beidou" "Layla" 
# "Fishl" "Yanfei" "Sayu" "Gorou" "Yun Jin" "Mika" "Kujou Sara" "Faruzan" "Heizou" "Diona" "Kuki Shinobu" "Sucrose" "Yaoyao" "Xiangling"
#-------------------------------- si le perso 4 stars n'est pas un de la bannière, le prochain perso 4 stars sera forcément un des trois---------------------------------------

# liste arme 5 stars perma = "Atlas de la Voute d'Azur", "Berge de la Voute d'Azur", "Ailes de la Voute d'Azur", "Fierté de la Voute d'Azur", "Lame de la Voute d'Azur",

# liste arme 4 stars perma = "rugissement du lion", "épée rituelle", "flute", "épée de favonius", "eclair des impasses", | "ombre immaculée", "fluorescence", "espadon royal", "espadon rituel", "épée horloge",
# "espadon de favonius" |"lance de favonius" "fléau du dragon" "la prise"| "traqueur des impasses" "arc rituel" "derniere corde" "arc rouillé" "arc de chasse de favonius" |"oeil de la perception"
# "memoire de rituels", "mouvements vagabonds", "code de favonius", "atlas des terres et des mers"

# liste armes 3 stars = "messager de l'aube", "lame froide", "épée céleste", "épée du voyageur", |"ombre ferreuse", "grande épée en fer blanc", "grande épée céleste", "épée de la raison", "épée céleste",|
# "hallebarde", "pampille blanche", "pampille noire", |"serment de l archer","messager", "lance-pierre", "arc du corbeau", "arc courbé", |"orbe jadien", "néphrite jumelle", "tales of the dragon slayers" 
# "guide de magie", "conte d'un autre monde"
# "
# mettre le système d'astérie et des trucs en couleur plus tard
#faire un dico pour chaque type d'arme genre générer d'abord la rareté puis l'arme en question
# -----> jpense faut faire une boucle qui prends en compte les garanties et ajouter des dictionnaires ?
def banniere_perma_alpha():
    arme_5_stars_perma = {"gremory1":"Atlas de la Voute d Azur", "lance1" : "Berge de la Voute d'Azur", "bow1" : "Ailes de la Voute d'Azur",
                           "claymore1": "Fierté de la Voute d'Azur","sword1" : "Lame de la Voute d'Azur"}
    sword4starsperma = {"sword2" : "rugissement du lion", "sword3" : "epee rituelle", "sword4" : "flute", "sword5" :"epee de favonius", 
                         "sword6" : "eclair des impasses"}
    bow4starsperma = {"bow2": "derniere corde", "bow3" : "arc rituel","bow4" : "traqueur des impasses", "bow5" : "arc rouillé", 
                      "bow6" : "arc de chasse de Favonius"}
    claymore4starsperma ={"claymore2" : "ombre immaculée", "claymore3" : "espadon de Favonius", "claymore4" : "fluorescence",
                          "claymore5" : "espadon rituel", "claymore6" : "espadon Royal"}
    lance4starsperma = {"lance2" : "fleau du dragon", "lance3" : "la prise", "lance4" : "lance de Favonius"}

    gremory4starsperma = {"gremory2" : "oeil de la perception", "gremory3" : "mouvement vagabond", "gremory4" : "atlas des Terres et des Mers",
                          "gremory5" : "memoires des rituels", "gremory6" : "code de favonius"}
    proba3star = 94.3
    proba4star_item = 5.100
    proba4star_item_garantie = 100
    proba4star_arme = 2.550
    proba4star_perso = 2.550
    proba5star = 0.600
    proba5star_garantie = 100    
    invoc = random.choices(["5star", "4star", "3star"], weights=[0.600, 5.100, 94.3], k=1)[0]
    if invoc == "5star":
        arme5stars = random.choices(["grimoire1", "sword1", "bow1", "lance1", "claymore1"], k=1)[0]
        print(sword4starsperma[arme5stars])
        