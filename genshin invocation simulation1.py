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
# "Ningguang" "Thomas" "Collei" "Candace" "Rosaria" "Beidou" "Layla" 
#"Fishl" "Yanfei" "Sayu" "Gorou" "Yun Jin" "Mika" "Kujou Sara" "Faruzan" "Heizou" "Diona" "Kuki Shinobu" "Sucrose" "Yaoyao" "Xiangling"}
#-------------------------------- si le perso 4 stars n'est pas un de la bannière, le prochain perso 4 stars sera forcément un des trois---------------------------------------


# liste arme 5 stars perma = "Atlas de la Voute d'Azur", "Berge de la Voute d'Azur", "Ailes de la Voute d'Azur", "Fierté de la Voute d'Azur", "Lame de la Voute d'Azur",
# liste armes 3 stars = "messager de l'aube", "lame froide", "épée céleste", "épée du voyageur", |"ombre ferreuse", "grande épée en fer blanc", "grande épée céleste", "épée de la raison", "épée céleste",|
# "hallebarde", "pampille blanche", "pampille noire", |"serment de l archer","messager", "lance-pierre", "arc du corbeau", "arc courbé", |"orbe jadien", "néphrite jumelle", "tales of the dragon slayers" 
# "guide de magie", "conte d'un autre monde"
# "
# mettre le système d'astérie et des trucs en couleur plus tard
#faire un dico pour chaque type d'arme genre générer d'abord la rareté puis l'arme en question
# -----> jpense faut faire une boucle qui prends en compte les garanties et ajouter des dictionnaires ?

def nombre_invocations_pour_pourcentage(desire_prcentage):
    nombre_invocations = 0
    nombre_invocations = 180 * desire_prcentage / 100
    return nombre_invocations
prcentage_voulu = 20 
nombre_d_invocations = nombre_invocations_pour_pourcentage(prcentage_voulu)
print(f"Il vous faut {nombre_d_invocations} invocations pour obtenir {prcentage_voulu}% du personnage mis en avant.")

def generate_arms_4():
    words = ["sword", "gremory", "lance", "bow", "claymore"]
    first_word = random.choice(words)
    if first_word == "lance" :
        random_number = str(random.randint(2, 4))
        result = first_word + random_number
    else :
        random_number = str(random.randint(2, 6))
        result = first_word + random_number
    
    return result

def generate_perso_5star():
    words = ["perso"]
    first_word = random.choice(words)
    random_number = str(random.randint(1, 6))
    result = first_word + random_number
    
    return result
def generate_perso_4star():
    words = ["perso"]
    first_word = random.choice(words)
    random_number = str(random.randint(1, 12))
    result = first_word + random_number
    return result

