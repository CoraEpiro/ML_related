from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_digits
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
import numpy as np

# Load digits
digits = load_digits()
X_digits = digits.data
Y_digits = digits.target

# Train & Test split
X_train, X_test, Y_train, Y_test = train_test_split(X_digits,
                                                    Y_digits,
                                                    test_size=0.8,
                                                    random_state=42,
                                                    stratify=Y_digits)

# Pipeline finds best K value with using accuracy as a score metric
pipeline = Pipeline(steps=[
    ('grid_search', GridSearchCV(
        estimator = KNeighborsClassifier(),
        param_grid = {'n_neighbors' : np.arange(1, 10)},
        scoring = 'accuracy',
        cv = 5
        ))
    ])

pipeline.fit(X_train, Y_train)

best_k = pipeline.named_steps['grid_search'].best_params_['n_neighbors']
best_estimator = pipeline.named_steps['grid_search'].best_estimator_
best_val_score = pipeline.named_steps['grid_search'].best_score_
    
# Print some data
accuracy = accuracy_score(Y_test, best_estimator.predict(X_test))

print("Best Validation Score:", best_val_score)
print("Best K Value:", best_k)
print("Best Estimator Accuracy:", accuracy)