import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon="🤖")

st.title("Password Strength Checker🔥🔒")
st.markdown("""
**Create passwords that protect what matters.**  
This tool helps you evaluate the strength of your password and provides clear suggestions to improve it.  

**Strong passwords** are your first line of defense—lets make sure yours is up to the task!
""")

password = st.text_input("Enter Your Password", type="password")

feedback = []

score = 0

# Strength Bar Display Function
def show_strength_bar(score):
    colors = {
        0: ("Weak", "red"),
        1: ("Weak", "orange"),
        2: ("Medium", "yellow"),
        3: ("Medium", "lightgreen"),
        4: ("Strong", "green"),
    }
    strength, color = colors[score]
    st.markdown(f"### Strength: **{strength}**")
    st.progress(score / 4)

if password:
    if len(password) >= 8:
        score +=1
    else :
        feedback.append("🔹Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌Password should contain both upper and lower case characters!.")
    
    if re.search(r'\d', password):
        score += 1
    else :
        feedback.append("❌Password should contain at least one digit.")

    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:
        feedback.append("❌Password should contain at least one special character(!@#$%^&*).")

        # Show strength bar
    show_strength_bar(score)

    if score == 4:
        feedback.append("### ✅Your Password is strong!🎇")
    elif score == 3:
        feedback.append("### 🔵Your Password is medium strength. It could be stronger!!☺")
    else:
        feedback.append("### 🔴Your Password is weak!☠ Please make it stronger..🔨")

    if feedback:
        st.markdown("## Improvement Suggestions!")
        for tip in feedback:
            st.write(tip)
else:
    st.info("Please Enter Your Password to get started!😎")