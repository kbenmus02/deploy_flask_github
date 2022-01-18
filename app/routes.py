from app import app
from flask import Flask, render_template, jsonify, request
import requests
import pickle
import numpy as np
# modules nécessaires pour le notebook
import pickle
#mport os

mydict = pickle.load(open("model_params.pkl", "rb"))


@app.route('/')
@app.route('/index')
def index():
    modeles = {'titre': 'Regression Lineaire'}
    # parametres = [{"param1":"10", "param2":"Uniform"},
    #               {"param1":"20", "param2":"lineaire"}]
    parametres = mydict

    return render_template('index.html', title = 'Accueil', mod=modeles, page_no=1, param=parametres)


from app.forms import ModelePredictionForm
from flask import flash, redirect

model_param = pickle.load(open("model_params.pkl", "rb"))
model = pickle.load(open("model_rl.pkl", "rb"))
param2 = {"coef":model.coef_, "inter": model.intercept_}
# print(model_param)

@app.route("/prediction", methods=["GET"])
def get_data_and_predict():
    data = request.get_json()
    print(data)
    data_in = np.array([data["TV"], data["Radio"], data["Newspaper"]]).reshape(1, -1)
    y = model.predict(data_in).tolist()[0]
    #output_dict = {"TV:": data["TV"], "Radio:": data["Radio"], "Newspaper:": data["Newspaper"], "An_prediction": y}
    #output_dict = {k : v for k, v in sorted(output_dict.items(), key=lambda item:item[0])}
    #return jsonify(output_dict)

    return jsonify({"Prediction:":y})



# prendre en charge de formulaire et recuperer les donnees du formulaire
@app.route("/form_input", methods=["GET", "POST"])
def form_input():
    form = ModelePredictionForm()
    if form.validate_on_submit():
        #data_in = np.array([float(form.TV.data), float(form.Radio.data), float(form.Newspaper.data)]).reshape(1, -1)
        #modele = pickle.load(open("model_rl.pkl", "rb"))
        #y = modele.predict(data_in)[0]

        data_in = {
            "TV": float(form.TV.data),
            "Radio": float(form.Radio.data),
            "Newspaper": float(form.Newspaper.data)
        }
        # data_in = {
        #     "TV": 12,
        #     "Radio": 42,
        #     "Newspaper": 12.8
        # }
        print(data_in)

        #y = requests.get("http://127.0.0.1:5000/prediction", json=data_in)
        #port = os.environ.get("PORT", 5000)
        y = requests.get("http://127.0.0.1:5000/prediction", json=data_in)
        print(y.status_code)
        print(y.json()["Prediction:"])

        flash("TV = {}, Radio = {}, Newspaper = {} donnent une prédioction de : {}".format(float(form.TV.data),
                                                                                           float(form.Radio.data),
                                                                                           float(form.Newspaper.data),
                                                                                           y.json()["Prediction:"]))
        return redirect("/index")
    return render_template("form_input.html", title = "Modele de Prediction", form = form)






