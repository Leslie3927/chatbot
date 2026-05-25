import streamlit as st
import json
import os
from openai import OpenAI
"""
# Hello World, Streamlit!

This is a website to demonstrate Streamlit's API.
You can stop looking at this now.

Please.
"""

with st.form("my_form"):
    fav_color = st.selectbox(
        "Choose a pokemon",
        [
            "Macargo",
            "Cinderace",
            "Fidough",
            "Turtwig",
            "Kyogre",
            "Poipole"
        ]
    )
    client = OpenAI(
    api_key = "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"
)
    
system_prompt = """
You are to act like a Pokedex from the Pokemon franchise.

A user will submit the name of a Pokemon.

If the request is for an official Pokemon, give them a description that matches
the official Pokedex entry as closely as possible.

If you don't recognize the Pokemon, act as if it was a Pokemon and describe it.

Return only valid JSON matching the required schema.
"""

st.form_submit_button()