def banniere_perma_single():
    arme_5_stars_perma = {"gremory1":"Atlas de la Voute d Azur", "lance1" : "Berge de la Voute d'Azur", "bow1" : "Ailes de la Voute d'Azur",
                           "claymore1": "Fierté de la Voute d'Azur","sword1" : "Lame de la Voute d'Azur"}
    perso_5_stars = {"perso1": "Keqing", "perso2": "Mona", "perso3": "Qiqi", "perso4": "Diluc", "perso5" :"Jean", "perso6": "Tighnari", "perso6": "dehya"}
    
    perso_4_stars = {"perso1" :"Bennet", "perso2": "Amber", "perso3" : "Lisa", "perso5" : "Kaeya", "perso6" : "Barbara", "perso7": "Dori",
                      "perso8" : "Xinqyu", "perso9": "Chongyun", "perso10": "Xinyan", "perso11" :  "Razor", "perso12": "Noelle"}
    arme_4_stars_perma = {"sword2" : "rugissement du lion", "sword3" : "epee rituelle", "sword4" : "flute", "sword5" :"epee de favonius", 
                           "sword6" : "eclair des impasses","bow2": "derniere corde", "bow3" : "arc rituel","bow4" : "traqueur des impasses", "bow5" : "arc rouillé",
                          "bow6" : "arc de chasse de Favonius","claymore2" : "ombre immaculée", "claymore3" : "espadon de Favonius", "claymore4" : "fluorescence",
                          "claymore5" : "espadon rituel", "claymore6" : "espadon Royal","lance2" : "fleau du dragon", "lance3" : "la prise", "lance4" : "lance de Favonius", 
                          "gremory2" : "oeil de la perception", "gremory3" : "mouvement vagabond", "gremory4" : "atlas des Terres et des Mers",
                          "gremory5" : "memoires des rituels", "gremory6" : "code de favonius"}
    
    
    arme_3_stars_perma = {"sword2" : "messager de l'aube", "sword3" :"lame froide", "sword4" : "epee celeste", "sword5" : "épee du voyageur", "claymore2" : "ombre ferreuse", "claymore 3" : "grande epee en fer blanc", 
                          "claymore4" : "grande épée céleste", "claymore5" : "épée de la raison", "claymore6" : "épée céleste","lance2" : "hallebarde", "lance3" : "pampille blanche", "lance4" : "pampille noire", 
                          "bow2" : "serment de l archer","bow3" : "messager", "bow4": "lance-pierre", "bow5" : "arc du corbeau", "bow6" : "arc courbé", 
                          "gremory2" : "orbe jadien", "gremory3" : "néphrite jumelle", "gremory4" : "tales of the dragon slayers", "gremory5" : "guide de magie", "gremory6" :"conte d'un autre monde"}
    proba3star = 94.3
    proba4star_item = 5.100
    proba4star_item_garantie = 100
    proba4star_arme = 2.550
    proba4star_perso = 2.550
    proba5star = 0.600
    proba5star_garantie = 100  
    pity = 0  
    print("Bienvenue dans la banniere permanente !")
    print("Cette version permet l'invocation a l'unité.")
    choix = str(input("Voulez vous effectuer une invocation ? (O/N)"))
    if choix == "O":
        invoc = random.choices(["5star", "4star", "3star"], weights=[0.600, 5.100, 94.3], k=1)[0]
        if invoc == "5star":
            item5stars = random.choices(["perso", "arme"], weights=[0.50, 0.50], k=1)[0]
            if item5stars == "arme":
                arme5stars = random.choices(["gremory1", "sword1", "bow1", "lance1", "claymore1"], k=1)[0]
                print(arme_5_stars_perma[arme5stars])
            if item5stars== "perso":
                perso_obtenu  =generate_perso_5star()
                print(perso_5_stars[perso_obtenu])
        if invoc == "4star":
            item4star = random.choices(["perso", "arme"], weights=[0.50, 0.50], k=1)[0]
            if item4star == "arme":
                arme4star = generate_arms_4()
                print(arme_4_stars_perma[arme4star])
            if item4star == "perso":
                perso4star = generate_perso_4star()
                print(perso_4_stars[perso4star])
        if invoc == "3star":
            arme3star = generate_arms_4()
            print(arme_3_stars_perma[arme3star])
    elif choix == "N":
        print("D'accord, a bientot !")
    
