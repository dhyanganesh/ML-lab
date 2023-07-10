import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,f1_score

data=pd.read_csv("titanic_train.csv")
data.tail(5)

data["Embarked"]=data["Embarked"].factorize()[0]
data=data[['Survived','Pclass','Age','SibSp','Parch','Fare','Embarked']]
data.head(5)

data["Survived"].hist()

def calculate_prior(data,target):
    classes=sorted(list(data[target].unique()))
    prior=[]
    for i in classes:
        prior.append((len(data[data[target]==i])) / (len(data)) )
    return prior

def calculate_likelihood(data,target,featname,featval,labels):
    data=data[data[target]==labels]
    mean,std=data[featname].mean(),data[featname].std()
    pxgiveny = (1/(std * np.sqrt(2 * np.pi))  *  np.exp( -((featval-mean)**2) / (2 * std ** 2))  )   
    return pxgiveny

def naive_bayes(data,test,target):
    features=list(data.columns)[0:-1]
    prior=calculate_prior(data,target)
    ypred=[]
    for testpoint in test:
        classes=sorted(list(data[target].unique()))
        likelihood=[1]*len(classes)
        for i in range(len(classes)):
            for j in range(len(features)):
                likelihood[i] = calculate_likelihood(data,target,features[j],testpoint[j],classes[i])
                
        postprob=[1]*len(classes)
        for i in range(len(classes)):
            postprob[i] = likelihood[i] * prior[i]
            
        ypred.append(np.argmax(postprob))
        
    return np.array(ypred)

train,test = train_test_split(data,test_size=.2,random_state=41)

xtest=test.iloc[:,:-1].values
ytest=test.iloc[:,-1].values
ypred=naive_bayes(train,xtest,"Embarked")

print(confusion_matrix(ytest,ypred))
print(f1_score(ytest,ypred,average="micro"))