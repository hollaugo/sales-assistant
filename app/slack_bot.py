import os
from slack_bolt.adapter.fastapi import SlackRequestHandler
from slack_bolt import App
from dotenv import load_dotenv
from langserve import RemoteRunnable

load_dotenv()

slack_app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

# Initialize RemoteRunnable with your LangChain service URL
remote_runnable = RemoteRunnable("http://localhost:8000/")

def fetch_response(query):
    # Use the synchronous invoke method
    result = remote_runnable.invoke({"input": query})
    return result

@slack_app.message("")
def handle_message_events(message, say, client):
    channel_id = message['channel']
    thread_ts = message['ts']
    query = message.get("text")

    # Post an initial message
    result = client.chat_postMessage(channel=channel_id, text=":mag: Searching...", thread_ts=thread_ts)
    thread_ts = result["ts"]
    
    # Fetch response using RemoteRunnable
    response = fetch_response(query)

    
    # Process response and send follow-up message
    output_text = response['output']  # Adjust according to your actual response structure

    #Update the initial message with the response and use mrkdown block section to return the response in Slack markdown format
    client.chat_update(
        channel=channel_id,
        ts=thread_ts,
        text=output_text,
        blocks=[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": output_text
                }
            }
        ]
    )



handler = SlackRequestHandler(slack_app)
