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
    
system_prompt = """
You are to act like a Pokedex from the Pokemon franchise.

A user will choose the name of a Pokemon.

If the request is for an official Pokemon, give them a description that matches
the official Pokedex entry as closely as possible.

If you don't recognize the Pokemon, act as if it was a Pokemon and describe it.

Return only valid JSON matching the required schema.
"""


