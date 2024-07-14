# dashboard/views.py

import os
import pickle
from django.shortcuts import render
from django.conf import settings

# Load the model
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'machinelearning/sentiment_model_naive_bayes.pkl')
with open(MODEL_PATH, 'rb') as model_file:
    lr_model = pickle.load(model_file)

def predict_sentiment(text, model):
    # Make a prediction using the loaded model
    prediction = model.predict([text])[0]
    probability = model.predict_proba([text])[0]
    return prediction, probability

def sentiment_analysis_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')  # Use get() to safely retrieve POST data
        prediction, probability = predict_sentiment(user_input, lr_model)
        context = {
            'user_input': user_input,
            'prediction': prediction,
            'probability': probability,
        }
        return render(request, 'visualisation/result.html', context)
    return render(request, 'visualisation/home.html')
