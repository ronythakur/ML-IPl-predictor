from flask import Flask,render_template,request
import random
import pickle
import numpy as np
app=Flask(__name__)

#ML Models into a File
ML_Models=['Logistic-Regression.pickle','Random-Forest.pickle']


@app.route("/")
def Main():
    return render_template("Main.html")

@app.route("/Predict",methods=['POST','GET'])
def Predict():
    Teams=['CSK','DC','KKR','PBKS','MI','RCB','RR','SRH']
    Colors=['#FFFF00','#2e68c7','#663333','#cf2348','#0000CC','#FF0000','#FF3399','#FF8000']
    # Team1 Input
    team1_name=(request.form['Name1'])
    team1_potential=int(request.form['Potential1'])
    team1_standing=int(request.form['Standing1'])
    team1_index=Teams.index(team1_name)+1
    team1_clr=Colors[team1_index-1]

    # Team-2 Input
    team2_name=(request.form['Name2'])
    team2_potential=int(request.form['Potential2'])
    team2_standing=int(request.form['Standing2'])
    team2_index=Teams.index(team2_name)+1
    team2_clr=Colors[team2_index-1]

    #Toss-Winner Input
    toss_winner=request.form['Toss']
    if(toss_winner==team1_name):
        toss_winner=1
    else:
        toss_winner=2

    #Printing values
    print(toss_winner)
    print(team1_index,' ',team1_name,' ',team1_potential+1,' ',team1_standing+1)
    print(team2_index,' ',team2_name,' ',team2_potential+1,' ',team2_standing+1)

    #Selecting a ML-Model
    val=ML_Models[random.randint(0,1)]
    print("val ",val) 
    with open(f"{val}",'rb') as f:
        model=pickle.load(f)
    f.close()

    #Prediction
    team1_percent=model.predict_proba([[team2_standing-team1_standing,team1_potential-team2_potential,toss_winner]])[:,0]
    team2_percent=model.predict_proba([[team2_standing-team1_standing,team1_potential-team2_potential,toss_winner]])[:,1]
    print(team1_percent,' ',team2_percent)
    
    return render_template("Predict.html",t1_name=team1_name,t1_percent=int((team1_percent+0.005)*100),t1_clr=team1_clr,t2_name=team2_name,t2_percent=int((team2_percent+0.005)*100),t2_clr=team2_clr)
if __name__=="__main__":
    app.run(debug=True)
