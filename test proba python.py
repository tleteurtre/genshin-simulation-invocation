import random


result = random.choices(['pile', 'face'], weights=[0.3, 0.7], k=1)[0]
#print(result)

# le 0 veut dire que la valeur c le premier truc de la liste qu'il renvoie

j = 5
def nombre_invocations_pour_pourcentage(desire_prcentage):
    if (1 <= desire_prcentage <= 100):
        print("il faut un pourcentage entre 1 et 100 !")
    nombre_invocations = 0
    total_personnages = 0
    while total_personnages < 180 * desire_prcentage / 100:
        total_personnages += 1
        nombre_invocations += 1
    return nombre_invocations
pourcentage_voulu = 100  # Vous pouvez changer ce pourcentage selon vos besoins
nombre_d_invocations = nombre_invocations_pour_pourcentage(pourcentage_voulu)
print(f"Il vous faut {nombre_d_invocations} invocations pour obtenir {pourcentage_voulu}% du personnage mis en avant.")