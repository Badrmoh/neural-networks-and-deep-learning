import mnist_loader

"""
import sys
print (sys.version_info[0])
"""

training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

import network 
net = network.Network([784, 10])

net.SGD(training_data, 30, 10, 3.0, test_data=test_data)

