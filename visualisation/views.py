import os
import pickle
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# Load the model
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'machinelearning/sentiment_model_naive_bayes.pkl')
MODEL_PATH_lr = os.path.join(os.path.dirname(__file__), 'machinelearning/sentiment_model_lr.pkl')

with open(MODEL_PATH, 'rb') as model_file:
    naive_bayes_model = pickle.load(model_file)

with open(MODEL_PATH_lr, 'rb') as model_file:
    lr_model = pickle.load(model_file)

def predict_sentiment(text, model):
    # Make a prediction using the loaded model
    prediction = model.predict([text])[0]
    probability = model.predict_proba([text])[0]
    return prediction, probability


def sentiment_analysis_view(request):
    context={}
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        print(f'user_input--{user_input}')
        # Assuming predict_sentiment returns predictions and probabilities
        nb_prediction, nb_probability = predict_sentiment(user_input, naive_bayes_model)
        lr_prediction, lr_probability = predict_sentiment(user_input, lr_model)
        
        context = {
            'user_input': user_input,
            'nb_prediction': nb_prediction * 100,  # Scale to percentage
            'nb_probability': nb_probability * 100,  # Scale to percentage
            'lr_prediction': lr_prediction * 100,  # Scale to percentage
            'lr_probability': lr_probability * 100,  # Scale to percentage
        }

    print(f'context--{context}')
    return render(request, 'visualisation/home.html',context)
