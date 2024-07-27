import streamlit as st
from travel.pipeline import run_travel_planner

# Set up the Streamlit app
st.title("AI Travel Planner(Agent) ✈️")
st.caption("Plan your next adventure with AI Travel Planner by researching and planning a personalized itinerary on autopilot using GPT-4")

# Get OpenAI API key from user
openai_api_key = st.text_input("Enter OpenAI API Key to access GPT-4", type="password")

if openai_api_key:
    destination = st.text_input("Where do you want to go?")
    num_days = st.number_input("How many days do you want to travel for?", min_value=1, max_value=30, value=7)

    if st.button("Generate Itinerary"):
        with st.spinner("Processing..."):
            st.write("Generating itinerary...")  # Debug print
            itinerary = run_travel_planner(openai_api_key, destination, num_days)
            st.write("Itinerary generated.")  # Debug print

            if "An error occurred" in itinerary:
                st.error(itinerary)
            else:
                st.write(itinerary)
