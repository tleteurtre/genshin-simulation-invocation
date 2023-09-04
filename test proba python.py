import random


result = random.choices(['pile', 'face'], weights=[0.3, 0.7], k=1)[0]
print(result)

# le 0 veut dire que la valeur c le premier truc de la liste qu'il renvoie