import matplotlib.pyplot as plt


nombre_invoc=90
prob_succes = 0.006
compteur=1

x_valeur=[]
y_valeur=[]
for k in range(1,nombre_invoc+1):
        if compteur<=73:
                x_valeur.append(k)
                y_valeur.append((1-prob_succes)**(k-1))
                compteur+=1
        elif 73<compteur:
                for k in range(nombre_invoc-15,nombre_invoc-1):
                        x_valeur.append(k)
                        y_valeur.append((1-prob_succes)**(k-1)-0.06)
                        compteur+=1
#        elif compteur==90:
 #               compteur+=1
  #              x_valeur.append(k)
   #             y_valeur.append(0)






# Création du graphique
plt.figure(figsize=(8, 4))
plt.plot(x_valeur, y_valeur, marker='', color='b', linestyle='-', linewidth=2, markersize=8, label='Probabilité de ne pas obtenir de 5 étoiles')
plt.xlabel('Nombre d\'invocations')
plt.ylabel('Probabilité de ne pas avoir un 5 étoile')
plt.title('Probabilité de ne pas obtenir un 5 étoile sur 100 invocations')
plt.grid(True)
plt.show()
