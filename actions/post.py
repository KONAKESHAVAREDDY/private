
from st2common.runners.base_action import Action
import requests
import json

class CreateServiceNowTicketAction(Action):
    def run(self):
        # ServiceNow instance details
        instance_url = "https://dev149795.service-now.com/"
        username = "admin"
        password = "grBDH*m7bH0@"

        # ServiceNow API endpoint
        api_url = f"{instance_url}/api/now/table/incident"

        # Headers for the API request
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        # Create payload for the ticket
        payload = {
            "short_description": "short_description",
            "description": "description",
            "caller_id": "caller_id"
            # Add more fields as required
        }

        response = requests.post(api_url, auth=(username, password), headers=headers, json=payload)
