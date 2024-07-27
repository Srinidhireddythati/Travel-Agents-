from textwrap import dedent
from travel.openai_model import call_openai

def generate_itinerary(destination, num_days, api_key):
    prompt = dedent(f"""
    Given a travel destination and the number of days the user wants to travel for,
    generate a detailed itinerary including the best travel destinations, activities, and accommodations.

    Destination: {destination}
    Number of days: {num_days}

    Please provide a detailed itinerary.
    """)
    response = call_openai(prompt, api_key)
    return response
