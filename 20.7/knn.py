import math
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

irisData = load_iris()

X = irisData.data
y = irisData.target

# print(X)
#print(y)

X_train,X_test,y_train,y_test=train_test_split(
    X,y,
    test_size=0.2,
    random_state=42
)
k=3
prediction=[]

def euclidean_distance(point_x,point_y):
    distance=0
    for i in range(len(point_x)):
        distance+=(point_x[i]-point_y[i])**2
        
    return math.sqrt(distance)



def predict(x_train,y_train,test_point,k):
    distances=[]
    for i in range(len(x_train)):
        dist=euclidean_distance(test_point,x_train[i])
        distances.append((dist,y_train[i]))
    distances.sort(key=lambda x:x[0])
    neighbours=distances[:k]
    votes={}
    for _,label in neighbours:
        if label in votes:
            votes[label]+=1
        else:
            votes[label]=1
    prediction=max(votes,key=votes.get)
    return prediction
for test_point in X_test:
    prediction.append(predict(X_train,y_train,test_point,k))
# print(X_train.shape)
# print(X_test.shape)
# print(y_train.shape)
# print(y_test.shape)
# print(irisData.feature_names)
accurace=accuracy_score(y_test,prediction)
cm=confusion_matrix(y_test)
print(prediction)