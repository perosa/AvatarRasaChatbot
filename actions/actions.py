from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import string
import random

import os
import logging

#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


try:
    logging.basicConfig(level=logging.DEBUG)
except Exception as e:
    logging.exception("Error configuring logging")


class ActionFindAvatar(Action):

    def name(self) -> Text:
        logging.debug("Action action_find_avatar")
        return "action_find_avatar"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        style = tracker.get_slot("style")
        gender = tracker.get_slot("gender")

        dispatcher.utter_message(template="utter_avatar_found")

        url = get_avatar_svc() + 'get/' + style + '/' + gender + '/' + id_generator()

        logging.info(f"image {url}")
        logging.info(f"sender_id {tracker.sender_id}")

        dispatcher.utter_message(image=url)

        return []


class ActionProcessFeedback(Action):

    def name(self) -> Text:
        logging.debug("Action action_process_feedback")
        return "action_process_feedback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        feedback = tracker.get_slot("feedback")
        logging.info(f"feedback {feedback}")

        if feedback == 'Good':
            dispatcher.utter_message(template="utter_goodbye_after_positive_feedback")
        else:
            dispatcher.utter_message(template="utter_goodbye_after_negative_feedback")

        return []


def get_avatar_svc():
    """
    Retrieves host serving the Avatar images
    :return:
    """
    return str(os.environ.get("AVATAR_SVC", 'http://localhost:5000/'))


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
