import numpy as np
import random

def CreaTablero():
    nf = 10
    nc = 8
    nm = 8
    # Matriz pulsado
    # rellenar matriz de 0 
    p = np.zeros((nf, nc))
    # Matriz mina
    m = np.zeros((nf, nc))
    M2 = np.zeros((nf+2, nc+2))
    # Num minas
    a = np.zeros((nf, nc))
    # Pos de las minas
    pos = []
    for i in range(nm):
        f = random.randint(0, nf-1)
        c = random.randint(0, nc-1)
        m[f,c] = 1 
        M2[f+1,c+1] = 1 
        pos.append(tuple([f,c]))
        #pos.append(np.array(f,c))
    return(p,m,a,M2)
    
ct = CreaTablero()
p  = ct[0]
m = ct[1]
a = ct[2]
M2 = ct[3]

print("m \n",m)

print("M2 \n",M2)




# Recorro filas
for i in range(1,M2.shape[0]-1): # Recorro de la 1 a la 10
    # Recorro cols
    for j in range(1,M2.shape[1]-1):
        cont  = 0
        print('Posición: ',i,j)
        print('P1, arriba izq',M2[i-1,j-1])
        if M2[i-1,j-1] == 1 :
            cont +=1
        print('P2, arriba',M2[i-1,j])
        if M2[i-1,j] == 1:
            cont +=1
        print('P3, arriba der',M2[i-1,j+1])
        if M2[i-1,j+1] == 1:
            cont +=1
        print('P4,  izq', M2[i,j-1])
        if  M2[i,j-1] == 1:
            cont +=1
        print('P5, der ',M2[i,j+1])
        if M2[i,j+1] == 1:
            cont += 1
        print('P6, abajo izq',M2[i+1,j-1] )
        if M2[i+1,j-1] == 1:
            cont +=1
        print('P7, abajo',M2[i+1,j])
        if M2[i+1,j] == 1:
            cont +=1
        print('P8, abajo der',M2[i+1,j+1])
        if M2[i+1,j+1] == 1:
            cont +=1
        print("Contador para la posición: ",str(cont))


# Recorro filas
for i in range(1,M2.shape[0]-1): # Recorro de la 1 a la 10
    # Recorro cols
    for j in range(1,M2.shape[1]-1): # Recorro de la 1 a la 8
        cont = 0 
        if M2[i-1,j-1] == 1: # Pos1
            cont +=1
        if M2[i-1,j] == 1: # Pos2
            cont +=1
        if M2[i-1,j+1] == 1: # Pos3 
            cont +=1
        if M2[i,j-1] == 1: # Pos4
            cont +=1
        if M2[i,j+1] == 1: # Pos5
            cont +=1
        if M2[i+1,j-1] == 1: # Pos 6
            cont +=1
        if M2[i+1,j] == 1: # Pos 7
            cont +=1
        if M2[i+1,j+1] == 1: # Pos 7
            cont +=1
        if M2[i,j] :
            pass
        a[i-1,j-1] = cont
        print("Hay "+str(cont)+" minas alrededor de la posición "+str(i)+','+str(j))
        
print("a: \n",a)
        
        