import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

"""print("Numpy version:", np.__version__ )
print(dir(np))
"""
"""python_list = [1, 2, 3, 4, 5]

print("Type: ", type(python_list)) #<class 'list'>

print(python_list) # [1, 2, 3, 4, 5]

two_dimentional_list = [[1, 2, 3], [4, 5, 6]]
print(two_dimentional_list) # [[1, 2, 3], [4, 5, 6]]


#creating numpy numerical python array from python list
numpy_array_from_list = np.array(python_list)
print(type(numpy_array_from_list)) # <class 'numpy.ndarray'>
print(numpy_array_from_list) # [1 2 3 4 5]

#Creacion de matrices numpy flotantes
python_list = [1,2,3,4,5]
numpy_list_f = np.array(python_list, dtype='float') 
print(numpy_list_f) # [1. 2. 3. 4. 5.]

#Creacion de matrices booleanas 

python_list_bool = [1,0,1,0,0]
numpy_bool = np.array (python_list_bool, dtype='bool')
print(numpy_bool) # [ True False  True False False]

#Creacion de matriz multidimensional
two_dimesnional_list = [[1,2,3],[4,5,6]] 
numpy_multidimensional = np.array(two_dimesnional_list)
print(numpy_multidimensional) # [[1 2 3] [4 5 6]]

#Podemos reconvertir una matriz numpy en una lista otra vez 
np_to_list = numpy_multidimensional.tolist()
print(type(np_to_list)) # <class 'list'>
print(np_to_list) # [[1, 2, 3], [4, 5, 6]]

#Usando shape obtenemos una tupla que indica las filas y columnas de nuestra matriz 
nums = np.array([[1,2,3],[4,5,6]])
print(nums.shape) # (2, 3)
nums2= np.array([[1,2,3],[4,5,6],[7,8,9]])
print(nums2.shape) # (3, 3)
nums3 = np.array ([1,2,3,4,5])
print(nums3.shape) # (5,)

#En numpy para saber la cantidad de elementos de una lista de matricez usamos size 
numpy_size1 = np.array([1,2,3,4,5])
numpy_size2 = np.array([[1,2,3],[4,5,6]])
print(numpy_size1.size) # 5
print(numpy_size2.size) # 6

#Obtener elementos de una matriz numpy 
matriz_tres_x_tres = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matriz_tres_x_tres[0,0]) # 1
print(matriz_tres_x_tres[0]) # [1 2 3]
print(matriz_tres_x_tres[:,0]) # [1 4 7]

#Cortar una matriz en Numpy 
print("Matriz cortada en 2x2: " , matriz_tres_x_tres[0:2,0:2]) # [[1 2] [4 5]]

#Invertir filas y columnas de una matriz
print("Matriz invertida: ", matriz_tres_x_tres[::-1, ::-1]) # [[9 8 7] [6 5 4] [3 2 1]]

#Como llenar de valroes nuevos
print("Matriz original: ", matriz_tres_x_tres) # [[1 2 3] [4 5 6] [7 8 9]]
matriz_tres_x_tres [0:2, 0:2] = 0
print("Matriz con valores cambiados: ", matriz_tres_x_tres) # [[0 0 3] [0 0 6] [7 8 9]]

#Llenar de ceros
matriz_tres_X_tres = np.zeros ((3,3), dtype='int', order='C') #Order C es por filas y F es por columnas
print("Matriz de ceros: ", matriz_tres_X_tres) # [[0 0 0] [0 0 0] [0 0 0]]

#Cambiar forma
matriz_tres_X_tres = np.array([[1,2,3],[4,5,6],[7,8,9]])
matriz_cambiada_forma = matriz_tres_X_tres.reshape(1,9)
print("Matriz original: ", matriz_tres_X_tres) # [[1 2 3] [4 5 6] [7 8 9]]
print("Matriz con forma cambiada: ", matriz_cambiada_forma) # [[1 2 3 4 5 6 7 8 9]]

#Generacion de numeros aleatorios
numeros_aleatorios = np.random.randint(0,11, size= (3,3))   
print("Matriz de numeros aleatorios: ", numeros_aleatorios) # [[ 0  9  3] [ 5  1 10] [ 2  4  6]]
"""
#Generacion con distribucion normal
numeros_aleatorios_normal = np.random.normal(50,50, size = 80) # 0 es el centro y 1 la desviacion 
print("Matriz de numeros aleatorios con distribucion normal: ", numeros_aleatorios_normal) # [[-0.123  0.456 -1.234] [ 0.789 -0.567  1.890] [ 0.345 -0.678  0.123]]
"""
sns.set() 
#sns.set() es para configurar el estilo de los gráficos de seaborn, que es una biblioteca de visualización de datos basada en matplotlib.
#Al llamar a sns.set(), se aplican automáticamente estilos y configuraciones predeterminadas a los gráficos generados con matplotlib, lo que mejora la apariencia visual de los gráficos y hace que se vean más atractivos y profesionales.
plt.hist (numeros_aleatorios_normal, bins=50, color='blue')
#Esto lo que hizo fue crear un histograma de los numeros aleatorios generados con distribucion normal, con 50 bins y color azul
plt.show()
"""
#Crear numero espaciados
numeros = np.arange (0, 10, 2) # [0 2 4 6 8]
print("Numeros espaciados: ", numeros)

#Crear numero espaciados con linspace
numeros_linspace = np.linspace(0, 10, 5) # [0. 2.5 5. 7.5 10.]
print("Numeros espaciados con linspace: ", numeros_linspace)
#Estadisticas en numpy 
two_dimentional_array = np.array([[1,2,3],[4,5,6]])
print("Array bidimensional: ", two_dimentional_array)
print("min: ", np.min(two_dimentional_array)) # 1
print("max: ", np.max(two_dimentional_array)) # 6
print("mean: ", np.mean(two_dimentional_array)) # 3.5
print("median: ", np.median(two_dimentional_array)) # 3.5
print("std: ", np.std(two_dimentional_array)) # 1.707825127659933

print("column with min: ", np.amin(two_dimentional_array, axis=0)) # [0 0 0]
print("row with min: ", np.amin(two_dimentional_array, axis=1)) # [0 0]
print("column with max: ", np.amax(two_dimentional_array, axis=0)) # [1 1 1]
print("row with max: ", np.amax(two_dimentional_array, axis=1)) # [2 2]

