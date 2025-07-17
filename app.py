# app.py
import streamlit as st
from main import generate_trophy_name # Imports your generator from main.py

# --- Page Configuration ---
st.set_page_config(
    page_title="Trophy Name Generator",
    page_icon="🏆",
    layout="wide"
)

# --- App Interface ---
st.title("🏆 Trophy Dark Name Generator")
st.write(
    "A procedural name generator that creates unique, thematic names "
    "in the somber style of the tabletop RPG *Trophy Dark*."
)
st.write("---")

# The button to generate names
if st.button("Generate a New Name"):
    # When the button is clicked, call your function and display the name
    generated_name = generate_trophy_name()
    st.success(f"**{generated_name}**")