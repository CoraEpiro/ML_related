from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

iris = load_iris()

df = pd.DataFrame(iris.data)

df['Target'] = iris.target.astype(float)

Xs, Ys = df.drop(['Target'], axis = 1), df['Target']

X_train, X_test, Y_train, Y_test = train_test_split(Xs,
                                                    Ys,
                                                    train_size=0.8,
                                                    random_state=42)

grid_search = GridSearchCV( 
    estimator=KNeighborsClassifier(),
    param_grid={'n_neighbors': np.arange(1, 10)},
    scoring='accuracy',
    cv=5
)

grid_search.fit(X_train, Y_train)

Y_pred = grid_search.best_estimator_.predict(X_test)

print('Best K:', grid_search.best_params_['n_neighbors'])
print('Best Accuracy:', accuracy_score(Y_test, Y_pred))