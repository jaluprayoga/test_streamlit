import streamlit as st
import streamlit.components.v1 as stc
import pickle

with open('gradient_boosting_regressor_model.pkl', 'rb') as file:
    gradient_boosting_regressor_model = pickle.load(file)

html_temp = """<div style="background-color:#000;padding:10px;border-radius:10px">
                <h1 style="color:#fff;text-align:center">Loan Eligibility Prediction App</h1> 
                <h4 style="color:#fff;text-align:center">Made for: Credit Team</h4> 
                """

desc_temp = """ ### Loan Prediction App 
                This app is used by Credit team for deciding Loan Application
                
                #### Data Source
                Kaggle: Link <Masukkan Link>
                
                """

def main():
    stc.html(html_temp)
    menu = ["Home", "Machine Learning App"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        st.markdown(desc_temp, unsafe_allow_html=True)
    elif choice == "Machine Learning App":
        run_ml_app()

def run_ml_app():
    design = """<div style="padding:15px;">
                    <h1 style="color:#fff">Loan Eligibility Prediction</h1>
                </div
             """
    st.markdown(design, unsafe_allow_html=True)
    
    #Membuat Struktur Form
    left, right = st.columns((2,2))
    age = left.number_input('age')
    bmi = right.selectbox('bmi', (24, 30, 55))
    children = left.selectbox('children', (0,1,2,3, 4, 5))
    sex_male = right.selectbox('gender', ('cewe', 'cowo'))
    smoker_yes = left.selectbox('smoker', ('Yes', 'No'))
    live = right.selectbox('live', ('region_northwest', 'region_southeast','region_southwest'))
    button = st.button("Predict")

    #If button is clilcked
    if button:
        result = predict(age, bmi, children, sex_male, smoker_yes, live)

        if result == 'Eligible':
            st.success(f'You are {result} for the loan')
        else:
            st.error(f'You are {result} for the loan')

def predict(age, bmi, children, sex_male, smoker_yes, live):
    #Preprocessing User Input
    sex = 0 if sex_male == 'cewe' else 1
    smk = 0 if smoker_yes == 'No' else 1
    # lve = 0 if live == 'region_northwest' else 1 if property_area == 'Urban' else 2

    #Making prediction
    prediction = gradient_boosting_regressor_model.predict(
        [[age, bmi, children, sex, smk, 1, 0, 0]])
    
    result = 'Not Eligible' if prediction == 0 else 'Eligible'
    return result

if __name__ == "__main__":
    main()
