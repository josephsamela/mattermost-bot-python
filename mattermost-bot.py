import requests
import json

def main():
    # Specify Mattermost webhook url to send message
    url = "https://mattermost.domain.com/hooks/bktqttmt3ifbbcg1g6d9qekkmy"

    # Create message payload per mattrermost API documentation:
    # https://docs.mattermost.com/developer/webhooks-incoming.html#parameters-and-formatting
    messages = [
        {
             'username': 'Obi-Wan Kenobi',
             'icon_url': 'https://bit.ly/2nQZ6vg',
             'text'    : 'It\'s over Anakin! I have the high ground.'
        },
        {
          'username': 'Anakin Skywalker',
          'icon_url': 'https://bit.ly/2njSENj',
          'text': 'You underestimate my power!'
        }
    ]

    # Post above messages!
    for message in messages:
        post_to_mattermost(url, json.dumps(message))

def post_to_mattermost(url, message):
    # Send payload as HTTP Post Request to Webhook URL
    r = requests.post(
        url,
        data=message
    )
    r.raise_for_status()

if (__name__) == '__main__':
    main()
