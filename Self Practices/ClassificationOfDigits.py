from sklearn.datasets import load_digits
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_validate
import numpy as np


X_digits, Y_digits = load_digits(return_X_y=True)

y_1 = (Y_digits == 1) # Just check that 1s or not 1s for simplicity purposes


X_train, X_test, Y_train, Y_test = train_test_split(X_digits,
                                                    Y_digits,
                                                    test_size=0.8,
                                                    random_state=42,
                                                    stratify=y_1)

stratify = StratifiedKFold(n_splits=5)

Ks = range(1, 10)

train_scores = []
val_scores = []

for k in Ks:
    model = KNeighborsClassifier(n_neighbors=k)
    scores = cross_validate(model,
                            X_train,
                            Y_train,
                            cv=stratify,
                            return_train_score=True)
    
    train_cv_score = np.mean(scores['train_score'])
    val_cv_score = np.mean(scores['test_score'])
    
    train_scores.append(train_cv_score)
    val_scores.append(val_cv_score)
    

print("Best Validation Score:", max(val_scores))
print("Corresponding Train Score:", train_scores[val_scores.index(max(val_scores))])

best_k = val_scores.index(max(val_scores)) + 1
print("Best K Value:", best_k)

model = KNeighborsClassifier(n_neighbors=best_k)
scores = cross_validate(model,
                             X_test,
                             Y_test,
                             cv=stratify)

test_score = np.mean(scores['test_score'])

print("Test Score:", test_score)