from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

from util.file_util import *

BASE_FOLDER = 'resources/avatars/'


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

class ActionFindAvatar(Action):

    def name(self) -> Text:
        print("Action action_find_avatar")
        return "action_find_avatar"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        style = tracker.get_slot("style")
        gender = tracker.get_slot("gender")

        path = BASE_FOLDER + '/' + style + '/' + gender
        file = get_random_file(path)

        dispatcher.utter_message(template="utter_avatar_found")

        url = 'http://localhost:5000/get/' + file;
        #
        # dispatcher.utter_message(attachment={
        #     "type": "image",
        #     "payload": {
        #         "title": "Avatar",
        #         "src": f"{url}"
        #     }
        # })

        dispatcher.utter_image_url(url)

        return []
