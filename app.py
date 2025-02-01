from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

SLACK_BOT_TOKEN="<replace_with_your_token>"
SLACK_APP_TOKEN="<replace_with_your_token>"

app = App(token=SLACK_BOT_TOKEN, name="Hw Bot")

@app.event("app_home_opened")
def say_hw(message, say):
    say("hello world")


def main():
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()


if __name__ == "__main__":
    main()