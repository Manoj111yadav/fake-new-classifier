from ast import If 
from pyexpat import model
from flask import Flask ,escape,request,render_template
import pickle
import os

vector_path = r'C:\Users\indra\OneDrive\Desktop\fakenews\newsapp\vectorizer.pkl'


model_path = r'C:\Users\indra\OneDrive\Desktop\fakenews\fake news classifier\finalized_model.pkl'

vector = pickle.load(open(vector_path,'rb'))
model = pickle.load(open(model_path,'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
     if request.method == "POST":
         News= request.form['news']
         print(News)
         predict =model.predict(vector.transform([News]))[0]
         print(predict)

         return render_template("prediction.html", prediction_text="News headline is ->{}".format(predict))

     else:       
          return render_template("prediction.html")                                   
                                            
                                            
if __name__=='__main__':
        app.run(debug=True)
