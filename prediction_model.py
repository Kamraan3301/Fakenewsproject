import joblib
import re
from nltk.stem.porter import PorterStemmer
import numpy as np
ps = PorterStemmer()
import nltk
import matplotlib.pyplot as plt


nltk.download('wordnet')
nltk.download('punkt')


model = joblib.load('C:\\Users\\User\\Documents\\Fakenewsproject\\model\\model.pkl')
print('=> Pickle Loaded : Model ')
bow = joblib.load('C:\\Users\\User\Documents\\Fakenewsproject\\model\\bow2.pkl')
print('=> Pickle Loaded : Vectorizer')


class PredictionModel:
    output = {}

    # constructor
    def __init__(self, original_text):
        self.output['original'] = original_text

    # predict
    def predict(self):
        def myround( x,base=100):
            return base*x
        review = self.clean_article()
        vect = bow.transform([review]).toarray()
        prediction_array = model.predict(vect)
        proba_array = model.predict_proba(vect)
        maxProba = np.amax(proba_array)
        maxProba = format(maxProba, ".2f")
        self.output['prediction'] = 'FAKE' if prediction_array == 0 else 'REAL'
        self.output['prediction_accuracy'] = myround(float(maxProba))
        predx= self.output['prediction']
        predy=self.output['prediction_accuracy']
        if predx=='REAL':
            data = {'REAL': predy, 'FAKE': 0}
            names = list(data.keys())
            values = list(data.values())
            fig, axs = plt.subplots(figsize=(9, 6), sharey=True)
            axs.bar(names, values)
            p=plt.show()
            print(p) 
        elif predx=='FAKE':
            data = {'REAL': 0, 'FAKE': predy}
            names = list(data.keys())
            values = list(data.values())
            fig, axs = plt.subplots(figsize=(9, 6), sharey=True)
            axs.bar(names, values)
            p=plt.show()
            print(p)
        return self.output
    def clean_article(self):
        art = re.sub("[^A-Za-z0-9' ]", '', self.output['original'])
        art2 = re.sub("[( ' )(' )( ')]", ' ', art)
        art3 = re.sub("\s[A-Za-z]\s", ' ', art2)
        return art3.lower()
    