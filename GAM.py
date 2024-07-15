import streamlit as st
import random

st.title('Welcome to Number guessing game')

num = random.randrange(1, 4)

txt_guess = int(st.text_input('Enter a number between 1 and 4: ', 1))

num1 = random.randrange(5, 7)

txt_guess = int(st.text_input('Enter a number between 5 and 7: ', 1))

btn_start = st.button('start again')

btn_guess = st.button('Make a guess')

if btn_guess:
    if txt_guess == num or txt_guess2 == num1:
        st.write('You win')
        st.balloons()
    else:
        html_str = f""" <h1 style='text-align: left; color: #FF4433;'> sorry. Try again. </h1> """
        st.markdown(html_str, unsafe_allow_html=True)
        
btn_show = st.button('show Number')

if btn_show:
    st.write('The number is ', num, 'and ', num1)


    
