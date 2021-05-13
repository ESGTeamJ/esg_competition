'''Importing esential libraries'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn import tree
from sklearn.model_selection import cross_val_score

'''Adding path to a .csv/.xlsx file with historical contribution of CO_2'''
mydata = pd.read_excel('D:\Desktop\ml\sample.xlsx')

''' Keep only those with 4 years of data 
where t is "current year" a t+1 "next year"'''
'''In .csv file are normally used  FY0, FY-1, FY-2,... 
instead of t+1, t, t-1,...'''
mydata = mydata[mydata['t+1'].notna()]
mydata = mydata[mydata['t'].notna()]
mydata = mydata[mydata['t-1'].notna()]
mydata = mydata[mydata['t-2'].notna()]


mydata = mydata[['t+1', 't', 't-1', 't-2']]


print(mydata.shape)

         
'''Predict the trend'''
X = mydata.copy()

y = X.pop('t+1')
'''This ensures that X no longer contains the target columns'''


X_train, X_test, y_train, y_test = train_test_split(X, y,test_size = 0.2, random_state = 37)


from sklearn.ensemble import RandomForestRegressor

'''fit the model'''
RFmodel = RandomForestRegressor(max_depth=2, random_state = 0)
                              

RFmodel.fit(X_train, y_train)


'''predict'''
y_pred = RFmodel.predict(X_test)

score = RFmodel.score(X_train, y_train)
print("R-squared:", score) 


from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error


mae = mean_absolute_error(y_test, y_pred)


mse = mean_squared_error(y_test, y_pred)


r2 = r2_score(y_test, y_pred)


print('Mean Absolute Error:', round(mae, 2))
print('Mean Squared Error:', round(mse, 2))
print('R-squared scores:', round(r2, 2))


characteristics = X.columns
'''Get the variables importances, sort them, and print the result'''
# Get the variables importances, sort them, and print the result
importances = list(RFmodel.feature_importances_)
characteristics_importances = [(characteristic, round(importance, 2)) for characteristic, importance in zip(characteristics, importances)]
characteristics_importances = sorted(characteristics_importances, key = lambda x: x[1], reverse = True)
[print('Variable: {:20} Importance: {}'.format(*pair)) for pair in characteristics_importances];

'''plot for visualization..'''
import matplotlib.pyplot as plt

plt.bar(characteristics, importances, orientation = 'vertical')
plt.xticks(rotation = 'vertical')
plt.ylabel('Dependence of t+1 with past years contribution')
plt.xlabel('year')
plt.grid(axis = 'y', color = '#D3D3D3', linestyle = 'solid')
plt.show()
plt.savefig('D:\\Desktop\\lol')
