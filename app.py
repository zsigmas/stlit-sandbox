from cmath import inf
from pickle import FALSE
import streamlit as st
import random as rn

# helpers

MAX_VAL = 20
MIN_VAL = 0
DEBUG = False

# initializing with a random number
if "mul_val" not in st.session_state:
    st.session_state["mul_val"] = [rn.randint(MIN_VAL,MAX_VAL), rn.randint(MIN_VAL,MAX_VAL)]

# callback function to change the random number stored in state
def change_number():
    st.session_state["mul_val"] = [rn.randint(MIN_VAL,MAX_VAL), rn.randint(MIN_VAL,MAX_VAL)]
    return

# app

st.title("Multiplication app")

st.write("Multiply {v1} X {v2}".format(v1 = st.session_state["mul_val"][0], v2=st.session_state["mul_val"][1]))

with st.form('Form'):
     # Looks better that st.numberinput though it is a bit less clear
    str_result = st.text_input('Input the solution')
    result = float(str_result) if str_result!="" else inf  

    # Apparently Streamlit does not read keypresses yet :(
    # https://discuss.streamlit.io/t/enter-key-press-to-submit-st-form/16939/5
    # https://docs.streamlit.io/library/api-reference/control-flow/st.form
    submit = st.form_submit_button('Send')

if submit:
    if DEBUG:
        st.write(str_result)
        st.write(result)
        st.write(result == st.session_state["mul_val"][0] * st.session_state["mul_val"][1])

    if result == st.session_state["mul_val"][0] * st.session_state["mul_val"][1]:
        st.success("Correct :)")
    else:
        st.error("Incorrect :(")

## button to generate new numbers
st.button("New multiplication?", on_click=change_number)