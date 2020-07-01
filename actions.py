# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

import datetime
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionGreatAgain(Action):

    def name(self) -> Text:
        return "action_great_again"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        last_message = tracker.latest_message
        if (("始めまして" in last_message) or ("はじめまして" in last_message)):
            dispatcher.utter_message(text="始めまして. ^^")
        else:
            now = datetime.datetime.now()
            hour = now.hour
            if (hour < 12):
                dispatcher.utter_message(text="お早う御座います. ^^")
            elif (hour < 18):
                dispatcher.utter_message(text="こんにちは. ^^")
            else:
                dispatcher.utter_message(text="今晩は. ^^")
        return []
