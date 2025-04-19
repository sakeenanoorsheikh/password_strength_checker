# Password Strength Checker:

import streamlit as st
import re 

st.set_page_config(page_title = "Password Strength Checker", page_icon="🔒")

st.title("🔐Password Strength Checker")
st.markdown("""
## Welcome to the ultimate password strength checker!👋
use this simple tool to check the strength of your password and get suggestions on how to make it stronger.
            we will give you helpfil tips to create a **Strong Password** 🔒""")

password = st.text_input("Enter Your Password", type="password")

feedback = []

score = 0

if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌Password should be at least 8 cheracters long.")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1  
    else:
        feedback.append("❌Password should contain both upper and lower case characters.")    

# 0-9 tak num show k liye

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌Password should contain at least one digit.")  

    if re.search(r'[!@#$%&*]', password):
        score += 1
    else:
        feedback.append("❌Password should contain at least one special charactar(!@#$%&*).")          

    if score == 4:
        feedback.append("✅Your password is strong!🎉")
    elif score == 3:
        feedback.append("🟡Your password is medium strength. It could be stronger.") 
    else:
        feedback.append("🔴Your password is weak. Please make it stronger.")      

    if feedback:
        st.markdown("## Improvement Suggestions💫")
        for tip in feedback:
            st.write(tip)     

else:
    st.info("Please enter your password to get started.")