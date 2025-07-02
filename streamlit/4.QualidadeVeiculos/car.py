import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from sklearn.naive_bayes import CategoricalNB
from sklearn.metrics import accuracy_score

st.set_page_config(
    page_title="Classificação Veículos", 
    page_icon="🚗",
    layout="wide"
)
st.title("Classificação de Veículos 🚗")

@st.cache_data
def load_data_and_modal():
    carros = pd.read_csv("car.csv", sep=",")
    encoder = OrdinalEncoder()

    for col in carros.columns.drop('class'):
        carros[col] = carros[col].astype('category')

    X_encoded = encoder.fit_transform(carros.drop('class', axis=1))
    y = carros['class'].astype('category').cat.codes

    X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)
    model = CategoricalNB()
    model.fit(X_train, y_train)

    y_prev = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_prev)

    return encoder, model, accuracy, carros


encoder, model, accuracy, carros = load_data_and_modal()

st.title('Previsao de qualidade do veiculo')
st.write(f"Acurácia do modelo: {accuracy:.2f}")
 

input_features = [
        st.selectbox("Preço:",carros['buying'].unique()),
        st.selectbox("Manutenção:",carros['maint'].unique()),
        st.selectbox("Portas:",carros['doors'].unique()),
        st.selectbox("Capacidade de Passegeiros:",carros['persons'].unique()),
        st.selectbox("Porta Malas:",carros['lug_boot'].unique()),
        st.selectbox("Segurança:",carros['safety'].unique()),
]


if st.button("Processar"):
    input_df = pd.DataFrame([input_features], columns=carros.columns.drop('class'))
    input_encoded = encoder.transform(input_df)
    predict_encoded = model.predict(input_encoded)
    previsao = carros['class'].astype('category').cat.categories[predict_encoded][0]
    st.header(f"Resultado da previsão:  {previsao}") 
