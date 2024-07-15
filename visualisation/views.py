import os
import pickle
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Define paths to each model
MODEL_PATHS = {
    'naive_bayes': os.path.join(os.path.dirname(__file__), 'machinelearning/sentiment_model_naive_bayes.pkl'),
    'lr': os.path.join(os.path.dirname(__file__), 'machinelearning/sentiment_model_lr.pkl'),
    'knn': os.path.join(os.path.dirname(__file__), 'machinelearning/sentiment_model_knn.pkl'),
    # 'svm': os.path.join(os.path.dirname(__file__), 'machinelearning/sentiment_model_svm.pkl'),
    'dt': os.path.join(os.path.dirname(__file__), 'machinelearning/sentiment_model_dt.pkl'),
}

# Load all models
models = {}
for model_name, model_path in MODEL_PATHS.items():
    with open(model_path, 'rb') as model_file:
        models[model_name] = pickle.load(model_file)

# Function to predict sentiment using a given model
def predict_sentiment(text, model):
    prediction = model.predict([text])[0]
    probability = model.predict_proba([text])[0] * 100  # Scale to percentage
    if prediction == 0:
        sentiment = "Negative Sentiment"
    elif prediction == 1:
        sentiment = "Positive Sentiment"
    else:
        sentiment = "No Sentiment can be detected"
        probability = 0.0
    return prediction, probability.tolist(), sentiment


@csrf_exempt
def sentiment_analysis_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        results = {}

        for model_name, model in models.items():
            prediction, probability, sentiment = predict_sentiment(user_input, model)
            results[f'{model_name}_prediction'] = int(prediction)
            results[f'{model_name}_probability'] = probability
            results[f'{model_name}_sentiment'] = sentiment

        return JsonResponse(results)

    # Handle GET or other methods gracefully
    return render(request, 'visualisation/home.html', {})
