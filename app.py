import streamlit as st
import pickle

def main():
     st.markdown("<h1 style='text-align: center; color:white;'>Health Insurance Cost Prediction</h1>",
                 unsafe_allow_html=True)

     st.image('https://miro.medium.com/v2/resize:fit:1400/0*ssbGU5VIxtVB6NrF')

        # loading in the model to predict on the data 
     pickle_in = open('rfclassifier.pkl', 'rb') 
     model = pickle.load(pickle_in) 


     age = st.slider('Enter Your Age',18,100)

     sex = st.selectbox('Sex',('Male','Female'))
     if(sex=='Male'):
          sex=1
     else:
          sex=0

     bmi = st.number_input("Enter Your BMI Value")

     children = st.selectbox('Enter Number of Children',(0,1,2,3,4))

     smoker = st.selectbox('Smoker',('Yes','No'))
     if(smoker=='Yes'):
          smoker=1
     else:
          smoker=0

     region = st.selectbox('Enter Your Region',('Southwest','Southeast','Northwest','Northeast'))
     if(region=='Southwest'):
          region=1
     elif(region=='Southeast'):
          region=2
     elif(region=='Northwest'):
          region=3
     else:
          region=4

     if st.button('Predict'):
          pred = model.predict([[age, sex, bmi, children, smoker, region]])

          st.balloons()
          st.success('Your Insurance Cost is {}'.format(round(pred[0],2)))


if __name__ == '__main__':
     main()