import numpy as np

# Activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Inputs and outputs
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
outputs = np.array([[0], [1], [1], [0]])

# Initialize weights
weights = np.random.rand(2, 1)
bias = np.random.rand(1)
learning_rate = 0.1

# Train the network
for epoch in range(10000):
    # Forward propagation
    inputs_weighted = np.dot(inputs, weights) + bias
    activated_output = sigmoid(inputs_weighted)

    # Backpropagation
    error = outputs - activated_output
    adjustments = error * sigmoid_derivative(activated_output)
    weights += np.dot(inputs.T, adjustments) * learning_rate
    bias += np.sum(adjustments) * learning_rate

print("Trained weights:\n", weights)
print("Trained bias:\n", bias)