def banniere_perma_multi_v1():
    arme_5_stars_perma = {"gremory1":"Atlas de la Voute d Azur", "lance1" : "Berge de la Voute d'Azur", "bow1" : "Ailes de la Voute d'Azur",
                           "claymore1": "Fierté de la Voute d'Azur","sword1" : "Lame de la Voute d'Azur"}
    perso_5_stars = {"perso1": "Keqing", "perso2": "Mona", "perso3": "Qiqi", "perso4": "Diluc", "perso5" :"Jean", "perso6": "Tighnari", "perso6": "dehya"}
    
    perso_4_stars = {"perso1" :"Bennet", "perso2": "Amber", "perso3" : "Lisa", "perso5" : "Kaeya", "perso6" : "Barbara", "perso7": "Dori",
                      "perso8" : "Xinqyu", "perso9": "Chongyun", "perso10": "Xinyan", "perso11" :  "Razor", "perso12": "Noelle"}
    arme_4_stars_perma = {"sword2" : "rugissement du lion", "sword3" : "epee rituelle", "sword4" : "flute", "sword5" :"epee de favonius", 
                           "sword6" : "eclair des impasses","bow2": "derniere corde", "bow3" : "arc rituel","bow4" : "traqueur des impasses", "bow5" : "arc rouillé",
                          "bow6" : "arc de chasse de Favonius","claymore2" : "ombre immaculée", "claymore3" : "espadon de Favonius", "claymore4" : "fluorescence",
                          "claymore5" : "espadon rituel", "claymore6" : "espadon Royal","lance2" : "fleau du dragon", "lance3" : "la prise", "lance4" : "lance de Favonius", 
                          "gremory2" : "oeil de la perception", "gremory3" : "mouvement vagabond", "gremory4" : "atlas des Terres et des Mers",
                          "gremory5" : "memoires des rituels", "gremory6" : "code de favonius"}
    
    
    arme_3_stars_perma = {"sword2" : "messager de l'aube", "sword3" :"lame froide", "sword4" : "epee celeste", "sword5" : "épee du voyageur", "claymore2" : "ombre ferreuse", "claymore 3" : "grande epee en fer blanc", 
                          "claymore4" : "grande épée céleste", "claymore5" : "epee de la raison", "claymore6" : "epee celeste","lance2" : "hallebarde", "lance3" : "pampille blanche", "lance4" : "pampille noire", 
                          "bow2" : "serment de l archer","bow3" : "messager", "bow4": "lance-pierre", "bow5" : "arc du corbeau", "bow6" : "arc courbé", 
                          "gremory2" : "orbe jadien", "gremory3" : "nephrite jumelle", "gremory4" : "tales of the dragon slayers", "gremory5" : "guide de magie", "gremory6" :"conte d'un autre monde"}
    liste_invocations_obtenus = []
    pity = 0
    for i in range(10):
            invoc = random.choices(["5star", "4star", "3star"], weights=[0.600, 5.100, 94.3], k=1)[0]
            if invoc == "5star":
                item5stars = random.choices(["perso", "arme"], weights=[0.50, 0.50], k=1)[0]
                if item5stars == "arme":
                    arme5stars = random.choices(["gremory1", "sword1", "bow1", "lance1", "claymore1"], k=1)[0]
                    liste_invocations_obtenus.append(arme_5_stars_perma[arme5stars])
                if item5stars== "perso":
                    perso_obtenu  =generate_perso_5star()
                    liste_invocations_obtenus.append(perso_5_stars[perso_obtenu])
            elif invoc == "4star":
                item4star = random.choices(["perso", "arme"], weights=[0.50, 0.50], k=1)[0]
                if item4star == "arme":
                    arme4star = generate_arms_4()
                    liste_invocations_obtenus.append(arme_4_stars_perma[arme4star])
                if item4star == "perso":
                    perso4star = generate_perso_4star()
                    liste_invocations_obtenus.append(perso_4_stars[perso4star])
            elif invoc == "3star":
                arme3star = generate_arms_4()
                a = arme_3_stars_perma[arme3star]
                liste_invocations_obtenus.append(a)
    return liste_invocations_obtenus
