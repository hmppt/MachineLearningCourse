from sklearn.tree import DecisionTreeClassifier  
from sklearn.datasets import load_iris  
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import accuracy_score

def get_data():
    iris = load_iris()
    data = iris.data
    result = iris.target
    return data,result

data,result = get_data()
data_train,data_test,result_train,result_test = train_test_split(data,result, test_size=0.3)
Tree = DecisionTreeClassifier()
Tree.fit(data_train,result_train)
pred = Tree.predict(data_test)

print(pred)
print(result_test)
print(accuracy_score(result_test,pred))