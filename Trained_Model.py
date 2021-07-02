import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
from sklearn import linear_model

# Taking Data-Frame
df=pd.read_csv("IPL Data.csv")


#Label Encoding for Team-name
from sklearn.preprocessing import LabelEncoder
le_team1=LabelEncoder()
le_team2=LabelEncoder()
le_winner=LabelEncoder()
le_toss=LabelEncoder()

#Creating a new data-frame
dfle=df

dfle['Team1']=le_team1.fit_transform(dfle['Team1'])
dfle['Team2']=le_team2.fit_transform(dfle['Team2'])
dfle['Toss Winner']=le_toss.fit_transform(dfle['Toss Winner'])
dfle['Winner']=le_winner.fit_transform(dfle['Winner'])


#Extracting columns from Data-Frame

#Team1

Team1=dfle['Team1']
P1=dfle['Team1 Potential']
S1=dfle['Team1 Standing']

#Team2
Team2=dfle['Team2']
P2=dfle['Team2 Potential']
S2=dfle['Team2 Standing']

#Toss-Winner and Match-Winner
Toss=dfle['Toss Winner']
Win=dfle['Winner']

#Length of dataframe
total=len(Toss)

#Potential-difference and Standing difference
Pdif=P1-P2
Sdif=S2-S1


#Creating new dataframe

Data=[[]]
Data.clear()
for i in range(total):
    p=1
    if(i%3!=0):
        if(Team1[i]==Toss[i]):
            p=1
        Data.insert(i+1,[int(Team1[i]),int(Team2[i]),int(Sdif[i]),int(Pdif[i]),p,1])
    else:
        if(Team2[i]==Toss[i]):
            p=1
        Data.insert(i+1,[int(Team2[i]),int(Team1[i]),int(-Sdif[i]),int(-Pdif[i]),p,2])


#Creating Dataframes
New=pd.DataFrame(Data,columns=['T-1','T-2','S-dif','P-dif','Toss','Winner'])
New_Data=New.drop(['T-1','T-2'],axis='columns')

#Printing Dataframes
print(New_Data)
print(New)


Win=New['Winner']
New=New.drop(['Winner'],axis='columns')
Win1=New_Data['Winner']
New_Data=New_Data.drop(['Winner'],axis='columns')


cnt=0
cnt1=0
P_dif=New['P-dif']
S_dif=New['S-dif']
Toss=New['Toss']
for i in range(total):
    if(P_dif[i]>=0 and S_dif[i]>=0):
        cnt+=1
        if(Win[i]==1):
            cnt1+=1

labels="Team winning after high potential and standing","Team losing with high potential and standing"
sizes=[cnt1,cnt-cnt1]
colors=['green','red']
plt.pie(sizes,labels=labels,colors=colors,autopct='%1.1f%%',startangle=0,shadow=True)
plt.axis('equal')
#To show the pie
#plt.show()
    


#Train-Test Split

from sklearn.model_selection import train_test_split

#1.New-Dataframe Train Test
X_train,X_test,Y_train,Y_test=train_test_split(New,Win,test_size=0.2)
       
#2.New-Data-Dataframe Train Test
X_train1,X_test1,Y_train1,Y_test1=train_test_split(New_Data,Win,test_size=0.2)


#Logistic Regression

#1.New-Dataframe
reg=linear_model.LogisticRegression()
reg.fit(X_train,Y_train)
print(reg.score(X_test,Y_test))

#2.New-Data Dataframe
reg1=linear_model.LogisticRegression()
reg1.fit(X_train1,Y_train1)
print(reg1.score(X_test1,Y_test1))

#Dumping into File

2New-Data Dataframe
with open("Logistic-Regression.pickle",'wb') as f:
    pickle.dump(reg1,f)
f.close()











#Random Forest Classfier

from sklearn.ensemble import RandomForestClassifier

#1.New-Dataframe
clf=RandomForestClassifier(max_depth=2,random_state=1)
clf.fit(X_train,Y_train)
print(clf.score(X_test,Y_test))

#2.New-Data Dataframe
clf1=RandomForestClassifier(max_depth=2,random_state=1)
clf1.fit(X_train1,Y_train1)
print(clf1.score(X_test1,Y_test1))

#Dumping File

#1.New-Dataframe
with open("Random1.pickle",'wb') as f:
    pickle.dump(clf,f)
f.close()

#2.New-Data-Dataframe
with open("Random-Forest.pickle",'wb') as f:
    pickle.dump(clf1,f)
f.close()