print(banniere_perma_multi_v1())

    
def banniere_perma_multi_global():
    arme_5_stars_perma = {"gremory1":"Atlas de la Voute d Azur", "lance1" : "Berge de la Voute d'Azur", "bow1" : "Ailes de la Voute d'Azur",
                           "claymore1": "Fierté de la Voute d'Azur","sword1" : "Lame de la Voute d'Azur"}
    perso_5_stars = {"perso1": "Keqing", "perso2": "Mona", "perso3": "Qiqi", "perso4": "Diluc", "perso5" :"Jean", "perso6": "Tighnari", "perso6": "dehya"}
    
    perso_4_stars = {"perso1" :"Bennet", "perso2": "Amber", "perso3" : "Lisa", "perso5" : "Kaeya", "perso6" : "Barbara", "perso7": "Dori",
                      "perso8" : "Xinqyu", "perso9": "Chongyun", "perso10": "Xinyan", "perso11" :  "Razor", "perso12": "Noelle"}
    arme_4_stars_perma = {"sword2" : "rugissement du lion", "sword3" : "epee rituelle", "sword4" : "flute", "sword5" :"epee de favonius", 
                           "sword6" : "eclair des impasses","bow2": "derniere corde", "bow3" : "arc rituel","bow4" : "traqueur des impasses", "bow5" : "arc rouillé",
                          "bow6" : "arc de chasse de Favonius","claymore2" : "ombre immaculée", "claymore3" : "espadon de Favonius", "claymore4" : "fluorescence",
                          "claymore5" : "espadon rituel", "claymore6" : "espadon Royal","lance2" : "fleau du dragon", "lance3" : "la prise", "lance4" : "lance de Favonius", 
                          "gremory2" : "oeil de la perception", "gremory3" : "mouvement vagabond", "gremory4" : "atlas des Terres et des Mers",
                          "gremory5" : "memoires des rituels", "gremory6" : "code de favonius"}
    
    
    arme_3_stars_perma = {"sword2" : "messager de l'aube", "sword3" :"lame froide", "sword4" : "epee celeste", "sword5" : "épee du voyageur", "claymore2" : "ombre ferreuse", "claymore 3" : "grande epee en fer blanc", 
                          "claymore4" : "grande épée céleste", "claymore5" : "epee de la raison", "claymore6" : "epee celeste","lance2" : "hallebarde", "lance3" : "pampille blanche", "lance4" : "pampille noire", 
                          "bow2" : "serment de l archer","bow3" : "messager", "bow4": "lance-pierre", "bow5" : "arc du corbeau", "bow6" : "arc courbé", 
                          "gremory2" : "orbe jadien", "gremory3" : "nephrite jumelle", "gremory4" : "tales of the dragon slayers", "gremory5" : "guide de magie", "gremory6" :"conte d'un autre monde"}
    liste_invocations_obtenus = []
    print("Bonjour et bienvenue sur ce second test de simulation de gacha !")
    print("Voulez vous faire une première multi ?")
    pity = 0
    
    for i in range(10):
            invoc = random.choices(["5star", "4star", "3star"], weights=[0.600, 5.100, 94.3], k=1)[0]
            if invoc == "5star":
                item5stars = random.choices(["perso", "arme"], weights=[0.50, 0.50], k=1)[0]
                if item5stars == "arme":
                    arme5stars = random.choices(["gremory1", "sword1", "bow1", "lance1", "claymore1"], k=1)[0]
                    liste_invocations_obtenus.append(arme_5_stars_perma[arme5stars])
                if item5stars== "perso":
                    perso_obtenu  =generate_perso_5star()
                    liste_invocations_obtenus.append(perso_5_stars[perso_obtenu])
            elif invoc == "4star":
                item4star = random.choices(["perso", "arme"], weights=[0.50, 0.50], k=1)[0]
                if item4star == "arme":
                    arme4star = generate_arms_4()
                    liste_invocations_obtenus.append(arme_4_stars_perma[arme4star])
                if item4star == "perso":
                    perso4star = generate_perso_4star()
                    liste_invocations_obtenus.append(perso_4_stars[perso4star])
            elif invoc == "3star":
                arme3star = generate_arms_4()
                a = arme_3_stars_perma[arme3star]
                liste_invocations_obtenus.append(a)
    print(liste_invocations_obtenus)
#fonction dans fonction ?

