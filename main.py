import random, os


def genText():
    with open("outtext.txt", "r") as f:
        rl = f.readlines()
        i1 = random.randint(0, len(rl)-1)
        i2 = i1 + 1 if not i1 + 1 == len(rl) else il - 1
        return "{l1}{l2}".format(l1=rl[i1], l2=rl[i2])


class CoinBot:

    # Create a constant that contains the default text for the message
    COIN_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Pretending to be Matthew...."
            ),
        },
    }

    # The constructor for the class. It takes the channel name as the a
    # parameter and then sets it as an instance variable
    def __init__(self, channel):
        self.channel = channel

    # Generate a random number to simulate flipping a coin. Then return the
    # crafted slack payload with the coin flip message.
    def _flip_coin(self):
        results = genText()
        text = f"{results}"

        return {"type": "section", "text": {"type": "mrkdwn", "text": text}},

    # Craft and return the entire message payload as a dictionary.
    def get_message_payload(self):
        return {
            "channel": self.channel,
            "blocks": [
                self.COIN_BLOCK,
                *self._flip_coin(),
            ],
        }