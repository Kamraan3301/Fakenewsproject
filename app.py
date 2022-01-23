from flask import Flask, render_template
from prediction_model import PredictionModel
from forms import OriginalTextForm
import fakenews
import nltk

nltk.download('stopwords')
app = Flask(__name__)
app.config['SECRET_KEY'] = '4c99e0361905b9f941f17729187afdb9'


@app.route("/", methods=['POST', 'GET'])
def home():
    form = OriginalTextForm()

    if form.global_times.data:
        news_data_1=fakenews.GlobalCN()
        form.original_text.data = str(news_data_1)
        return render_template('home.html', form=form, output=False)
    elif form.daily.data:
        news_data_2=fakenews.dailystar()
        form.original_text.data = str(news_data_2)
        return render_template('home.html', form=form, output=False)
    elif form.abc.data:
        news_data_3 = fakenews.abc() 
        form.original_text.data = str(news_data_3)
        return render_template('home.html', form=form, output=False)
    elif form.predict.data:
        if len(str(form.original_text.data)) > 10:
            model = PredictionModel(form.original_text.data)
            return render_template('home.html', form=form, output=model.predict())
    return render_template('home.html', form=form, output=False)


@app.route('/predict/<original_text>', methods=['POST', 'GET'])
def predict(original_text):
    model = PredictionModel(original_text)
    return model.predict()
if __name__ == '__main__':
    app.run(debug=True)

