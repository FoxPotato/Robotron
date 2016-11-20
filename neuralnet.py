import numpy as np
import matplotlib.pyplot as plt

class NeuralNetwork(object):
    def __init__(self, input_layer_size, hidden_layer_size, num_labels, training_rate=0.1, reg_factor=1.0):
        self.input_layer_size = input_layer_size
        self.hidden_layer_size = hidden_layer_size
        self.num_labels = num_labels
        self.training_rate = training_rate
        self.reg_factor = reg_factor

        # Randomly initialize weights
        self.theta1 = 0.5 * (np.random.rand(hidden_layer_size, input_layer_size + 1) - 0.5)
        self.theta2 = 0.5 * (np.random.rand(num_labels, hidden_layer_size + 1) - 0.5)

    def train(self, X_train, y_train, X_cv, y_cv, num_iterations=50):
        train_costs = np.zeros(num_iterations)
        cv_costs = np.zeros(num_iterations)
        
        for i in range(num_iterations):
            (J, theta1_grad, theta2_grad) = self.cost(X_train, y_train)

            train_costs[i] = J
            cv_costs[i] = self.cost(X_cv, y_cv)[0]

            self.theta1 -= self.training_rate * theta1_grad
            self.theta2 -= self.training_rate * theta2_grad

        return (train_costs, cv_costs)

    def cost(self, X, y):
        m = float(len(y))

        # Convert labels to binary array
        c = np.arange(self.num_labels)
        y_temp = np.zeros(( m, self.num_labels) )
        
        for c in range(0, self.num_labels):
            y_temp[:,c] = np.where(y==c, 1, 0)
        
        y = y_temp

        # Compute activations and hypothesis using forward propagation
        (a1, z2, a2, z3, h) = self.feedforward(X)

        # Compute regularization terms for theta1 and theta2, skipping the bias weights
        theta1_reg = np.append(np.zeros( (self.hidden_layer_size, 1) ), self.theta1[:, 1:self.input_layer_size + 1], 1)
        theta1_reg = np.power(theta1_reg, 2)
        theta2_reg = np.append(np.zeros( (self.num_labels, 1) ), self.theta2[:, 1:self.hidden_layer_size + 1], 1)
        theta2_reg = np.power(theta2_reg, 2)

        # Compute regularized logistic cost
        J = np.sum( np.sum( -y * np.log(h) - (1 - y) * np.log(1 - h) ) ) / m + self.reg_factor / (2 * m) * ( np.sum(theta1_reg) + np.sum(theta1_reg) )

        # Compute gradients of theta1 and theta2 using backpropagation
        delta3 = h - y;
        delta2 = np.dot(delta3, self.theta2) * np.append(np.ones( (m, 1) ), self.sigmoid_gradient(z2), 1)
        delta2 = delta2[:, 1:self.hidden_layer_size + 1]

        theta1_grad_reg = self.reg_factor / m * self.theta1
        theta1_grad_reg = np.append(np.zeros( (self.hidden_layer_size, 1) ), theta1_grad_reg[:, 1:self.input_layer_size + 1], 1)
        theta2_grad_reg = self.reg_factor / m * self.theta2
        theta2_grad_reg = np.append(np.zeros( (self.num_labels, 1) ), theta2_grad_reg[:, 1:self.hidden_layer_size + 1], 1)

        theta1_grad = np.dot(delta2.T, a1) / m + theta1_grad_reg
        theta2_grad = np.dot(delta3.T, a2) / m + theta2_grad_reg

        return (J, theta1_grad, theta2_grad)

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def sigmoid_gradient(self, z):
        g = self.sigmoid(z)
        return g * (1 - g)

    def feedforward(self, X):
        m = len(X[:,0])
        
        a1 = np.append(np.ones( (m, 1) ), X, 1)
        z2 = np.dot(a1, self.theta1.T)
        a2 = np.append(np.ones( (m, 1) ), self.sigmoid(z2), 1)
        z3 = np.dot(a2, self.theta2.T)
        h = self.sigmoid(z3)
        
        return (a1, z2, a2, z3, h)

# Load dataset
data = np.loadtxt(open("resource/iris.data", 'rb'), delimiter=',')
X = data[:,0:4]
y = data[:,4].astype(int)

#X = ( X - X.mean() ) / np.std(X)   # Standardize features
X = (X - X.min(0)) / (X.max(0) - X.min(0))  # Normalize features

# Split datasets for cross-validation and testing
X_train = X[0:90,:]
y_train = y[0:90]

X_cv = X[90:120,:]
y_cv = y[90:120]

X_test = X[120:150,:]
y_test = y[120:150]

# Initialize the network
nn = NeuralNetwork(4, 5, 3, training_rate=0.2, reg_factor=0)

# Train the network
costs = nn.train(X_train, y_train, X_cv, y_cv, 5000)

# Print cost of the training, cross-validation, and test sets
print(nn.cost(X_train, y_train)[0])
print(nn.cost(X_cv, y_cv)[0])
print(nn.cost(X_test, y_test)[0])

# Plot cost graph
plt.plot(costs[0], "b")
plt.plot(costs[1], "g")

plt.xlabel("Iterations")
plt.ylabel("Cost")

plt.show()
