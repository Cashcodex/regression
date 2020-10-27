import numpy as np
import kmeans as ml1
import svgutils.compose as sc 
import matplotlib.pyplot as plt
from random import random
from IPython.display import SVG
import imageio
from scipy import misc
import glob


def createData(dims, *positional_parameters, **keyword_parameters):
	if ('means' in keyword_parameters):
		return keyword_parameters['means']+np.random.randn(*dims)
	else:
		return np.random.randn(*dims)

def clustering_2D_example(n,k):
	X=createData((n,2))

	meaner=ml1.kmeans(X,k)
	meaner.run2()
	for i in range(k):
		plt.plot(X[meaner.labels==i][:,0],X[meaner.labels==i][:,1],marker='o', linestyle='', color=(random(),random(),random()), label='Datenpunkte')
	plt.plot(meaner.centers[:,0],meaner.centers[:,1],marker='x', linestyle='', color='r', label='Datenpunkte')
	plt.show()

def clustering_2D_example2(n,k):
	X=createData((n,2))

def clustering_2D 

	centers,labels=ml1.kmeans2(X,k)
	for i in range(k):
		print("i: ",i)
		plt.plot(X[labels==i][:,0],X[labels==i][:,1],marker='o', linestyle='', color=(random(),random(),random()), label='Datenpunkte')
		
	plt.plot(centers[:,0],centers[:,1],marker='x', linestyle='', color='r', label='Datenpunkte')
	plt.show()
	
def clustering_speed_1(n,k):
	X=createData((n,2))

	meaner=ml1.kmeans(X,k)
	meaner.run()

def clustering_speed_2(n,k):
	X=createData((n,2))

	meaner=ml1.kmeans(X,k)
	meaner.run2()
	
def clustering_speed_3(n,k):
	X=createData((n,2))
	meaner=ml1.k_means(X,k,50)

	
def loadData():
	sc.Figure("16cm", "16cm",
    sc.Panel(sc.SVG("./Price/monogram.price.2.svg"))).save("compose.svg")
	print(np.array(sc.SVG("./Price/monogram.price.2.svg")))
	SVG('compose.svg')
	print("Success")

	image1 = imageio.imread("/Users/kashefkarim/desktop/ML1 Algo/1.png")
	image2 = imageio.imread("/Users/kashefkarim/desktop/ML1 Algo/2.png")
	X=np.ones(shape=(2,1000*1000*4))
	X[0]=image1.flatten()
	X[1]=image2.flatten()
	print(image1.flatten())
	print(image3.flatten())
	print(image2.shape)
	meaner = ml1.kmeans(X, 2)
	meaner.run()

 	
    
#from timeit import timeit
#setup = 'from __main__ import clustering_speed_2,clustering_speed_3 ; import numpy as np'
#num = 5
#t1 = timeit('clustering_speed_3(100000,5)', setup=setup, number=num)
#t2 = timeit('clustering_speed_2(100000,5)', setup=setup, number=num)
#print('Average Algorithm 1: {:0.1f} \n Average Algorithm 2: {:0.1f}'.format(t1/num,t2/num))
	
#clustering_2D_example(60,3)
#clustering_2D_example(1,1)

loadData()
