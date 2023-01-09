
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets.samples_generator import make_blobs

#read data from file
data = np.genfromtxt('data.txt', delimiter=',')

#print data
print(data) 