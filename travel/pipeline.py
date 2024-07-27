from travel.agents import TravelPlannerAgent

def run_travel_planner(api_key, destination, num_days):
    agent = TravelPlannerAgent(api_key)
    return agent.create_itinerary(destination, num_days)
