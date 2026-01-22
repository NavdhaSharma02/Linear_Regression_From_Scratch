# The given X and Y are the training data.
X = [1, 2, 3, 4, 5]
Y = [2, 4, 6, 8, 10]

# Given parameters
m = 0 # slope of the line
b = 0  # y-intercept of the line
learning_rate = 0.01 # size of step
epochs = 1000 # how many times we train
n = len(X) # number of data points (from data we can see here 5)

#  training loop
for _ in range(epochs):
    y_pred = [(m*x + b) for x in X]

    # gradient descent - move little bit in right direction repeatedly
    
    # which directionshould m to move to reduce error
    dm = (-2/n) * sum(x*(y - y_hat) for x, y, y_hat in zip(X, Y, y_pred))
    # which direction should b move to reduce errors
    db = (-2/n) * sum(y - y_hat for y, y_hat in zip(Y, y_pred))

    # update parameters
    m = m - learning_rate * dm
    b = b - learning_rate * db

print("Slope (m):", m)
print("Intercept (b):", b)