def banniere_perma_multi_intra(pity):
    arme_5_stars_perma = {"gremory1":"Atlas de la Voute d Azur", "lance1" : "Berge de la Voute d'Azur", "bow1" : "Ailes de la Voute d'Azur",
                           "claymore1": "Fierté de la Voute d'Azur","sword1" : "Lame de la Voute d'Azur"}
    perso_5_stars = {"perso1": "Keqing", "perso2": "Mona", "perso3": "Qiqi", "perso4": "Diluc", "perso5" :"Jean", "perso6": "Tighnari", "perso6": "dehya"}
    
    perso_4_stars = {"perso1" :"Bennet", "perso2": "Amber", "perso3" : "Lisa", "perso5" : "Kaeya", "perso6" : "Barbara", "perso7": "Dori",
                      "perso8" : "Xinqyu", "perso9": "Chongyun", "perso10": "Xinyan", "perso11" :  "Razor", "perso12": "Noelle"}
    arme_4_stars_perma = {"sword2" : "rugissement du lion", "sword3" : "epee rituelle", "sword4" : "flute", "sword5" :"epee de favonius", 
                           "sword6" : "eclair des impasses","bow2": "derniere corde", "bow3" : "arc rituel","bow4" : "traqueur des impasses", "bow5" : "arc rouillé",
                          "bow6" : "arc de chasse de Favonius","claymore2" : "ombre immaculée", "claymore3" : "espadon de Favonius", "claymore4" : "fluorescence",
                          "claymore5" : "espadon rituel", "claymore6" : "espadon Royal","lance2" : "fleau du dragon", "lance3" : "la prise", "lance4" : "lance de Favonius", 
                          "gremory2" : "oeil de la perception", "gremory3" : "mouvement vagabond", "gremory4" : "atlas des Terres et des Mers",
                          "gremory5" : "memoires des rituels", "gremory6" : "code de favonius"}
    
    
    arme_3_stars_perma = {"sword2" : "messager de l'aube", "sword3" :"lame froide", "sword4" : "epee celeste", "sword5" : "épee du voyageur", "claymore2" : "ombre ferreuse", "claymore 3" : "grande epee en fer blanc", 
                          "claymore4" : "grande épée céleste", "claymore5" : "epee de la raison", "claymore6" : "epee celeste","lance2" : "hallebarde", "lance3" : "pampille blanche", "lance4" : "pampille noire", 
                          "bow2" : "serment de l archer","bow3" : "messager", "bow4": "lance-pierre", "bow5" : "arc du corbeau", "bow6" : "arc courbé", 
                          "gremory2" : "orbe jadien", "gremory3" : "nephrite jumelle", "gremory4" : "tales of the dragon slayers", "gremory5" : "guide de magie", "gremory6" :"conte d'un autre monde"}
    liste_invocations_obtenus = []
    for i in range(10):
            invoc = random.choices(["5star", "4star", "3star"], weights=[0.600, 5.100, 94.3], k=1)[0]
            if pity == 90:
                invoc == "5star"
                if invoc == "5star":
                    item5stars = random.choices(["perso", "arme"], weights=[0.50, 0.50], k=1)[0]
                    if item5stars == "arme":
                        arme5stars = random.choices(["gremory1", "sword1", "bow1", "lance1", "claymore1"], k=1)[0]
                        liste_invocations_obtenus.append(arme_5_stars_perma[arme5stars])
                    if item5stars== "perso":
                        perso_obtenu  =generate_perso_5star()
                        liste_invocations_obtenus.append(perso_5_stars[perso_obtenu])
                elif invoc == "4star":
                    item4star = random.choices(["perso", "arme"], weights=[0.50, 0.50], k=1)[0]
                    if item4star == "arme":
                        arme4star = generate_arms_4()
                        liste_invocations_obtenus.append(arme_4_stars_perma[arme4star])
                    if item4star == "perso":
                        perso4star = generate_perso_4star()
                        liste_invocations_obtenus.append(perso_4_stars[perso4star])
                elif invoc == "3star":
                    arme3star = generate_arms_4()
                    a = arme_3_stars_perma[arme3star]
                    liste_invocations_obtenus.append(a)
            else :
                if invoc == "5star":
                    item5stars = random.choices(["perso", "arme"], weights=[0.50, 0.50], k=1)[0]
                    if item5stars == "arme":
                        arme5stars = random.choices(["gremory1", "sword1", "bow1", "lance1", "claymore1"], k=1)[0]
                        liste_invocations_obtenus.append(arme_5_stars_perma[arme5stars])
                    if item5stars== "perso":
                        perso_obtenu  =generate_perso_5star()
                        liste_invocations_obtenus.append(perso_5_stars[perso_obtenu])
                elif invoc == "4star":
                    item4star = random.choices(["perso", "arme"], weights=[0.50, 0.50], k=1)[0]
                    if item4star == "arme":
                        arme4star = generate_arms_4()
                        liste_invocations_obtenus.append(arme_4_stars_perma[arme4star])
                    if item4star == "perso":
                        perso4star = generate_perso_4star()
                        liste_invocations_obtenus.append(perso_4_stars[perso4star])
                elif invoc == "3star":
                    arme3star = generate_arms_4()
                    a = arme_3_stars_perma[arme3star]
                    liste_invocations_obtenus.append(a)
                
    print(liste_invocations_obtenus)
    
#to not end = while ?