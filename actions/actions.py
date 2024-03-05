# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
 #https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
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

# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher

# class ActionFallback(Action):
#     def name(self) -> Text:
#         return "action_default"

#     def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict[Text, Any]]:
#         dispatcher.utter_template("utter_default", tracker)
#         return []

# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher

# class FallbackAction(Action):
#     def name(self) -> Text:
#         return "action_default_fallback"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(template="utter_unknown")
#         return []


# from rasa_core.actions.action import Action
# from rasa_core.interpreter import RasaInterpreter
# # # Update the import statement in actions.py
# # #from rasa.nlu.interpreter import RasaNLUInterpreter

# class FallbackAction(Action):
#     def name(self):
#         return "action_fallback"

#     def run(self, dispatcher, tracker, domain):
#         interpreter = RasaInterpreter(tracker)
#         message = "Sorry, I can't help you with that right now."
#         dispatcher.utter_message(text=message)


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import Restarted
from rasa_sdk.executor import CollectingDispatcher

class ActionRestartConversation(Action):
    def name(self) -> Text:
        return "action_restart_conversation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [Restarted()]


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import Restarted
from rasa_sdk.executor import CollectingDispatcher

class ActionGoodbye(Action):
    def name(self) -> Text: 
        return "action_goodbye"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Goodbye! Have a great day.")
        # Add any cleanup tasks here if needed
        return [Restarted()]
