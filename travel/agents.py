from travel.tasks import generate_itinerary

class TravelPlannerAgent:
    def __init__(self, api_key):
        self.api_key = api_key

    def create_itinerary(self, destination, num_days):
        return generate_itinerary(destination, num_days, self.api_key)
