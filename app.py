from flask import Flask, render_template, request
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler



app = Flask(__name__)

model =pickle.load(open('random_forest_regression_model_1.pkl', 'rb'))
@app.route('/',methods=['GET'])

def Home():
    return render_template('index.html')

standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
        Fuel_Type_Diesel=0
        MarutiSwift=0
        MarutiAlto=0
        MarutiWagon=0
        Hyundaii20=0
        HyundaiVerna=0
        HyundaiGrand=0
        HyundaiSantro=0
        ToyotaInnova=0
        HyundaiEON=0
        TataIndica=0

        if request.method == 'POST':
            name=request.form['Car_name']
            if(name=='MarutiSwift'):
                MarutiSwift=1
            elif (name == 'MarutiAlto'):
                MarutiAlto = 1
            elif (name == 'MarutiWagon'):
                MarutiWagon = 1
            elif (name == 'Hyundaii20'):
                Hyundaii20 = 1
            elif (name == 'HyundaiVerna'):
                HyundaiVerna = 1
            elif (name == 'HyundaiGrand'):
                HyundaiGrand = 1
            elif (name == 'HyundaiSantro'):
                HyundaiSantro = 1
            elif (name == 'ToyotaInnova'):
                ToyotaInnova = 1
            elif (name == 'HyundaiEON'):
                HyundaiEON = 1
            else:
                TataIndica = 1

            Year = int(request.form['Year'])
            Kms_Driven=int(request.form['kms'])
            Kms_Driven2=np.log(Kms_Driven)
            Owner=int(request.form['owners'])
            Dealer=request.form['dealer']
            if(Dealer=='dealer'):
                Dealer=1
            else:
                Dealer=0
            Fuel_Type_Petrol=request.form['Fuel_Type_Petrol']
            if(Fuel_Type_Petrol=='Petrol'):
                Fuel_Type_Petrol=1
                Fuel_Type_Diesel=0
            else:
                Fuel_Type_Petrol=0
                Fuel_Type_Diesel=1
            Year=2020-Year
            Seller_Type_Individual=request.form['dealer']
            if(Seller_Type_Individual=='individual'):
                Seller_Type_Individual=1
            else:
                Seller_Type_Individual=0
            Transmission_Mannual=request.form['Transmission']
            if(Transmission_Mannual=='manual'):
                Transmission_Mannual=1
            else:
                Transmission_Mannual=0
            prediction=model.predict([[Kms_Driven2,Owner,MarutiSwift,MarutiAlto,MarutiWagon,
                                       Hyundaii20,HyundaiVerna,HyundaiGrand,HyundaiSantro,
                                       ToyotaInnova,HyundaiEON,TataIndica,
                                       Year,Seller_Type_Individual,Dealer,Fuel_Type_Diesel,Fuel_Type_Petrol,Transmission_Mannual]])
            output=round(prediction[0],2)
            if output<0:
                return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
            else:
                return render_template('index.html',prediction_text="You Can Sell The Car at {}".format(output))
        else:
            return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

