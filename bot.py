import requests
import os

def send_poll():
    # We use 'os.environ' to keep your keys secret
    id_instance = os.environ.get('ID_INSTANCE')
    api_token = os.environ.get('API_TOKEN')
    chat_id = os.environ.get('CHAT_ID')
    
    url = f"https://api.green-api.com/waInstance{id_instance}/sendPoll/{api_token}"
    
    payload = {
        "chatId": chat_id,
        "message": "Good morning! Are you joining the gym today?",
        "options": [
            {"Yes": "Yes"},
            {"No": "No"}
        ],
        "multipleAnswers": False
    }
    
    response = requests.post(url, json=payload)
    print(f"Response: {response.status_code}, {response.text}")

if __name__ == "__main__":
    send_poll()
