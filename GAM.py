import streamlit as st
import random

st.title('Welcome to Number guessing game')

num = random.randrange(1, 4)

txt_guess = int(st.text_input('Enter a number between 1 and 4: ', 1))

btn_start = st.button('start again')

btn_guess = st.button('Make a guess')

if btn_guess:
    if txt_guess == num:
        st.write('You win')
        st.balloons()
    else:
        
        st.write('sorry. Try again.')
        
btn_show = st.button('show Number')

if btn_show:
    st.write('The number is ', num)


    
