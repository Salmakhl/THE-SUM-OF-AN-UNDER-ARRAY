n=int(input("type the number of thr list: "))
list=[]
somme=0
sommemax=0
for i in range(n):
    b=int(input("type a nbre : "))
    list.append(b)

tableau_indice = [] #Array that has  the hints of the under array numbre 

sous_tableau = [] #the under array


for i in range(n):
    somme=somme+ list[i]
    if somme>=sommemax:
        sommemax=somme
       

        tableau_indice.append(i)  #the hints
    if somme<0:
        somme=0
        sous_tableau.clear()
        tableau_indice.clear()   #if the addition equal >0 the under array become empty 


for i in range(tableau_indice[0], tableau_indice[-1] + 1) : 
    sous_tableau.append(list[i])        
print(sommemax)
print(sous_tableau)

