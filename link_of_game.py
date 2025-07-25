import streamlit as st
import random

st.title("🐍💧🔫 Snake Water Gun Game")

b = st.selectbox("Choose your weapon:", ["snake", "water", "gun"])

if st.button("Play"):
    options = ["snake", "water", "gun"]
    a = random.choice(options)
    st.write(f"Python chose: **{a}**")

    if (a == "snake" and b == "water") or (a == "water" and b == "gun") or (a == "gun" and b == "snake"):
        st.error("Python wins!")
    elif a == b:
        st.info("It's a tie!")
    else:
        st.success("You win!")
