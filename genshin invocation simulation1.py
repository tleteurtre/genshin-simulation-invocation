import random
import time
def nombre_invocations_pour_pourcentage(desire_prcentage):
    nombre_invocations = 0
    nombre_invocations = 180 * desire_prcentage / 100
    return nombre_invocations
#prcentage_voulu = 20 
#nombre_d_invocations = nombre_invocations_pour_pourcentage(prcentage_voulu)
#print(f"Il vous faut {nombre_d_invocations} invocations pour obtenir {prcentage_voulu}% du personnage mis en avant.")

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

def generate_arms_3():
    words = ["sword", "gremory", "lance", "bow", "claymore"]
    first_word = random.choice(words)
    if first_word == "lance" :
        random_number = str(random.randint(2, 4))
        resultat = first_word + random_number
    elif first_word == "sword":
        random_number = str(random.randint(2, 5))
        resultat = first_word + random_number
    else :
        random_number = str(random.randint(2, 6))
        resultat = first_word + random_number
    
    return resultat

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

def perma_single():
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
    
    
    arme_3_stars_perma = {"sword2" : "messager de l'aube", "sword3" :"lame froide", "sword4" : "epee celeste", "sword5" : "épee du voyageur", "claymore2" : "ombre ferreuse", "claymore 3" : "epee en fer blanc", 
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
            elif item5stars== "perso":
                perso_obtenu  =generate_perso_5star()
                print(perso_5_stars[perso_obtenu])
        elif invoc == "4star":
            item4star = random.choices(["perso", "arme"], weights=[0.50, 0.50], k=1)[0]
            if item4star == "arme":
                arme4star = generate_arms_4()
                print(arme_4_stars_perma[arme4star])
            elif item4star == "perso":
                perso4star = generate_perso_4star()
                print(perso_4_stars[perso4star])
        elif invoc == "3star":
            arme3star = generate_arms_3()
            print(arme_3_stars_perma[arme3star])
        time.sleep(3)    
        next = str(input(print("voulez vous refaire une invocation ? (0ui/Non)")))
        if next == "Non":
            print("D'accord, a bientot !")
            
        elif next == "Oui":
            print("tu l'aura voulu!")
            perma_single()
    else:
        print("D'accord, a bientôt !!")
    
def multi_v1():
    arme_5_stars_perma = {"gremory1":"Atlas de la Voute d Azur", "lance1" : "Berge de la Voute d'Azur", "bow1" : "Ailes de la Voute d'Azur",
                           "claymore1": "Fierté de la Voute d'Azur","sword1" : "Lame de la Voute d'Azur"}
    perso_5_stars = {"perso1": "Keqing", "perso2": "Mona", "perso3": "Qiqi", "perso4": "Diluc", "perso5" :"Jean", "perso6": "Tighnari", "perso6": "dehya"}
    
    perso_4_stars = {"perso1" :"Bennet", "perso2": "Amber", "perso3" : "Lisa", "perso5" : "Kaeya", "perso6" : "Barbara", "perso7": "Dori",
                      "perso8" : "Xinqyu", "perso9": "Chongyun", "perso10": "Xinyan", "perso11" :  "Razor", "perso12": "Noelle"}
    arme_4_stars_perma = {"sword2" : "rugissement du lion", "sword3" : "epee rituelle", "sword4" : "flute", "sword5" :"epee de favonius", 
                           "sword6" : "eclair des impasses","bow2": "derniere corde", "bow3" : "arc rituel",  "bow4" : "traqueur des impasses", "bow5" : "arc rouillé",
                          "bow6" : "arc de chasse de Favonius","claymore2" : "ombre immaculée", "claymore3" : "espadon de Favonius", "claymore4" : "fluorescence",
                          "claymore5" : "espadon rituel", "claymore6" : "espadon Royal","lance2" : "fleau du dragon", "lance3" : "la prise", "lance4" : "lance de Favonius", 
                          "gremory2" : "oeil de la perception", "gremory3" : "mouvement vagabond", "gremory4" : "atlas des Terres et des Mers",
                          "gremory5" : "memoires des rituels", "gremory6" : "code de favonius"}
    
    
    arme_3_stars_perma = {"sword2" : "messager de l'aube", "sword3" :"lame froide", "sword4" : "epee celeste", "sword5" : "épee du voyageur", "claymore2" : "ombre ferreuse", "claymore3" : "epee en fer blanc", 
                          "claymore4" : "grande épée céleste", "claymore5" : "épée de la raison", "claymore6" : "épée céleste","lance2" : "hallebarde", "lance3" : "pampille blanche", "lance4" : "pampille noire", 
                          "bow2" : "serment de l archer","bow3" : "messager", "bow4": "lance-pierre", "bow5" : "arc du corbeau", "bow6" : "arc courbé", 
                          "gremory2" : "orbe jadien", "gremory3" : "néphrite jumelle", "gremory4" : "tales of the dragon slayers", "gremory5" : "guide de magie", "gremory6" :"conte d'un autre monde"}
    liste_invocations_obtenus = []
    print("bienvenue dans cette version one shot des multi !")
    time.sleep(2)
    come_on = str(input("Tu veux commencer une multi ? Aller, lâche toi, tu verra c'est marrant (O/N)"))
    if come_on == "O":
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
                    arme3star = generate_arms_3()
                    a = arme_3_stars_perma[arme3star]
                    liste_invocations_obtenus.append(a)
        print(liste_invocations_obtenus)
        wanna_continue = str(input("Tu veux continuer ? (Yes/No)"))
        if wanna_continue == "Yes":
            print("Yes !")
            multi_v1()
        else:
            print("A la prochaine alors")
    
    else:
        print("Bah salut alors")
    
def perma_multi_global():
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
    
    
    arme_3_stars_perma = {"sword2" : "messager de l'aube", "sword3" :"lame froide", "sword4" : "epee celeste", "sword5" : "épee du voyageur", "claymore2" : "ombre ferreuse", "claymore3" : "grande epee en fer blanc", 
                          "claymore4" : "grande épée céleste", "claymore5" : "epee de la raison", "claymore6" : "epee celeste","lance2" : "hallebarde", "lance3" : "pampille blanche", "lance4" : "pampille noire", 
                          "bow2" : "serment de l archer","bow3" : "messager", "bow4": "lance-pierre", "bow5" : "arc du corbeau", "bow6" : "arc courbé", 
                          "gremory2" : "orbe jadien", "gremory3" : "nephrite jumelle", "gremory4" : "tales of the dragon slayers", "gremory5" : "guide de magie", "gremory6" :"conte d'un autre monde"}
    liste_invocations_obtenus = []
    proba3star = 94.3
    proba4star_item = 5.100
    proba4star_item_garantie = 100
    #proba4star_arme = 2.550
    #proba4star_perso = 2.550
    proba5star = 0.600
    proba5star_garantie = 100  
    pity = 0 
    
    print("Bonjour et bienvenue sur ce second test de simulation de gacha !")
    time.sleep(3)
    w = str(input("Voulez vous faire une première multi (0/N)?"))
    if w == "N":
        print("Bonne journée !")
    if w == "O":
        for i in range(10):
                invoc = random.choices(["5star", "4star", "3star"], weights=[proba5star, proba4star_item, proba3star], k=1)[0]
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
                    arme3star = generate_arms_3()
                    a = arme_3_stars_perma[arme3star]
                    liste_invocations_obtenus.append(a)
        print(liste_invocations_obtenus)
        again = str(input("Tu veux voir la suite ? (O/N)"))
        if again == "O":
            
            multi_intra(10)
        else:
            print("Merci d'avoir participé à cette expérience !")
#fonction dans fonction ?

def multi_intra(pity):
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
    
    
    arme_3_stars_perma = {"sword2" : "messager de l'aube", "sword3" :"lame froide", "sword4" : "epee celeste", "sword5" : "épee du voyageur", "claymore2" : "ombre ferreuse", "claymore3" : "grande epee en fer blanc", 
                          "claymore4" : "grande épée céleste", "claymore5" : "epee de la raison", "claymore6" : "epee celeste","lance2" : "hallebarde", "lance3" : "pampille blanche", "lance4" : "pampille noire", 
                          "bow2" : "serment de l archer","bow3" : "messager", "bow4": "lance-pierre", "bow5" : "arc du corbeau", "bow6" : "arc courbé", 
                          "gremory2" : "orbe jadien", "gremory3" : "nephrite jumelle", "gremory4" : "tales of the dragon slayers", "gremory5" : "guide de magie", "gremory6" :"conte d'un autre monde"}
    liste_invocations_obtenus = []
    for i in range(10):
            data = pity
            
            if data == 90: #cas maximum
                invoc = random.choices(["5star", "4star", "3star"], weights=[100 ,0, 0], k=1)[0]
                pity = 1
                if invoc == "5star":
                    item5stars = random.choices(["perso", "arme"], weights=[0.50, 0.50], k=1)[0]
                    if item5stars == "arme":
                        arme5stars = random.choices(["gremory1", "sword1", "bow1", "lance1", "claymore1"], k=1)[0]
                        liste_invocations_obtenus.append(arme_5_stars_perma[arme5stars])
                        
                    if item5stars== "perso":
                        perso_obtenu  =generate_perso_5star()
                        liste_invocations_obtenus.append(perso_5_stars[perso_obtenu])
                        
                
            elif data == 1: #cas minimum
                invoc = random.choices(["5star", "4star", "3star"], weights=[0.600, 5.100, 94.3], k=1)[0]
                pity = 2
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
                    arme3star = generate_arms_3()
                    a = arme_3_stars_perma[arme3star]
                    liste_invocations_obtenus.append(a)
                   
            #coder pour entre (2 et 73) et (74 et 89)
            elif 2 <= data <= 73:
                proba5star = 0.600* (10/111)**data
                invoc = random.choices(["5star", "4star", "3star"], weights=[proba5star, 5.100, 94.9-proba5star], k=1)[0]
                pity = pity +1
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
                    arme3star = generate_arms_3()
                    a = arme_3_stars_perma[arme3star]
                    liste_invocations_obtenus.append(a)
            
            elif 74 <= data <= 89:
                proba5star = 0.600 + data*6
                invoc = random.choices(["5star", "4star", "3star"], weights=[proba5star, 5.100, 94.9-proba5star], k=1)[0]
                pity = pity +1
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
                    arme3star = generate_arms_3()
                    a = arme_3_stars_perma[arme3star]
                    liste_invocations_obtenus.append(a)
                
    print(liste_invocations_obtenus)
    final = str(input("Tu veux recommencer, genre ?(Y/N)"))
    if final == "Y":
        multi_intra(pity)
    else : 
        print("See ya !")
    