import requests
import time

BACKEND_URL = "http://backend:8000"


def agent(prompt):
    for attempt in range(10):
        try:
            response = requests.post(
                f"{BACKEND_URL}/imageGeneration/", params={"prompt": prompt}, timeout=5
            )
            response.raise_for_status()
            result = response.json()
            return result["message"]
        except (requests.ConnectionError, requests.exceptions.HTTPError) as e:
            print(f"[Attempt {attempt+1}] Backend not ready yet, retrying in 3s...")
            time.sleep(3)
    raise Exception("Failed to connect to backend after 10 attempts.")


prompt = "Generate a photorealistic image of a cuddly cat wearing a green hat."
print(agent(prompt))
