# Ejercicio 1

import numpy as np
import matplotlib.pylab as plt


# Use esta funcion que recibe un valor x y retorna un valor f(x) donde f es la forma funcional que debe seguir su distribucion. 
def mifun(x):
    x_0 = 3.0
    a = 0.01
    return np.exp(-(x**2))/((x-x_0)**2 + a**2)

# Dentro de una funcion que reciba como parametros el numero de pasos y el sigma de la distribucion gausiana que va a usar para calcular el paso de su caminata, implemente el algortimo de Metropolis-Hastings. Finalmente, haga un histograma de los datos obtenidos y grafique en la misma grafica, la funcion de distribucion de probabilidad fx (Ojo, aca debe normalizar). Guarde la grafica sin mostrarla en un pdf. Use plt.savefig("histograma_"+str(sigma)+"_"+str(pasos)+".pdf"), donde sigma y pasos son los parametros que recibe la funcion.

def algoritmoMH(n,sigma):
    x = np.zeros(n)
    x[0]=0
    for i in range(0,n-1):
        x_new = x[i]+np.random.uniform(-sigma,sigma)
        a = mifun(x_new)/mifun(x[i])
        if ( np.random.rand() < min(1,a) ):
            x[i+1] = x_new
        else:
            x[i+1] = x[i]
    return x

# Cuando haya verificado que su codigo funciona, use los siguientes parametros:
# sigma = 5, pasos =100000 
# sigma = 0.2, pasos =100000 
# sigma = 0.01, pasos =100000 
# sigma = 0.1, pasos =1000 
# sigma = 0.1, pasos =100000 
# este puede ser muy demorado dependiendo del computador: sigma = 0.1, pasos =500000 

# Al ejecutar el codigo, este debe generar 6 (o 5) graficas .pdf una para cada vez que se llama a la funcion.
def crearGraf(n,sigma):
    plt.figure()
    plt.hist(algoritmoMH(n,sigma),density=True,bins=30)
    x_f = np.linspace(-2,4,100)
    plt.plot(x_f,mifun(x_f))
    plt.savefig("histograma_"+str(sigma)+"_"+str(n)+".pdf")
    plt.close()
    
    
crearGraf(100000,5)
crearGraf(100000,0.2)
crearGraf(100000,0.01)
crearGraf(1000,0.1)
crearGraf(100000,0.1)
crearGraf(500000,0.1)
