import numpy as np
def sigmoid(z):
    """The sigmoid function."""
    return 1.0/(1.0+np.exp(-z))
sizes = [4,2,3]
a = np.random.randn(sizes[0],1)
biases = [np.random.randn(y, 1) for y in sizes[1:]]
weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]
for b, w in zip(biases, weights):
    a = sigmoid(np.dot(w, a)+b)    
    print (a)

