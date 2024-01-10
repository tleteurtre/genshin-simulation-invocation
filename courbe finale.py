import matplotlib.pyplot as plt


nombre_invoc=100
prob_succes = 0.006
compteur=1
compteur_d_invoc=1
compteur_compteur=1
prob_change=0
x_valeur=[]
y_valeur=[]

for i in range(1,nombre_invoc+1):
        prob_succes = 0.006
        x_valeur.append(compteur_d_invoc)
        y_valeur.append((1-prob_succes)**(compteur-1))
        compteur+=1
        compteur_d_invoc+=1
        if compteur==90:
            compteur=1
            x_valeur.append(compteur_d_invoc)
            y_valeur.append(0)
            compteur_d_invoc+=1

# Create the graph
plt.figure(figsize=(8, 4))
plt.plot(x_valeur, y_valeur, marker='', color='b', linestyle='-', linewidth=2, markersize=8, label='Probabilité de ne pas avoir de 5-star')
plt.xlabel('nombre d invocation')
plt.ylabel('Probabilité de ne pas avoir de 5-star')
plt.title('Probabilité de ne pas avoir de 5-star sur 100 invocations')
plt.grid(True)
plt.show()
