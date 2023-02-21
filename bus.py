import numpy as np
import random



mina = "*"
no_pulsado = "."
pulsado = "-"
tablero_ini = []
WIN = False
GAME_OVER = False


def CreaTablero():
    global tablero_ini
    global nf
    global nc
    tablero_ini = []
    nf = 10
    nc = 8
    nm = 8
    # Matriz pulsado
    # rellenar matriz de 0 
    p = np.zeros((nf, nc))
    
    # Tablero inicial
    for fila in range(nf):
        tablero_ini.append([])
        for columna in range(nc):
                tablero_ini[fila].append(no_pulsado)
    
    
    
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
    return(p,m,a,M2,tablero_ini)
    
ct = CreaTablero()
p  = ct[0]
m = ct[1]
a = ct[2]
M2 = ct[3]
tablero_inicial = ct[4]

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
        #print("Hay "+str(cont)+" minas alrededor de la posición "+str(i)+','+str(j))

def movimiento():
    '''
    Función que pide una fila y col para hacer movimiento
    '''
    global fila
    global col 
    # Selección de fila
    
    while True:

        try:
            print("-"*40)
            fila = int(input("Indique la fila: "))
            fila = fila-1 # Resto 1 por los índices en python
            if  fila < 0 or fila > 9:
                raise ValueError
                
            break
        except ValueError:
            print("Introduzca una fila entre 1 y 10")
    # Selección de columna
    while True:
        try:
            col =  int(input("Indique la columna: "))
            print("-"*40)
            col = col-1 # Resto 1 por los índices en python
            if  col < 0 or col > 7 :
                raise ValueError
                
            break
        except ValueError:
            print("Introduzca una columna entre 1 y 8")



num = '------'+' 1 '+'-'+' 2 '+'-'+' 3 '+'-' + ' 4 '+'-'+' 5 '+'-'+' 6 '+'-'+' 7 '  + '-'+ ' 8'


print("Comienzo del juego: \n")
print(num)
cuento_filas = 1
for i in tablero_inicial: 
    if cuento_filas <10:
        print(cuento_filas,'--',np.array(i))
        cuento_filas +=1
    else:
        print(cuento_filas,'-',np.array(i))
        cuento_filas +=1




print("-"*30)
contador_partidas= 0 

while not GAME_OVER: # Mientras que no hayamos perdido
    
    ###### ES EL INICIO DE LA PARTIDA #######
    if contador_partidas == 0:
        print("Empezamos a jugar, partida: ",str(contador_partidas+1) )
        movimiento()
        print("Movimiento: ", str(fila+1),',',str(col+1))
        p[fila,col] = 1 # Modifico p 
        if a[fila,col] != 0: # Es decir, que tiene o mina o nº
            tablero_inicial[fila][col]  = int(a[fila,col])
        if a[fila,col] == 0:
            tablero_inicial[fila][col] = pulsado # Tablero ini es una lista
        # print('Tablero de juego: \n')
        print(num)
        cuento_filas = 1
        for i in tablero_inicial: 
            if cuento_filas <10:
                print(cuento_filas,'--',np.array(i))
                cuento_filas +=1
            else:
                print(cuento_filas,'-',np.array(i))
                cuento_filas +=1
        contador_partidas +=1
        print("-"*40)
        
        
    ####### A PARTIR DE LA SEGUNDA JUGADA #########
    else: 
        movimiento()
        print("Partida ", contador_partidas,"\nMovimiento: ", str(fila+1),',',str(col+1))
        
        
        
        
        
        if p[fila,col] != 0 :
            print('Esa casilla ya ha sido pulsada, pruebe de nuevo: ')
            #movimiento()

        elif m[fila,col] == 1:
            print("Ha perdido, había una mina.")
            tablero_inicial[fila][col] = mina
            GAME_OVER = True
            # print('Tablero de juego: \n')
            cuento_filas = 1
            for i in tablero_inicial: 
                if cuento_filas <10:
                    print(cuento_filas,'--',np.array(i))
                    cuento_filas +=1
                else:
                    print(cuento_filas,'-',np.array(i))
                    cuento_filas +=1
            print("-"*40)
            print("Duración del juego: "+str(contador_partidas +1)+" partidas.")

            break
        
        
        
        
        else:
            p[fila,col] = 1 # Modifico p 
            if a[fila,col] != 0: # Es decir, que tiene o mina o nº
                tablero_inicial[fila][col]  = int(a[fila,col])
            if a[fila,col] == 0:
                tablero_inicial[fila][col] = pulsado # Tablero ini es una lista
            # print('Tablero de juego: \n')
            print(num)
            cuento_filas = 1
            for i in tablero_inicial: 
                if cuento_filas <10:
                    print(cuento_filas,'--',np.array(i))
                    cuento_filas +=1
                else:
                    print(cuento_filas,'-',np.array(i))
                    cuento_filas +=1

            contador_partidas +=1
            #movimiento()