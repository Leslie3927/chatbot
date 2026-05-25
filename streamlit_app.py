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

pokedex_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "entry_number": {"type": "string"},
        "stats": {
            "type": "object",
            "properties": {
                "hp": {"type": "integer", "minimum": 1, "maximum": 999},
                "attack": {"type": "integer", "minimum": 1, "maximum": 999},
                "defense": {"type": "integer", "minimum": 1, "maximum": 999},
                "special attack": {"type": "integer", "minimum": 1, "maximum": 999},
                "special defense": {"type": "integer", "minimum": 1, "maximum": 999},
                "speed": {"type": "integer", "minimum": 1, "maximum": 999}
            },
            "required": [
                "hp",
                "attack",
                "defense",
                "special attack",
                "special defense",
                "speed"
            ],
            "additionalProperties": False
        },
        "description": {"type": "string"},
        "details": {
            "type": "object",
            "properties": {
                "height": {"type": "string"},
                "weight": {"type": "string"},
                "gender": {"type": "string"},
                "category": {"type": "string"},
                "abilities": {
                    "type": "array",
                    "items": {"type": "string"}
                }
            },
            "required": [
                "height",
                "weight",
                "gender",
                "category",
                "abilities"
            ],
            "additionalProperties": False
        },
        "type": {
            "type": "array",
            "items": {"type": "string"}
        },
        "weaknesses": {
            "type": "array",
            "items": {"type": "string"}
        },
        "evolutions": {"type": "string"}
    },
    "required": [
        "name",
        "entry_number",
        "stats",
        "description",
        "details",
        "type",
        "weaknesses",
        "evolutions"
    ],
    "additionalProperties": False
}


def show_pokedex_entry(page_json):
    print(page_json["name"] + " " + page_json["entry_number"])
    print()

    print("STATS")
    print("\tHP: " + str(page_json["stats"]["hp"]))
    print("\tAttack: " + str(page_json["stats"]["attack"]))
    print("\tDefense: " + str(page_json["stats"]["defense"]))
    print("\tSpecial Attack: " + str(page_json["stats"]["special attack"]))
    print("\tSpecial Defense: " + str(page_json["stats"]["special defense"]))
    print("\tSpeed: " + str(page_json["stats"]["speed"]))
    print()

    print(page_json["description"])
    print()

    print("DETAILS")
    print("\tHeight:", page_json["details"]["height"])
    print("\tWeight:", page_json["details"]["weight"])
    print("\tGender:", page_json["details"]["gender"])
    print("\tCategory:", page_json["details"]["category"])

    print("\tAbilities:")
    for ability in page_json["details"]["abilities"]:
        print("\t\t" + ability)

    print()
    print("TYPE")
    for pokemon_type in page_json["type"]:
        print("\t" + pokemon_type)

    print()
    print("WEAKNESSES")
    for weakness in page_json["weaknesses"]:
        print("\t" + weakness)

    print()
    print("EVOLUTIONS")
    print(page_json["evolutions"])
    print()


def create_pokedex_entry(pokemon_name):
    response = client.responses.create(
        model="gpt-5.4-mini",
        instructions=system_prompt,
        input=f"Create a Pokedex entry for: {pokemon_name}",
        text={
            "format": {
                "type": "json_schema",
                "name": "pokedex_entry",
                "schema": pokedex_schema,
                "strict": True
            }
        }
    )

    return json.loads(response.output_text)


pokedex = {}

print("Welcome to the Pokedex!")

while True:
    page_select_prompt = """
What would you like to do?

1. View generated Pokedex entries
2. Create a new Pokedex entry
3. Search entries
4. Quit

Please select an option: """

    selection = ""

    while selection not in ["1", "2", "3"]:
        selection = input(page_select_prompt)

    if selection == "1":
        if len(pokedex) == 0:
            print("You have no Pokedex entries.")
        else:
            print("Here are all of your entries:")

            names = list(pokedex.keys())

            for i in range(len(names)):
                print(str(i + 1) + ". " + names[i])

            entry_select = 0

            while entry_select < 1 or entry_select > len(names):
                try:
                    entry_select = int(input("Please select an option: "))
                except ValueError:
                    print("Please enter a valid number.")

            selected_name = names[entry_select - 1]
            show_pokedex_entry(pokedex[selected_name])

    elif selection == "2":
        pokemon_name = input("Please enter the name of the Pokemon: ")

        try:
            pokedex[pokemon_name] = create_pokedex_entry(pokemon_name)
            print("Created!")
            show_pokedex_entry(pokedex[pokemon_name])

        except Exception as e:
            print("Something went wrong while creating the Pokedex entry.")
            print(e)

    elif selection == "4":
        print("Goodbye!")
    elif selection == "3":
        want = input("What pokemon do you want to see")
        if want in pokedex:
            print (show_pokedex_entry(pokedex[want]))
    else: 
        print("eh?")


    '''
    #ADD THE SEARCH FEATURE HERE
    elif selection == "4": #or 3


    '''
