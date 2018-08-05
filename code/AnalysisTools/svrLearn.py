import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt
import pandas as pd

# #############################################################################
# Generate sample data
X = np.sort(5 * np.random.rand(40), axis=0)
#X2 = np.sort(5 * np.random.rand(40), axis=0)
#X3 = np.sort(-8 * np.random.rand(40), axis=0)
y = np.sin(X)#.ravel()+X2-np.cos(X3).ravel()

# #############################################################################
# Add noise to targets
y[::5] += 3 * (0.5 - np.random.rand(8))

# #############################################################################
# Fit regression model
svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
svr_lin = SVR(kernel='linear', C=1e3)
svr_poly = SVR(kernel='poly', C=1e3, degree=2)

x = pd.DataFrame(data={'X':X})#,'X2':X2,'X3':X3})

y_rbf = svr_rbf.fit(x, y).predict(x)
y_lin = svr_lin.fit(x, y).predict(x)
y_poly = svr_poly.fit(x, y).predict(x)

# #############################################################################
# Look at the results
lw = 2
plt.scatter(X, y, color='darkorange', label='data')
#plt.scatter(X2, y, color='blue', label='data')
plt.plot(X, y_rbf, color='navy', lw=lw, label='RBF model')
plt.plot(X, y_lin, color='c', lw=lw, label='Linear model')
plt.plot(X, y_poly, color='cornflowerblue', lw=lw, label='Polynomial model')
plt.xlabel('data')
plt.ylabel('target')
plt.title('Support Vector Regression')
plt.legend()
plt.show()
