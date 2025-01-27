import streamlit as st
from PIL import Image

st.title("Currency Converter App")
st.markdown('''this app interconvert the value of different currency''')

image = Image.open("df.jpeg")
st.image(image, width = 550, caption="Currency APP")

img= Image.open("gt.jpeg")
st.sidebar.image(img.resize((50,50)))


            
Cur = ["Dollars", "Pounds", "Euros", "Naira", "Rupees", "Yen",
        "Cedis", "Shekel", "Dinah", "Dirham"] 
rate = [1557, 1919,1621, 1, 18, 213, 102, 437, 50604, 424]

def convert_formula(num, initial, final):
    ini_id = Cur.index(initial)
    fin_id = Cur.index(final)


    value1 = rate[ini_id]
    value2 = rate[fin_id]

    result = (num * value1) / value2
    return round(result, 2) 

num = st.number_input("How much are you converting")
initial_currency = st.selectbox("what is your initial currency", Cur)
final_currency = st.selectbox("what is your final currency", Cur)

amount = convert_formula(num, initial_currency, final_currency)

if st.button("Convert"):
   st.write(amount)


   expander_bar = st.expander("About")
   expander_bar.markdown("""
                         ***python libraries:** streamlit, PIL 
                         ***credit:** App built by [sunny] ()""")
                         #C:\Program Files\Tesseract-OCR
   
     