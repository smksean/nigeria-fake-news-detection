# Nigeria Fake News Detection

> Binary NLP classifier detecting fake vs. real news from Nigerian media — TF-IDF pipeline with a deployed Streamlit web app covering 38 Nigerian news sources.

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-orange.svg)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-app-red.svg)](https://streamlit.io/)

---

## Problem

Misinformation spreads rapidly across Nigerian digital media. This project builds a classifier that flags fake news from 38 major Nigerian outlets — including Punch, Vanguard, Channels TV, Sahara Reporters, Arise News, and others — based on headline and article content.

---

## Approach

1. **Dataset**: Synthetic Nigerian news dataset with balanced real/fake labels across 38 sources
2. **EDA**: Label distribution, top news sources, headline length analysis by label, word clouds for fake vs. real news
3. **Preprocessing**: Regex cleaning, stopword removal, NLTK tokenisation
4. **Vectorisation**: TF-IDF
5. **Modelling**: Multiple scikit-learn classifiers evaluated; best model serialised to `models/model.pkl`
6. **Deployment**: Streamlit web app — paste a headline and select a news source to get an instant real/fake prediction

---

## Results

- Trained model: `models/model.pkl`
- Vectoriser: `vectorizer/vectorizer.pkl`
- Full classification report and confusion matrix in the notebook

---

## How to Run

**Install dependencies:**
```bash
pip install -r requirements.txt
```

**Run the web app:**
```bash
streamlit run app.py
```

**Explore the notebook:**
```bash
jupyter notebook "notebooks/Nigeria_fake_new_detection (2).ipynb"
```

---

## Tech Stack

`Python` · `scikit-learn` · `NLTK` · `pandas` · `NumPy` · `Streamlit` · `matplotlib` · `seaborn` · `joblib`

---

## Project Structure

```
nigeria-fake-news-detection/
├── app.py                                    # Streamlit web app
├── models/model.pkl                          # Trained classifier
├── vectorizer/vectorizer.pkl                 # TF-IDF vectoriser
├── notebooks/
│   └── Nigeria_fake_new_detection (2).ipynb  # EDA + training
├── data/
│   └── nigeria_synthetic_news_dataset.xlsx
├── output/                                   # Processed outputs
└── requirements.txt
```

---

## Supported News Sources

The classifier covers 38 Nigerian outlets across politics, entertainment, finance, and fact-checking categories, including:

`Punch` · `Vanguard` · `Channels TV` · `Sahara Reporters` · `TheCable` · `Nairametrics` · `Dubawa` · `Africa Check` · `FactCheckHub` · `Linda Ikeji Blog` · `BellaNaija` and more.
