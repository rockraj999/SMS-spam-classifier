import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))


def transform_text(text):
    text = text.lower()  # 1
    text = nltk.word_tokenize(text)  # 2
    y = []
    for i in text:
        if i.isalnum() and i not in string.punctuation:  # 3
            y.append(i)

    text = y[:]
    y.clear()
    for i in text:  # 4
        if i not in stopwords.words('english'):
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return ' '.join(y)



st.title("Email/SMS spam Classifier")

input_sms = st.text_area("Enter the message")

if st.button('Predict'):
    # 1. preprocess:
    transformed_sms = transform_text(input_sms)
    # 2. vectorize
    vect_opt = tfidf.transform([transformed_sms])
    #3. predict
    result = model.predict(vect_opt)[0]

    if result==1:
        st.header("Spam")
    else:
        st.header("Not Spam")



