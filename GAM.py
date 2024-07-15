import streamlit as st
import random

st.title('Welcome to Number guessing game')

st.write('Choose one...')

btn_choice1 = st.button('guess b/w 1 and 4')
if btn_choice1:
    num = random.randrange(1, 5)

    txt_guess = int(st.text_input('Enter a number between 1 and 4: ', 1))

     if txt_guess:
        txt_guess = int(txt_guess)
        if txt_guess == num:
        st.write('You win')
        st.balloons()
    else:
        html_str = f""" <h1 style='text-align: left; color: #FF4433;'> sorry. Try again. </h1> """
        st.markdown(html_str, unsafe_allow_html=True)   
    st.write('The number is ', num)




btn_choice2 = st.button('guess b/w 5 and 7')
if btn_choice2: 

    num1 = random.randrange(5, 8)

    txt_guess2 = int(st.text_input('Enter a number between 5 and 7: ', 1))
    
        if txt_guess2:
            txt_guess2 = int(txt_guess2)
            if txt_guess2 == num1:
                st.write('You win')
                st.balloons()
        else:
            html_str = f""" <h1 style='text-align: left; color: #FF4433;'> sorry. Try again. </h1> """
            st.markdown(html_str, unsafe_allow_html=True)
st.write('The number is', num1)


with st.expander("Help..."):
    st.write('''
 This game will randomly choose a number between 1 and 4 for the first box, and 5 and 7 for the second box.
 Try to guess a number between 1 and 4 for the first box, and 5 and 7 for the second box to see if you can guess the same number.
 Press the button make a guess and if you get either of them right you win''')


    
