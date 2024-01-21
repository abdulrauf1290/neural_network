# -*- coding: utf-8 -*-
"""Neural_network.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mhHyCKZwATbjtqAX45it75keG0HvIeiw

## ReLU Activation
"""

import numpy as np

import nnfs
from nnfs.datasets import spiral_data
np.random.seed(0)

X = [[1,2,3,2.5],
     [2.0,5.0,-1.0,2.0],
     [-1.5,2.7,3.3,-0.8]]


X,y = spiral_data(100, 3)

class Layer_Dense:
  def __init__(self,n_inputs,n_neurons):
    self.weights = 0.10 * np.random.randn(n_inputs,n_neurons)
    self.biases =  np.zeros((1,n_neurons))
  def forward(self,inputs):
    self.output = np.dot(inputs, self.weights) + self.biases


class Activation_ReLU:
  def forward(self,inputs):
    self.output = np.maximum(0, inputs)


layer1 = Layer_Dense(2,5)
activation1 = Activation_ReLU()
#layer2 = Layer_Dense(5,2)      # layer 2 take layer1 output as a input


#print(layer1.output)
layer1.forward(X)
activation1.forward(layer1.output)
#print(layer1.output)                   # this may contain the negative values
print(activation1.output)               # this will make the negative values to 0 and positive values as it is.
#layer2.forward(layer1.output)
#print(layer2.output)



"""## Exponential"""

## Exponential

import math

layer_outputs = [4.8, 1.12, 2.385]

#E = 2.71828182846
E = math.e

exp_values = []

for output in layer_outputs:
  exp_values.append(E**output)

print(exp_values)


norm_base = sum(exp_values)
norm_values = []

for value in exp_values:
  norm_values.append(value / norm_base)

print(norm_values)
print(sum(norm_values))

import math
import numpy as np

layer_outputs = [4.8, 1.12, 2.385]

exp_values = np.exp(layer_outputs)

norm_values = exp_values / np.sum(exp_values)

print(norm_values)
print(sum(norm_values))



import math
import numpy as np
import nnfs

layer_outputs = [[4.8,1.21,2.385],
                 [8.9,-1.81,0.2],
                 [1.41,1.051,0.026]]


exp_values = np.exp(layer_outputs)

#print(np.sum(layer_outputs,axis=1,keepdims=True))     # axis=1 is for rows, axis=0 is for column and by default it is None

norm_values = exp_values / np.sum(exp_values,axis=1,keepdims=True)

print(norm_values)

"""## Softmax Activation"""

import numpy as np

import nnfs
from nnfs.datasets import spiral_data
np.random.seed(0)

X,y = spiral_data(100, 3)

class Layer_Dense:
  def __init__(self,n_inputs,n_neurons):
    self.weights = 0.10 * np.random.randn(n_inputs,n_neurons)
    self.biases =  np.zeros((1,n_neurons))
  def forward(self,inputs):
    self.output = np.dot(inputs, self.weights) + self.biases


class Activation_ReLU:
  def forward(self,inputs):
    self.output = np.maximum(0, inputs)

class Activation_Softmax:
  def forward(self, inputs):
    exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))             # it will normalise the values as the exponential make the value to be in between 0 and 1.
    probablities = exp_values / np.sum(exp_values,axis=1, keepdims=True)
    self.output = probablities

X,y =spiral_data(samples =100, classes=3)

dense1 = Layer_Dense(2,3)
activation1 = Activation_ReLU()

dense2 = Layer_Dense(3,3)
activation2 = Activation_Softmax()

dense1.forward(X)
activation1.forward(dense1.output)

dense2.forward(activation1.output)
activation2.forward(dense2.output)
print(activation2.output[:5])



"""## Loss with categorical cross entropy"""

import numpy as np
import math

softmax_output = [0.7,0.1,0.2]
target_output = [1,0,0]


loss = -(math.log(softmax_output[0])* target_output[0] +
         math.log(softmax_output[1])* target_output[1]+
         math.log(softmax_output[2])* target_output[2])

print(loss)

print(-math.log(0.7))
print(-math.log(0.5))                              # as the value in the log increases the overall value decreases. confidence belongs to [0,1] and loss belongs to (-inf,0].



import numpy as np

softmax_outputs = np.array([[0.7,0.1,0.2],
                            [0.1,0.5,0.4],
                            [0.02,0.9,0.08]])

class_targets = [0,1,1]

print(softmax_outputs[[0,-1,-2], class_targets])

class Loss:
  def calculate(self,output,y):
    sample_losses = self.forward(output,y)
    data_loss = np.mean(sample_losses)
    return data_loss

class Loss_CategoricalCrossEntropy(Loss):
  def forward(self,y_pred, y_true):
    samples = len(y_pred)
    y_pred_clipped = np.clip(y_pred, 1e-7 , 1-1e-7)


    if len(y_true.shape) == 1:
      correct_confidences = y_pred_clipped[range(samples), y_true]
    elif len(y_true.shape) == 2:
      correct_confidences = np.sum(y_pred_clipped*y_true, axis=1)

    negative_log_likelihoods = -np.log(correct_confidences)
    return negative_log_likelihoods


loss_function = Loss_CategoricalCrossEntropy()
loss = loss_function.calculate(activation2.output,y)

print("Loss :" , loss)

