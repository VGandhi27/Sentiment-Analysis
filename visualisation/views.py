import os
import pickle
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Load the model
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'machinelearning/sentiment_model_naive_bayes.pkl')
MODEL_PATH_lr = os.path.join(os.path.dirname(__file__), 'machinelearning/sentiment_model_lr.pkl')
MODEL_PATH_knn = os.path.join(os.path.dirname(__file__), 'machinelearning/sentiment_model_knn.pkl')
MODEL_PATH_svm = os.path.join(os.path.dirname(__file__), 'machinelearning/sentiment_model_svm.pkl')
MODEL_PATH_dt = os.path.join(os.path.dirname(__file__), 'machinelearning/sentiment_model_dt.pkl')
with open(MODEL_PATH, 'rb') as model_file:
    naive_bayes_model = pickle.load(model_file)

with open(MODEL_PATH_lr, 'rb') as model_file:
    lr_model = pickle.load(model_file)

def predict_sentiment(text, model):
    # Make a prediction using the loaded model
    prediction = model.predict([text])[0]
    probability = model.predict_proba([text])[0]
    probability=(probability * 100).tolist()
    prob=probability[1]
    if prediction == 0:
        sentiment="Negative Sentiment"
    elif prediction == 1:
        sentiment="Positive Sentiment"

    else:
        sentiment="No Sentiment can be detected "
        prob=0
    print(f'prediction--{prediction}, probability--{probability},prediction---{prediction},sentiment={sentiment}')
    return prediction, probability,sentiment

@csrf_exempt
def sentiment_analysis_view(request):
    context = {}
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        print(f'user_input--{user_input}')
        # Assuming predict_sentiment returns predictions and probabilities
        nb_prediction, nb_probability,nb_sentiment = predict_sentiment(user_input, naive_bayes_model)
        lr_prediction, lr_probability,lr_sentiment = predict_sentiment(user_input, lr_model)
        
        context = {
            'user_input': user_input,
            'nb_prediction': int(nb_prediction ),  # Scale to percentage and convert to int
            'nb_probability': (nb_probability ),  # Scale to percentage and convert to list
            'lr_prediction': int(lr_prediction ),  # Scale to percentage and convert to int
            'lr_probability': (lr_probability ),  # Scale to percentage and convert to list
            'lr_sentiment':lr_sentiment,
            'nb_sentiment':nb_sentiment
        }
        return JsonResponse(context)

    data={}
    return render(request, 'visualisation/home.html', data)
