from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
import flask_email_util
from rasa_sdk.events import SlotSet
import zomatopy
import json


class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def run(self, dispatcher, tracker, domain):
		config = {"user_key": "75502752c8a4b706194ec22543a11dc1"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		budget = tracker.get_slot('budget')
		location_detail = zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat = d1["location_suggestions"][0]["latitude"]
		lon = d1["location_suggestions"][0]["longitude"]
		cuisines_dict = {'chinese': 25, 'italian': 55, 'north indian': 50,'south indian': 85, 'american': 1, 'mexican': 73}

		if(budget.lower() == 'low'):
			options = {'mincft': 0, 'maxcft': 300, 'sort': 'rating', 'order': 'dsc'}
		elif(budget.lower() == 'medium'):
			options = {'mincft': 300, 'maxcft': 700, 'sort': 'rating', 'order': 'dsc'}
		elif(budget.lower() == 'high'):
			options = {'mincft': 700, 'maxcft': 99999, 'sort': 'rating', 'order': 'dsc'}
		else:
			options = {'sort': 'rating', 'order': 'dsc'}

		results = zomato.restaurant_advance_search(
"", lat, lon, str(cuisines_dict.get(cuisine)), options, 5)
		d = json.loads(results)
		# d['restaurants'] = sorted(d['restaurants'], key=lambda k: k['restaurant']['user_rating']['aggregate_rating'], reverse=True)
		response = ""
		if d['results_found'] == 0:
			response = "no results found. Please try something else."
		else:
			for restaurant in d['restaurants']:
				response = response + "Found " + \
				    restaurant['restaurant']['name'] + " in " + \
				        restaurant['restaurant']['location']['address']+"\n"
		dispatcher.utter_message("-----"+response)
		return [SlotSet('location', loc), SlotSet('restaurant_found', True)]


class ActionVerifyLocation(Action):

	def name(self):
		return 'action_verify_location'

	def run(self, dispatcher, tracker, domain):
		# Fetch the user input for location
		loc = tracker.get_slot('location')
		# List of Tier 1 and Tier 2 cities
		valid_cities = ['Ahmedabad', 'Bangalore', 'Chennai', 'Delhi', 'Hyderabad', 'Kolkata', 'Mumbai', 'Pune', 'Agra', 'Ajmer', 'Aligarh', 'Amravati', 'Amritsar', 'Asansol', 'Aurangabad', 'Bareilly', 'Belgaum', 'Bhavnagar', 'Bhiwandi', 'Bhopal', 'Bhubaneswar', 'Bikaner', 'Bokaro Steel City', 'Chandigarh', 'Coimbatore', 'Cuttack', 'Dehradun', 'Dhanbad', 'Durg-Bhilai Nagar', 'Durgapur', 'Erode', 'Faridabad', 'Firozabad', 'Ghaziabad', 'Gorakhpur', 'Gulbarga', 'Guntur', 'Gurgaon', 'Guwahati', 'Gwalior', 'Hubli-Dharwad', 'Indore', 'Jabalpur', 'Jaipur', 'Jalandhar', 'Jammu', 'Jamnagar', 'Jamshedpur', 'Jhansi', 'Jodhpur', 'Kannur', 'Kanpur',
			'Kakinada', 'Kochi', 'Kottayam', 'Kolhapur', 'Kollam', 'Kota', 'Kozhikode', 'Kurnool', 'Lucknow', 'Ludhiana', 'Madurai', 'Malappuram', 'Mathura', 'Goa', 'Mangalore', 'Meerut', 'Moradabad', 'Mysore', 'Nagpur', 'Nanded', 'Nashik', 'Nellore', 'Noida', 'Palakkad', 'Patna', 'Pondicherry', 'Prayagraj', 'Raipur', 'Rajkot', 'Rajahmundry', 'Ranchi', 'Rourkela', 'Salem', 'Sangli', 'Siliguri', 'Solapur', 'Srinagar', 'Sultanpur', 'Surat', 'Thiruvananthapuram', 'Thrissur', 'Tiruchirappalli', 'Tirunelveli', 'Tiruppur', 'Ujjain', 'Bijapur', 'Vadodara', 'Varanasi', 'Vasai-Virar City', 'Vijayawada', 'Visakhapatnam', 'Vellore', 'Warangal']
		# Converting the city names into lower case for ease of comparison
		valid_cities_lc = [x.lower() for x in valid_cities]
		# If Location is provided
		if loc is not None:
			# If city provided by user is present in the list of tier 1 and tier 2 cities, continue with the search
			if loc.lower() in valid_cities_lc:
				return[SlotSet('location', loc), SlotSet('location_found', True)]
		    # If city provided by user is not present in the list of tier 1 and tier 2 cities, ask the user to provide some other city
			else:
				dispatcher.utter_message("Sorry, we do not operate in that area yet. Please try for some other city.")
				return[SlotSet('location', None), SlotSet('location_found', False)]
		else:
			dispatcher.utter_message("Sorry, I was unable to understand the location provided. Please re-enter the city again.")
			return[SlotSet('location', None), SlotSet('location_found', False)]

class ActionVerifyCuisine(Action):

    def name(self):
        return 'action_verify_cuisine'

    def run(self, dispatcher, tracker, domain):
		# Fetch the user input for cuisine
        cuisine = tracker.get_slot('cuisine')
		# List of available cuisines
        valid_cuisines = ['chinese', 'italian', 'american',
            'mexican', 'north indian', 'south indian']
		# If user has provided some values for cuisine and it is availabe, continue with the search, else ask the user to re-enter the cuisine
        if cuisine is not None:
                if cuisine.lower() in valid_cuisines:
                        return[SlotSet('cuisine', cuisine), SlotSet('cuisine_found', True)]
                else:
                    dispatcher.utter_message(
                        "Sorry, the cuisine is not available in our menu. Please try for some other cuisine.")
                    return[SlotSet('cuisine', None), SlotSet('cuisine_found', False)]
        else:
                dispatcher.utter_message(
                    "Sorry, I was unable to understand the cuisine provided. Please re-enter the cuisine again.")
                return[SlotSet('cuisine', None), SlotSet('cuisine_found', False)]


class ActionVerifyBudget(Action):

	def name(self):
		return 'action_verify_budget'

	def run(self, dispatcher, tracker, domain):
		# Fetch the user input for budget
		budget = tracker.get_slot('budget')
		# List of available budget options
		valid_budget = ['low', 'medium', 'high']
		# If user has provided some values for budget, continue with the search, else ask the user to re-enter the budget
		if budget is not None:
			if(budget.lower() in valid_budget):
				return[SlotSet('budget', budget),SlotSet('budget_found',True )]				
			else:
				dispatcher.utter_message("Sorry, we cannot understand the budget option provided. Please re-enter the budget.")
				return[SlotSet('budget',None),SlotSet('budget_found',False)]
		else:
				dispatcher.utter_message("Sorry, I did not receive any input for the budget. Please re-enter.")
				return[SlotSet('budget', None),SlotSet('budget_found', False)]	

class ActionSendEmailWithTop10(Action):
	def name(self):
		return 'action_send_email'
		
	def run(self, dispatcher, tracker, domain):
		# Fetch the top 10 restaurants from zomato
		config = {"user_key":"75502752c8a4b706194ec22543a11dc1"}
		# Initialize the zomato app by passing authentication keys
		zomato = zomatopy.initialize_app(config)
		# Fetch the information provided by the user as an input in conversation with the bot like location, cuisine and budget
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		budget = tracker.get_slot('budget')
		# Fetch the latitude and longitude as those are required to be passed as input parameters to the "restaurant_search" function
		location_detail = zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat = d1["location_suggestions"][0]["latitude"]
		lon = d1["location_suggestions"][0]["longitude"]
		cuisines_dict = {'chinese':25,'italian':55,'north indian':50,'south indian':85,'american':1,'mexican':73}		
		if(budget.lower() == 'low'):
			options = {'mincft':0, 'maxcft':300, 'sort':'rating', 'order':'dsc'}
		elif(budget.lower() == 'medium'):
			options = {'mincft':300, 'maxcft':700, 'sort':'rating', 'order':'dsc'}
		elif(budget.lower() == 'high'):
			options = {'mincft':700, 'maxcft':99999, 'sort':'rating', 'order':'dsc'}
		else:
			options = {'sort':'rating', 'order':'dsc'}
			
		results=zomato.restaurant_advance_search("", lat, lon, str(cuisines_dict.get(cuisine)), options, 10)
		d = json.loads(results)
      
        # Generate the email body with the search results from zomato
        # The format should be: {restaurant_name} in {restaurant_address} has been rated {rating}.
		email_msg = ""
		counter = 1
		if d['results_found'] == 0:
			email_msg = email_msg + "Sorry, we regret to inform you that no matching restaurants could be located with your preferred search criteria"
		else:
			email_msg = "As requested by you, sharing the top 10 " + cuisine + " restaurants in your preferred location" + loc + ". The restaurants have been sorted based on customer ratings:\n"
			for restaurant in d['restaurants']:
				email_msg = email_msg + "[" + str(counter) + "]." + str(restaurant['restaurant']['name']) + " in " + str(restaurant['restaurant']['location']['address']) + " has been rated " + str(restaurant['restaurant']['user_rating']['aggregate_rating']) + "\n"
				counter = counter + 1
				
		email_msg = email_msg + "\n\n" + "Bon Apetit!!" + "\n\n" + "Foodie"

        # Invoke the email utility for sending mail
		email_subj = "Top 10 " + cuisine + " restaurants in your preferred location" + loc
		email_id = tracker.get_slot('emailid')
		email_to = [email_id]
		
		response = flask_email_util.trigger_mail(email_subj, email_to, email_msg)
		dispatcher.utter_message(response)
		return[SlotSet('emailid', email_id)]
