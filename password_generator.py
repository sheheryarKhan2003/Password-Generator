
import streamlit as st 
import random 
import string

def generate_password(Length,use_digits,use_special):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits #(0-9) if selected

    if use_special:
        characters += string.punctuation  # (!,@,#,$,%,^,&,*)
        
    return ''.join(random.choice(characters) for _ in range(Length))

st.title("Password Generator")

Length = st.slider("Select Password Length",min_value=6,max_value=32,value=12)

use_digits = st.checkbox("Include Digits")

use_special =st.checkbox("Include Special Characters")

if st.button("Generate Password"):
    Password = generate_password(Length,use_digits,use_special)
    st.write(f"Generated Password: `{Password}`")

st.write("--------------------------------")

st.write("Build with by [Maleeha](https://github.com/Maleeha)")
