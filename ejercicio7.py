notas1=[81,60,72,24,15,91,12,70,29,42,16,3,35,67,10,57,11,69,12,77,13,86,48,65,51,41,87,43,10,87,91,15,44,85,73,37,42,95,18,7,74,60,9,65,93,63,74]
notas2=[30,95,28,84,84,43,66,51,4,11,58,10,13,34,96,71,86,37,64,13,8,87,14,14,49,27,55,69,77,59,57,40,96,24,30,73,95,19,47,15,31,39,15,74,33,57,10]
Nom= ['Agustin','Alan','Andrés','Ariadna','Bautista','CAROLINA','CESAR','David','Diego','Dolores','DYLAN','ELIANA','Emanuel','Fabián','Facundo','Facundo','FEDERICO','FEDERICO','GONZALO','Gregorio','Ignacio','Jonathan','Jonathan','Jorge','JOSE','JUAN','Juan','Juan','Julian','Julieta','LAUTARO','Leonel','LUIS','Luis','Marcos','María','MATEO','Matias','Nicolás','NICOLÁS','Noelia','Pablo','Priscila','TOMAS','Tomás','Ulises','Yanina']
notas_final=[]
promedio=0
i=0
for elem in notas1:
    suma=notas1[i]+notas2[i]
    notas_final.append(suma)
    promedio=promedio+notas_final[i]
    i=i+1

dicc={}
ii=0
for elem in Nom:
    dicc[Nom[ii]]=notas_final[ii]
    ii=ii+1

cant=len(notas_final)
promedio = promedio/cant
#print(promedio)
#print(dicc)

for elem in dicc:
    if (dicc[elem] < promedio):
        print(elem)