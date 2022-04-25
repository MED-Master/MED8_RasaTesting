# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from Plots import plotting
from foldercreation import folder


class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_hello_world"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="Hello World!")

         return []


class PlotTimelineOfDNT(Action):#1

    def name(self) -> Text:
        return "PlotTimelineOfDNT"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Here is the timeline for DNT!")
        plotting.linePlot("Dates", "DNT (Median)", "Country", "Hospital", plotting.df, folder.baseFolder)

        return []

class PlotlocalComparisonsTimelineOfDNT(Action): #2

    def name(self) -> Text:
        return "PlotlocalComparisonsTimelineOfDNT"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Here is the timeline for DNT with other local hospitals!")
        plotting.linePlot("Dates", "DNT (Median)", "Country", "Hospital", plotting.df, folder.baseFolder)

        return []


class PlotAnnotateDNTLocalHospitals(Action): #4

    def name(self) -> Text:
        return "PlotAnnotateDNTLocalHospitals"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Here is the annotations with the DNT of local hospitals")
        plotting.linePlot("Dates", "DNT (Median)", "Country", "Hospital", plotting.df, folder.baseFolder)


        return []

class PlotCompareToCounty(Action): #6

    def name(self) -> Text:
        return "PlotCompareToCounty"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Your average DNT is similar to South Korea and higher than Iran by 3 procent point.")
        plotting.linePlot("Dates", "DNT (Mean)", "Country", "Hospital", plotting.df, folder.baseFolder)


        return []

class PlotPatientOfImpact(Action): #9

    def name(self) -> Text:
        return "PlotPatientOfImpact"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="The biggest reason I can see can be the increased amount of patients you have had recently.")
        plotting.linePlot("Dates", "DNT (Mean)", "Country", "Hospital", plotting.df, folder.baseFolder)


        return []

class PlotCompareLocalHospitals(Action): #10

    def name(self) -> Text:
        return "PlotCompareLocalHospitals"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Your Mean DNT is 5 min higher than the average of local hospitals.")
        plotting.linePlot("Dates", "DNT (Median)", "Country", "Hospital", plotting.df, folder.baseFolder)


        return []