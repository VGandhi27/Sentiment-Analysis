# 📊 Sentiment Analysis Dashboard

![Dashboard Screenshot](https://github.com/user-attachments/assets/b03e7409-706f-459c-9ee0-94dc0d3cd525)


🚀 **Live Demo:** [Sentiment Analysis](https://sentiment-analysis-1-r0ao.onrender.com)

📄 **Research Paper:** [SVM-Based Framework for Sentiment Analysis](https://ijcmps.mstrust.in/Files/Vol/Issue/ijcmps-6-1-1.pdf)

## 🌟 Overview

The **Sentiment Analysis Dashboard** is a web-based application designed to determine the sentiment polarity (positive or negative) of user-input text. Leveraging multiple machine learning models, the system provides real-time sentiment analysis with visual representations to facilitate user understanding.

**Key Features:**

- **User-Friendly Interface:** Simplified input for seamless user experience.
- **Multiple Machine Learning Models:** Implements Naïve Bayes, Logistic Regression, K-Nearest Neighbors (KNN), and Decision Tree classifiers.
- **Visual Representations:** Pie charts and graphs to depict sentiment distribution and model performance.
- **Real-Time Analysis:** Immediate feedback upon text submission.

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript (Bootstrap)
- **Backend:** Django (Python)
- **Machine Learning Models:**
  - Naïve Bayes
  - Logistic Regression
  - K-Nearest Neighbors (KNN)
  - Decision Tree
- **Visualization Libraries:** Matplotlib, Seaborn
- **Database:** SQLite (default), with potential for PostgreSQL/MySQL integration

---

## 🎯 How It Works

1. **Data Preprocessing:** Utilizes Natural Language Processing (NLP) techniques such as tokenization, stop-word removal, and stemming to prepare the input text.
2. **Feature Extraction:** Employs Term Frequency-Inverse Document Frequency (TF-IDF) to convert text data into numerical features suitable for model input.
3. **Model Prediction:** Processes the features through trained machine learning models to predict sentiment polarity.
4. **Visualization:** Displays the results using pie charts to represent the proportion of positive and negative sentiments as predicted by each model.

---

## 🚀 Installation Guide

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/VGandhi27/Sentiment-Analysis.git
   cd Sentiment-Analysis
   ```
2. **Create and Activate Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Apply Migrations:**
   ```bash
   python manage.py migrate
   ```
5. **Start the Development Server:**
   ```bash
   python manage.py runserver
   ```
6. **Access the Dashboard:** Open `http://127.0.0.1:8000` in your web browser.

---

## 📷 Screenshots

### ➤ **User Interface**
![UI Screenshot](https://github.com/user-attachments/assets/89837d3b-a065-4dc0-8c14-a0edb1a98c07)


### ➤ **Model Predictions Visualization**
![Model Predictions](https://github.com/user-attachments/assets/aeb7a0f2-77d0-44cd-b485-091d755b16b5)


---

## 📝 Research & Development

This project is grounded in comprehensive research on sentiment analysis using machine learning techniques. The detailed methodology, including data preprocessing, feature extraction, model selection, and evaluation metrics, is documented in the research paper: [SVM-Based Framework for Sentiment Analysis](https://ijcmps.mstrust.in/Files/Vol/Issue/ijcmps-6-1-1.pdf).

---

## 💡 Future Enhancements

- **Expand Dataset:** Incorporate larger and more diverse datasets to improve model generalization.
- **Advanced Models:** Integrate deep learning models such as Recurrent Neural Networks (RNNs) and Transformers for enhanced performance.
- **Multilingual Support:** Extend sentiment analysis capabilities to multiple languages.
- **Deployment:** Host the application on cloud platforms like AWS, Heroku, or Vercel for public accessibility.

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a Pull Request.

---

## 📬 Contact

- **Author:** Vidushi Gandhi
- **GitHub:** [VGandhi27](https://github.com/VGandhi27)
- **LinkedIn:** [Vidushi Gandhi](https://www.linkedin.com/in/vidushi-gandhi/)

---

This README provides a comprehensive overview of the **Sentiment Analysis Dashboard**, detailing its features, technical stack, setup instructions, and future development plans. For a deeper understanding, refer to the linked research paper and project report.

--- 
