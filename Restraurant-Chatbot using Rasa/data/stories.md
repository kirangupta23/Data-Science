## complete path-1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_verify_location
    - slot{"location_found": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
  	- action_verify_cuisine
    - slot{"cuisine_found": true}
	- utter_ask_budget
* restaurant_search{"budget": "Low"}
    - slot{"budget": "Low"}
	- action_verify_budget
    - slot{"budget": "Low"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"restaurant_found": true}
	- utter_ask_email
* affirm
    - utter_ask_emailid
* get_results_in_mail{"emailid": "abc.xyz@gmail.com"}
    - slot{"emailid": "abc.xyz@gmail.com"}
    - action_send_email
	  - utter_sent
    - action_restart

## complete path-2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_verify_location
    - slot{"location_found": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
	- action_verify_cuisine
    - slot{"cuisine": "American"}
    - slot{"cuisine_found": true}
	- utter_ask_budget
* restaurant_search{"budget": "Medium"}
    - slot{"budget": "Medium"}
    - action_verify_budget
    - slot{"budget": "Medium"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - slot{"restaurant_found": true}
    - utter_ask_email
* deny{"deny": "no"}
    - utter_goodbye
	- action_restart

## complete path 3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Agra"}
    - slot{"location": "Agra"}
    - action_verify_location
    - slot{"location_found": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
	- action_verify_cuisine
    - slot{"cuisine": "North Indian"}
    - slot{"cuisine_found": true}
	- utter_ask_budget
* restaurant_search{"budget": "High"}
    - slot{"budget": "High"}
	- action_verify_budget
    - slot{"budget": "High"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"location": "Agra"}
    - slot{"restaurant_found": true}
	- utter_ask_email
* affirm
    - utter_ask_emailid
* get_results_in_mail{"emailid": "kiran.gup@gmail.com"}
    - slot{"emailid": "kiran.gup@gmail.com"}
    - action_send_email
    - slot{"emailid": "kiran.gup@gmail.com"}
	  - utter_sent
    - action_restart	


## complete_story_4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Noida"}
    - slot{"location": "Noida"}
    - action_verify_location
    - slot{"location": "Noida"}
    - slot{"location_found": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_verify_cuisine
    - slot{"cuisine": "mexican"}
    - slot{"cuisine_found": true}
    - utter_ask_budget
* restaurant_search{"budget": "Low"}
    - slot{"budget": "Low"}
	- action_verify_budget
    - slot{"budget": "Low"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"location": "Noida"}
    - slot{"restaurant_found": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* get_results_in_mail{"emailid": "kiran.gup@gmail.com"}
    - slot{"emailid": "kiran.gup@gmail.com"}
    - action_send_email
    - slot{"emailid": "kiran.gup@gmail.com"}
    - utter_sent
    - action_restart

## complete_story_5
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_verify_location
    - slot{"location": "Delhi"}
    - slot{"location_found": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_verify_cuisine
    - slot{"cuisine_found": true}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "High"}
    - slot{"budget": "High"}
	- action_verify_budget
    - slot{"budget": "High"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"restaurant_found": true}
    - utter_ask_email
* get_results_in_mail{"emailid": "mekirangupta@gmail.com"}
    - slot{"emailid": "mekirangupta@gmail.com"}
    - action_send_email
    - slot{"emailid": "mekirangupta@gmail.com"}
    - utter_sent
* goodbye
    - action_restart


## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_verify_location
    - slot{"location": "Delhi"}
    - slot{"location_found": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_verify_cuisine
    - slot{"cuisine": "american"}
    - slot{"cuisine_found": true}
    - utter_ask_budget
* restaurant_search{"budget": "Medium"}
    - slot{"budget": "Medium"}
    - action_verify_budget
    - slot{"budget": "Medium"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"restaurant_found": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* get_results_in_mail{"emailid": "mekirangupta@gmail.com"}
    - slot{"emailid": "mekirangupta@gmail.com"}
    - action_send_email
    - slot{"emailid": "mekirangupta@gmail.com"}
    - utter_sent
    - action_restart

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_verify_location
    - slot{"location": "Kolkata"}
    - slot{"location_found": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_verify_cuisine
    - slot{"cuisine": "mexican"}
    - slot{"cuisine_found": true}
    - utter_ask_budget
* restaurant_search{"budget": "High"}
    - slot{"budget": "High"}
    - action_verify_budget
    - slot{"budget": "High"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"restaurant_found": true}
    - utter_ask_email
* deny{"deny": "no"}
    - utter_goodbye
    - action_restart

## interactive_story_3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "jAIPUR"}
    - slot{"location": "jAIPUR"}
    - action_verify_location
    - slot{"location": "jAIPUR"}
    - slot{"location_found": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_verify_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_found": true}
    - utter_ask_budget
* restaurant_search{"budget": "Medium"}
    - slot{"budget": "Medium"}
    - action_verify_budget
    - slot{"budget": "Medium"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"location": "jAIPUR"}
    - slot{"restaurant_found": true}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart

## interactive_story_4
* greet
    - utter_greet
* restaurant_search{"location": "Ajmer"}
    - slot{"location": "Ajmer"}
    - action_verify_location
    - slot{"location": "Ajmer"}
    - slot{"location_found": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_verify_cuisine
    - slot{"cuisine": "South Indian"}
    - slot{"cuisine_found": true}
    - utter_ask_budget
* restaurant_search{"budget": "Medium"}
    - slot{"budget": "Medium"}
    - action_verify_budget
    - slot{"budget": "Medium"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"restaurant_found": true}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart

## interactive_story_5
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Amritsar"}
    - slot{"location": "Amritsar"}
    - action_verify_location
    - slot{"location": "Amritsar"}
    - slot{"location_found": true}
    - action_verify_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_found": true}
    - utter_ask_budget
* restaurant_search{"budget": "Low"}
    - slot{"budget": "Low"}
    - action_verify_budget
    - slot{"budget": "Low"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"restaurant_found": true}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart

## interactive_story_6
* greet
    - utter_greet
* restaurant_search{"location": "Ajmer"}
    - slot{"location": "Ajmer"}
    - action_verify_location
    - slot{"location": "Ajmer"}
    - slot{"location_found": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_verify_cuisine
    - slot{"cuisine": "american"}
    - slot{"cuisine_found": true}
    - utter_ask_budget
* restaurant_search{"budget": "High"}
    - slot{"budget": "High"}
    - action_verify_budget
    - slot{"budget": "High"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"location": "Ajmer"}
    - slot{"restaurant_found": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* get_results_in_mail{"emailid": "mekirangupta@gmail.com"}
    - slot{"emailid": "mekirangupta@gmail.com"}
    - action_send_email
    - slot{"emailid": "mekirangupta@gmail.com"}
    - utter_sent
    - action_restart

## interactive_story_7
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "Varanasi"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Varanasi"}
    - action_verify_location
    - slot{"location": "Varanasi"}
    - slot{"location_found": true}
    - action_verify_cuisine
    - slot{"cuisine": "mexican"}
    - slot{"cuisine_found": true}
    - utter_ask_budget
* restaurant_search{"budget": "Medium"}
    - slot{"budget": "Medium"}
    - action_verify_budget
    - slot{"budget": "Medium"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"restaurant_found": true}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart

## interactive_story_8
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Ujjain"}
    - slot{"location": "Ujjain"}
    - action_verify_location
    - slot{"location": "Ujjain"}
    - slot{"location_found": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_verify_cuisine
    - slot{"cuisine": "Italian"}
    - slot{"cuisine_found": true}
    - utter_ask_budget
* restaurant_search{"budget": "Medium"}
    - slot{"budget": "Medium"}
    - action_verify_budget
    - slot{"budget": "Medium"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"location": "Ujjain"}
    - slot{"restaurant_found": true}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart

## interactive_story_9
* greet
    - utter_greet
* restaurant_search{"budget": "High", "location": "Lucknow"}
    - slot{"budget": "High"}
    - slot{"location": "Lucknow"}
    - action_verify_location
    - slot{"location": "Lucknow"}
    - slot{"location_found": true}
    - action_verify_budget
    - slot{"budget": "High"}
    - slot{"budget_found": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_verify_cuisine
    - slot{"cuisine": "South Indian"}
    - slot{"cuisine_found": true}
    - action_search_restaurants
    - slot{"location": "Lucknow"}
    - slot{"restaurant_found": true}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart

## interactive_story_10
* greet
    - utter_greet
* restaurant_search{"location": "Rajkot"}
    - slot{"location": "Rajkot"}
    - action_verify_location
    - slot{"location": "Rajkot"}
    - slot{"location_found": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_verify_cuisine
    - slot{"cuisine": "american"}
    - slot{"cuisine_found": true}
    - utter_ask_budget
* restaurant_search{"budget": "Low"}
    - slot{"budget": "Low"}
    - action_verify_budget
    - slot{"budget": "Low"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"location": "Rajkot"}
    - slot{"restaurant_found": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* get_results_in_mail{"emailid": "mekirangupta@gmail.com"}
    - slot{"emailid": "mekirangupta@gmail.com"}
    - action_send_email
    - slot{"emailid": "mekirangupta@gmail.com"}
    - utter_sent
    - action_restart

## interactive_story_11
* greet
    - utter_greet
* restaurant_search{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - action_verify_location
    - slot{"location": "Nashik"}
    - slot{"location_found": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_verify_cuisine
    - slot{"cuisine": "North Indian"}
    - slot{"cuisine_found": true}
    - utter_ask_budget
* restaurant_search{"budget": "Low"}
    - slot{"budget": "Low"}
    - action_verify_budget
    - slot{"budget": "Low"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"location": "Nashik"}
    - slot{"restaurant_found": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* get_results_in_mail{"emailid": "mekirangupta@gmail.com"}
    - slot{"emailid": "mekirangupta@gmail.com"}
    - action_send_email
    - slot{"emailid": "mekirangupta@gmail.com"}
    - utter_sent
    - action_restart

## interactive_story_12
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* deny{"location": "nagpur"}
    - slot{"location": "nagpur"}
    - action_verify_location
    - slot{"location": "nagpur"}
    - slot{"location_found": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_verify_cuisine
    - slot{"cuisine": "North Indian"}
    - slot{"cuisine_found": true}
    - utter_ask_budget
* restaurant_search{"budget": "Low"}
    - slot{"budget": "Low"}
    - action_verify_budget
    - slot{"budget": "Low"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"location": "nagpur"}
    - slot{"restaurant_found": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* get_results_in_mail{"emailid": "mekirangupta@gmail.com"}
    - slot{"emailid": "mekirangupta@gmail.com"}
    - action_send_email
    - slot{"emailid": "mekirangupta@gmail.com"}
    - utter_sent
    - action_restart

## interactive_story_13
* restaurant_search{"budget": "cheap", "location": "Vellore", "cuisine": "North Indian"}
    - slot{"budget": "cheap"}
    - slot{"cuisine": "North Indian"}
    - slot{"location": "Vellore"}
    - action_verify_location
    - slot{"location": "Vellore"}
    - slot{"location_found": true}
    - action_verify_cuisine
    - slot{"cuisine": "North Indian"}
    - slot{"cuisine_found": true}
    - action_verify_budget
    - slot{"budget": "cheap"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"location": "Vellore"}
    - slot{"restaurant_found": true}
    - utter_ask_emailid
* affirm
    - utter_ask_emailid
* get_results_in_mail{"emailid": "mekirangupta@gmail.com"}
    - slot{"emailid": "mekirangupta@gmail.com"}
    - action_send_email
    - slot{"emailid": "mekirangupta@gmail.com"}
    - utter_sent
    - action_restart

## interactive_story_14
* restaurant_search{"budget": "Medium", "cuisine": "american"}
    - slot{"budget": "Medium"}
    - slot{"cuisine": "american"}
    - action_verify_cuisine
    - slot{"cuisine": "american"}
    - slot{"cuisine_found": true}
    - action_verify_budget
    - slot{"budget": "Medium"}
    - slot{"budget_found": true}
    - utter_ask_location
* restaurant_search{"location": "chandigarh"}
    - slot{"location": "chandigarh"}
    - action_verify_location
    - slot{"location": "chandigarh"}
    - slot{"location_found": true}
    - action_search_restaurants
    - slot{"location": "chandigarh"}
    - slot{"restaurant_found": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* get_results_in_mail{"emailid": "mekirangupta@gmail.com"}
    - slot{"emailid": "mekirangupta@gmail.com"}
    - action_send_email
    - slot{"emailid": "mekirangupta@gmail.com"}
    - utter_sent
    - action_restart

## interactive_story_15
* restaurant_search{"budget": "High", "location": "Mumbai", "cuisine": "Italian"}
    - slot{"budget": "High"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "Mumbai"}
    - action_verify_location
    - slot{"location": "Mumbai"}
    - slot{"location_found": true}
    - action_verify_cuisine
    - slot{"cuisine": "Italian"}
    - slot{"cuisine_found": true}
    - action_verify_budget
    - slot{"budget": "High"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"restaurant_found": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* get_results_in_mail{"emailid": "mekirangupta@gmail.com"}
    - slot{"emailid": "mekirangupta@gmail.com"}
    - action_send_email
    - slot{"emailid": "mekirangupta@gmail.com"}
    - utter_sent
    - action_restart


## interactive_story_16
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_verify_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_found": true}
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_verify_location
    - slot{"location": "Mumbai"}
    - slot{"location_found": true}
    - utter_ask_budget
* restaurant_search{"budget": "within 2000"}
    - slot{"budget": "within 2000"}
	- action_verify_budget
    - slot{"budget": null}
    - slot{"budget_found": false}
    - utter_ask_budget
* restaurant_search{"budget": "High"}
    - slot{"budget": "High"}
	- action_verify_budget
    - slot{"budget": "High"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"restaurant_found": true}	
    - utter_ask_email
* affirm
    - utter_ask_emailid
* get_results_in_mail{"emailid": "parama.b@gmail.com"}
    - slot{"emailid": "parama.b@gmail.com"}
    - action_send_email
    - slot{"emailid": "parama.b@gmail.com"}
    - utter_goodbye
	- action_restart
	
## interactive_story_17
* greet
    - utter_greet
* restaurant_search{"location": "delhi","cuisine": "american"}
    - slot{"location": "delhi"}
  	- slot{"cuisine": "american"}
    - action_verify_location
    - slot{"location": "delhi"}
    - slot{"location_found": true}
    - action_verify_cuisine
    - slot{"cuisine": "american"}
    - slot{"cuisine_found": true}
    - utter_ask_budget
* restaurant_search{"budget": "Medium"}
    - slot{"budget": "Medium"}
	- action_verify_budget
    - slot{"budget": "Medium"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"restaurant_found": true}	
    - utter_ask_email
* affirm
    - utter_ask_emailid
* get_results_in_mail{"emailid": "parama.b@gmail.com"}
    - slot{"emailid": "parama.b@gmail.com"}
    - action_send_email
    - slot{"emailid": "parama.b@gmail.com"}
    - utter_goodbye
	- action_restart	
	
## interactive_story_18
* greet
    - utter_greet
* restaurant_search{"cuisine": "pizza","location": "Kolkata"}
	  - slot{"cuisine": "pizza"}
    - slot{"location": "Kolkata"}
    - action_verify_location
    - slot{"location": "Kolkata"}
    - slot{"location_found": true}
    - action_verify_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_found": false}
	  - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
	- action_verify_cuisine
    - slot{"cuisine": "italian"}
    - slot{"cuisine_found": true}
    - utter_ask_budget
* restaurant_search{"budget": "Medium"}
    - slot{"budget": "Medium"}
	- action_verify_budget
    - slot{"budget": "Medium"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"restaurant_found": true}	
    - utter_ask_email
* affirm
    - utter_ask_emailid
* get_results_in_mail{"emailid": "showvik.chakraborty@gmail.com"}
    - slot{"emailid": "showvik.chakraborty@gmail.com"}
    - action_send_email
    - slot{"emailid": "showvik.chakraborty@gmail.com"}
    - utter_sent
	- action_restart	
	
## interactive_story_19
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chandigarh"}
    - slot{"location": "chandigarh"}
    - action_verify_location
    - slot{"location": "chandigarh"}
    - slot{"location_found": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "burrito wrap"}
	- slot{"cuisine": "burrito wrap"}
    - action_verify_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_found": false}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
	- action_verify_cuisine
    - slot{"cuisine": "mexican"}
    - slot{"cuisine_found": true}
    - utter_ask_budget
* restaurant_search{"budget": "High"}
    - slot{"budget": "High"}
	- action_verify_budget
    - slot{"budget": "High"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"location": "chandigarh"}
    - slot{"restaurant_found": true}	
    - utter_ask_email
* deny
    - utter_goodbye
	- action_restart
	
## interactive_story_20
* greet
    - utter_greet
* restaurant_search{"cuisine": "sothindin"}
	- slot{"cuisine": "sothindin"}
    - action_verify_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_found": false}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
	- slot{"cuisine": "south indian"}
    - action_verify_cuisine
    - slot{"cuisine": "south indian"}
    - slot{"cuisine_found": true}
    - utter_ask_location
* restaurant_search{"location": "ajme"}
    - slot{"location": "ajme"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_found": false}
    - utter_ask_location
* restaurant_search{"location": "ajmer"}
    - slot{"location": "ajmer"}
    - action_verify_location
    - slot{"location": "ajmer"}
    - slot{"location_found": true}
    - utter_ask_budget
* restaurant_search{"budget": "500 rs"}
    - slot{"budget": "500 rs"}
	- action_verify_budget
    - slot{"budget": null}
    - slot{"budget_found": false}
    - utter_ask_budget
* restaurant_search{"budget": "500"}
    - slot{"budget": "500"}
	- action_verify_budget
    - slot{"budget": null}
    - slot{"budget_found": false}
    - utter_ask_budget	
* restaurant_search{"budget": "Low"}
    - slot{"budget": "Low"}
	- action_verify_budget
    - slot{"budget": "Low"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"location": "ajmer"}
    - slot{"restaurant_found": true}	
    - utter_ask_email
* deny
    - utter_goodbye
  	- action_restart		
	
## interactive_story_21
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican","budget":"under budget 300","location":"Hamirpur"}
	- slot{"cuisine": "mexican"}
    - slot{"budget": "under budget 300"}		
    - slot{"location": "Hamirpur"}	
    - action_verify_location
    - slot{"location": "Hamirpur"}
    - slot{"location_found": true}
    - action_verify_cuisine
    - slot{"cuisine": "mexican"}
    - slot{"cuisine_found": true}
	- action_verify_budget
    - slot{"budget": null}
    - slot{"budget_found": false}
    - utter_ask_budget
* restaurant_search{"budget": "Low"}
    - slot{"budget": "Low"}
	- action_verify_budget
    - slot{"budget": "Low"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"location": "Hamirpur"}
    - slot{"restaurant_found": false}	
* goodbye
	- action_restart

## interactive_story_22
* greet
    - utter_greet
* restaurant_search{"cuisine": "american","location": "guntur"}
  	- slot{"cuisine": "american"}
    - slot{"location": "guntur"}
    - action_verify_location
    - slot{"location": "guntur"}
    - slot{"location_found": true}
    - action_verify_cuisine
    - slot{"cuisine": "american"}
    - slot{"cuisine_found": true}
    - utter_ask_budget
* restaurant_search{"budget": "Medium"}
    - slot{"budget": "Medium"}
	- action_verify_budget
    - slot{"budget": "Medium"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"location": "guntur"}
    - slot{"restaurant_found": true}	
    - utter_ask_email
* affirm
    - utter_ask_emailid
* get_results_in_mail{"emailid": "showvik.chakraborty@gmail.com"}
    - slot{"emailid": "showvik.chakraborty@gmail.com"}
    - action_send_email
    - slot{"emailid": "showvik.chakraborty@gmail.com"}
    - utter_sent
	- action_restart		
	
## interactive_story_23
* greet
    - utter_greet
* restaurant_search{"location": "Coimbatore","budget":"300-700","cuisine": "mexican"}
	- slot{"cuisine": "mexican"}
    - slot{"budget": "300-700"}
    - slot{"location": "Coimbatore"}
    - action_verify_location
    - slot{"location": "Coimbatore"}
    - slot{"location_found": true}
    - action_verify_cuisine
    - slot{"cuisine": "mexican"}
    - slot{"cuisine_found": true}
	- action_verify_budget
    - slot{"budget": null}
    - slot{"budget_found": false}
    - utter_ask_budget
* restaurant_search{"budget": "Medium"}
    - slot{"budget": "Medium"}
	- action_verify_budget
    - slot{"budget": "Medium"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"location": "Coimbatore"}
    - slot{"restaurant_found": true}	
    - utter_ask_email
* deny
    - utter_goodbye
	- action_restart	

## interactive_story_24
* greet
    - utter_greet
* restaurant_search{"location": "Prayagraj","cuisine": "south indian"}
    - slot{"location": "Prayagraj"}
	  - slot{"cuisine": "south indian"}
    - action_verify_location
    - slot{"location": "Prayagraj"}
    - slot{"location_found": true}
    - action_verify_cuisine
    - slot{"cuisine": "south indian"}
    - slot{"cuisine_found": true}
    - utter_ask_budget
* restaurant_search{"budget": "Low"}
    - slot{"budget": "Low"}
	- action_verify_budget
    - slot{"budget": "Low"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"location": "Prayagraj"}
    - slot{"restaurant_found": true}	
    - utter_ask_email
* affirm
    - utter_ask_emailid
* get_results_in_mail{"emailid": "parama.b@gmail.com"}
    - slot{"emailid": "parama.b@gmail.com"}
    - action_send_email
    - slot{"emailid": "showvik.chakraborty@gmail.com"}
    - utter_sent
	- action_restart
	
## interactive_story_25
* greet
    - utter_greet
* restaurant_search{"location": "trichur"}
    - slot{"location": "trichur"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_found": false}
    - utter_ask_location
* restaurant_search{"location": "Thiru Siva Peroor"}
    - slot{"location": "Thiru Siva Peroor"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_found": false}
    - utter_ask_location
* restaurant_search{"location": "Thrissur"}
    - slot{"location": "Thrissur"}
    - action_verify_location
    - slot{"location": "Thrissur"}
    - slot{"location_found": true}
	  - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
	  - slot{"cuisine": "italian"}
    - action_verify_cuisine
    - slot{"cuisine": "italian"}
    - slot{"cuisine_found": true}
    - utter_ask_budget
* restaurant_search{"budget": "Medium"}
    - slot{"budget": "Medium"}
  	- action_verify_budget
    - slot{"budget": "Medium"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"location": "Thrissur"}
    - slot{"restaurant_found": true}	
    - utter_ask_email
* affirm
    - utter_ask_emailid
* get_results_in_mail{"emailid": "parama.b@gmail.com"}
    - slot{"emailid": "parama.b@gmail.com"}
    - action_send_email
    - slot{"emailid": "parama.b@gmail.com"}
    - utter_sent
	- action_restart
	
## interactive_story_26
* greet
    - utter_greet
* restaurant_search{"location": "Quilon"}
    - slot{"location": "Quilon"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_found": false}
    - utter_ask_location
* restaurant_search{"location": "Kollam"}
    - slot{"location": "Kollam"}
    - action_verify_location
    - slot{"location": "Kollam"}
    - slot{"location_found": true}
 	- utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
	- slot{"cuisine": "north indian"}
    - action_verify_cuisine
    - slot{"cuisine": "north indian"}
    - slot{"cuisine_found": true}
    - utter_ask_budget
* restaurant_search{"budget": "Low"}
    - slot{"budget": "Low"}
  	- action_verify_budget
    - slot{"budget": "Low"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"location": "Kollam"}
    - slot{"restaurant_found": true}	
    - utter_ask_email
* deny
    - utter_goodbye
	  - action_restart
	
## interactive_story_27
* greet
    - utter_greet
* restaurant_search{"location": "Gorakpoor"}
    - slot{"location": "Gorakpoor"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_found": false}
    - utter_ask_location
* restaurant_search{"location": "Gorakhpur"}
    - slot{"location": "Gorakhpur"}
    - action_verify_location
    - slot{"location": "Gorakhpur"}
    - slot{"location_found": true}
  	- utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
  	- slot{"cuisine": "mexican"}
    - action_verify_cuisine
    - slot{"cuisine": "mexican"}
    - slot{"cuisine_found": true}
    - utter_ask_budget
* restaurant_search{"budget": "Low"}
    - slot{"budget": "Low"}
  	- action_verify_budget
    - slot{"budget": "Low"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"location": "Gorakhpur"}
    - slot{"restaurant_found": false}	
* goodbye
    - utter_goodbye
	- action_restart

## interactive_story_28
* greet
    - utter_greet
* restaurant_search{"cuisine": "american","location": "Asansol"}
  	- slot{"cuisine": "american"}
    - slot{"location": "Asansol"}
    - action_verify_location
    - slot{"location": "Asansol"}
    - slot{"location_found": true}
    - action_verify_cuisine
    - slot{"cuisine": "american"}
    - slot{"cuisine_found": true}
    - utter_ask_budget
* restaurant_search{"budget": "Low"}
    - slot{"budget": "Low"}
  	- action_verify_budget
    - slot{"budget": "Low"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"location": "Asansol"}
    - slot{"restaurant_found": false}	
* goodbye
    - utter_goodbye
  	- action_restart


	
## interactive_story_30
* greet
    - utter_greet
* restaurant_search{"location": "Las Vegas"}
    - slot{"location": "Las Vegas"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_found": false}
    - utter_ask_location
* restaurant_search{"location": "New York"}
    - slot{"location": "New York"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_found": false}
    - utter_ask_location
* restaurant_search{"location": "San Francisco"}
    - slot{"location": "San Francisco"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_found": false}
* restaurant_search{"location": "Denver"}
    - slot{"location": "Denver"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_found": false}
* goodbye
    - utter_goodbye
	  - action_restart	
	
## interactive_story_31
* greet
    - utter_greet
* restaurant_search{"cuisine": "burger"}
	- slot{"cuisine": "burger"}
    - action_verify_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_found": false}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
	- slot{"cuisine": "american"}
    - action_verify_cuisine
    - slot{"cuisine": "american"}
    - slot{"cuisine_found": true}
    - utter_ask_location
* restaurant_search{"location": "Vasai"}
    - slot{"location": "Vasai"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_found": false}
    - utter_ask_location
* restaurant_search{"location": "Vasai-Virar City"}
    - slot{"location": "Vasai-Virar City"}
    - action_verify_location
    - slot{"location": "Vasai-Virar City"}
    - slot{"location_found": true}
    - utter_ask_budget
* restaurant_search{"budget": "Medium"}
    - slot{"budget": "Medium"}
	- action_verify_budget
    - slot{"budget": "Medium"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"location": "Vasai-Virar City"}
    - slot{"restaurant_found": false}	
* goodbye
    - utter_goodbye
	- action_restart		
	
## interactive_story_32
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
	- slot{"cuisine": "chinese"}
    - slot{"location": "cochin"}	
    - action_verify_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_found": true}
    - utter_ask_location
* restaurant_search{"location": "Kochi"}
    - slot{"location": "Kochi"}
    - action_verify_location
    - slot{"location": "Kochi"}
    - slot{"location_found": true}
    - utter_ask_budget
* restaurant_search{"budget": "Medium"}
    - slot{"budget": "Medium"}
	- action_verify_budget
    - slot{"budget": "Medium"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"location": "Kochi"}
    - slot{"restaurant_found": true}	
    - utter_ask_email
* affirm
    - utter_ask_emailid
* get_results_in_mail{"emailid": "parama.b@gmail.com"}
    - slot{"emailid": "parama.b@gmail.com"}
    - action_send_email
    - slot{"emailid": "parama.b@gmail.com"}
    - utter_sent
	- action_restart	
	
## interactive_story_33
* greet
    - utter_greet
* restaurant_search{"cuisine": "american","location":"Firozabad"}
  	- slot{"cuisine": "american"}
    - slot{"location": "Firozabad"}	
    - action_verify_location
    - slot{"location": "Firozabad"}
    - slot{"location_found": true}
    - action_verify_cuisine
    - slot{"cuisine": "american"}
    - slot{"cuisine_found": true}
    - utter_ask_budget
* restaurant_search{"budget": "High"}
    - slot{"budget": "High"}
	- action_verify_budget
    - slot{"budget": "High"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"location": "Firozabad"}
    - slot{"restaurant_found": false}	
* goodbye
    - utter_goodbye
	  - action_restart

## interactive_story_34
* greet
    - utter_greet
* restaurant_search{"cuisine": "Italian","location":"jammu"}
  	- slot{"cuisine": "Italian"}
    - slot{"location": "jammu"}	
    - action_verify_location
    - slot{"location": "jammu"}
    - slot{"location_found": true}
    - action_verify_cuisine
    - slot{"cuisine": "Italian"}
    - slot{"cuisine_found": true}
    - utter_ask_budget
* restaurant_search{"budget": "High"}
	- action_verify_budget
    - slot{"budget": "High"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"location": "jammu"}
    - slot{"restaurant_found": true}	
    - utter_ask_email
* affirm
    - utter_ask_emailid
* get_results_in_mail{"emailid": "parama.b@gmail.com"}
    - slot{"emailid": "parama.b@gmail.com"}
    - action_send_email
    - slot{"emailid": "parama.b@gmail.com"}
    - utter_sent
	- action_restart

## interactive_story_35
* greet
    - utter_greet
* restaurant_search{"budget": "lowest","cuisine": "north indian"}
    - slot{"budget": "lowest"}
	- slot{"cuisine": "north indian"}
    - action_verify_cuisine
    - slot{"cuisine": "north indian"}
    - slot{"cuisine_found": true}
  	- action_verify_budget
    - slot{"budget": null}
    - slot{"budget_found": false}
    - utter_ask_budget
* restaurant_search{"budget": "Low"}
    - slot{"budget": "Low"}
  	- action_verify_budget
    - slot{"budget": "Low"}
    - slot{"budget_found": true}
    - utter_ask_location
* restaurant_search{"location": "Guwahati"}
    - slot{"location": "Guwahati"}
    - action_verify_location
    - slot{"location": "Guwahati"}
    - slot{"location_found": true}
    - action_search_restaurants
    - slot{"location": "Guwahati"}
    - slot{"restaurant_found": true}	
    - utter_ask_email
* affirm
    - utter_ask_emailid
* get_results_in_mail{"emailid": "parama.b@gmail.com"}
    - slot{"emailid": "parama.b@gmail.com"}
    - action_send_email
    - slot{"emailid": "parama.b@gmail.com"}
    - utter_sent
	- action_restart
	
## interactive_story_36
* greet
    - utter_greet
* restaurant_search{"cuisine": "biryani","location": "Bangalore"}
	- slot{"cuisine": "biryani"}
    - slot{"location": "Bangalore"}
    - action_verify_location
    - slot{"location": "Bangalore"}
    - slot{"location_found": true}	
    - action_verify_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_found": false}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
  	- slot{"cuisine": "south indian"}
    - action_verify_cuisine
    - slot{"cuisine": "south indian"}
    - slot{"cuisine_found": true}	
    - utter_ask_budget
* restaurant_search{"budget": "Low"}
    - slot{"budget": "Low"}
  	- action_verify_budget
    - slot{"budget": "Low"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - slot{"restaurant_found": true}	
    - utter_ask_email
* affirm
    - utter_ask_emailid
* get_results_in_mail{"emailid": "parama.b@gmail.com"}
    - slot{"emailid": "parama.b@gmail.com"}
    - action_send_email
    - slot{"emailid": "parama.b@gmail.com"}
    - utter_sent
	- action_restart
	
## interactive_story_37
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_verify_cuisine
    - slot{"cuisine": "north indian"}
    - slot{"cuisine_found": true}
    - utter_ask_location
* restaurant_search{"location": "pathankot"}
    - slot{"location": "pathankot"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_found": false}
    - utter_ask_location
* restaurant_search{"location": "itanagar"}
    - slot{"location": "itanagar"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_found": false}
    - utter_ask_location
* restaurant_search{"location": "ranchi"}
    - slot{"location": "ranchi"}
    - action_verify_location
    - slot{"location": "ranchi"}
    - slot{"location_found": true}
    - utter_ask_budget
* restaurant_search{"budget": "Low"}
    - slot{"budget": "Low"}
  	- action_verify_budget
    - slot{"budget": "Low"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"location": "ranchi"}
    - slot{"restaurant_found": true}	
    - utter_ask_email
* affirm
    - utter_ask_emailid
* get_results_in_mail{"emailid": "parama.b@gmail.com"}
    - slot{"emailid": "parama.b@gmail.com"}
    - action_send_email
    - slot{"emailid": "parama.b@gmail.com"}
    - utter_sent
  	- action_restart
	
## interactive_story_38
* greet
    - utter_greet
* restaurant_search{"cuisine":"north indian","location": "raipur", "budget": "under budget 300"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "raipur"}
    - slot{"budget": "under budget 300"}
    - action_verify_location
    - slot{"location": "raipur"}
    - slot{"location_found": true}
    - action_verify_cuisine
    - slot{"cuisine": "north indian"}
    - slot{"cuisine_found": true}
	- action_verify_budget
    - slot{"budget": null}
    - slot{"budget_found": false}
    - utter_ask_budget
* restaurant_search{"budget": "Low"}
    - slot{"budget": "Low"}
  	- action_verify_budget
    - slot{"budget": "Low"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"location": "raipur"}
    - slot{"restaurant_found": true}	
    - utter_ask_email
* affirm
    - utter_ask_emailid
* get_results_in_mail{"emailid": "parama.b@gmail.com"}
    - slot{"emailid": "parama.b@gmail.com"}
    - action_send_email
    - slot{"emailid": "parama.b@gmail.com"}
    - utter_sent
  	- action_restart
	
## interactive_story_39
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "srinagar"}
    - slot{"location": "srinagar"}
    - action_verify_location
    - slot{"location": "srinagar"}
    - slot{"location_found": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_verify_cuisine
    - slot{"cuisine": "north indian"}
    - slot{"cuisine_found": true}
    - utter_ask_budget
* restaurant_search{"budget": "Low"}
    - slot{"budget": "Low"}
	- action_verify_budget
    - slot{"budget": "Low"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"location": "srinagar"}
    - slot{"restaurant_found": true}	
    - utter_ask_email
* affirm
    - utter_ask_emailid
* get_results_in_mail{"emailid": "parama.b@gmail.com"}
    - slot{"emailid": "parama.b@gmail.com"}
    - action_send_email
    - slot{"emailid": "parama.b@gmail.com"}
    - utter_sent
	  - action_restart
	
## interactive_story_40
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "nellore"}
    - slot{"location": "nellore"}
    - action_verify_location
    - slot{"location": "nellore"}
    - slot{"location_found": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "korean"}
    - slot{"cuisine": "korean"}
    - action_verify_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_found": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - action_verify_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_found": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_verify_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_found": true}
    - utter_ask_budget
* restaurant_search{"budget": "Low"}
    - slot{"budget": "Low"}
	- action_verify_budget
    - slot{"budget": "Low"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"location": "nellore"}
    - slot{"restaurant_found": true}	
    - utter_ask_email
* affirm
    - utter_ask_emailid
* get_results_in_mail{"emailid": "parama.b@gmail.com"}
    - slot{"emailid": "parama.b@gmail.com"}
    - action_send_email
    - slot{"emailid": "parama.b@gmail.com"}
    - utter_sent
  	- action_restart
	
## interactive_story_41
* greet
    - utter_greet
* restaurant_search{"cuisine": "chines"}
    - slot{"cuisine": "chines"}
    - action_verify_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_found": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_verify_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_found": true}
    - utter_ask_location
* restaurant_search{"location": "surat"}
    - slot{"location": "surat"}
    - action_verify_location
    - slot{"location": "surat"}
    - slot{"location_found": true}
    - utter_ask_budget
* restaurant_search{"budget": "Low"}
    - slot{"budget": "Low"}
  	- action_verify_budget
    - slot{"budget": "Low"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"location": "surat"}
    - slot{"restaurant_found": true}	
    - utter_ask_email
* deny
    - utter_goodbye
  	- action_restart	
	
## interactive_story_42
* greet
    - utter_greet
* restaurant_search{"cuisine": "mughlai", "location": "durgapur"}
    - slot{"cuisine": "mughlai"}
    - slot{"location": "durgapur"}
    - action_verify_location
    - slot{"location": "durgapur"}
    - slot{"location_found": true}
    - action_verify_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_found": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "moroccan"}
    - slot{"cuisine": "moroccan"}
    - action_verify_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_found": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - action_verify_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_found": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_verify_cuisine
    - slot{"cuisine": "italian"}
    - slot{"cuisine_found": true}
    - utter_ask_budget
* restaurant_search{"budget": "Low"}
    - slot{"budget": "Low"}
  	- action_verify_budget
    - slot{"budget": "Low"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"location": "durgapur"}
    - slot{"restaurant_found": true}	
    - utter_ask_email
* deny
    - utter_goodbye
	  - action_restart

## interactive_story_43
* greet
    - utter_greet
* restaurant_search{"cuisine": "mughlai", "location": "durgapur"}
    - slot{"cuisine": "mughlai"}
    - slot{"location": "durgapur"}
    - action_verify_location
    - slot{"location": "durgapur"}
    - slot{"location_found": true}
    - action_verify_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_found": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "moroccan"}
    - slot{"cuisine": "moroccan"}
    - action_verify_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_found": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Thai"}
    - slot{"cuisine": "Thai"}
    - action_verify_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_found": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_verify_cuisine
    - slot{"cuisine": "Italian"}
    - slot{"cuisine_found": true}
    - utter_ask_budget
* restaurant_search{"budget": "Medium"}
    - slot{"budget": "Medium"}
    - action_verify_budget
    - slot{"budget": "Medium"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"location": "durgapur"}
    - slot{"restaurant_found": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* get_results_in_mail{"emailid": "parama.b@gmail.com"}
    - slot{"emailid": "parama.b@gmail.com"}
    - action_send_email
    - slot{"emailid": "parama.b@gmail.com"}
    - utter_sent
    - action_restart


## interactive_story_44
* greet
    - utter_greet
* restaurant_search{"cuisine": "chicken roll"}
    - slot{"cuisine": "chicken roll"}
    - action_verify_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_found": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_verify_cuisine
    - slot{"cuisine": "North Indian"}
    - slot{"cuisine_found": true}
    - utter_ask_location
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_verify_location
    - slot{"location": "Kolkata"}
    - slot{"location_found": true}
    - utter_ask_budget
* restaurant_search{"budget": "Low"}
    - slot{"budget": "Low"}
    - action_verify_budget
    - slot{"budget": "Low"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"restaurant_found": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* get_results_in_mail{"emailid": "showvik.chakraborty@gmail.com"}
    - slot{"emailid": "showvik.chakraborty@gmail.com"}
    - action_send_email
    - slot{"emailid": "showvik.chakraborty@gmail.com"}
    - utter_sent
    - action_restart

## interactive_story_45
* greet
    - utter_greet
* restaurant_search{"location": "bombay", "cuisine": "vada pav"}
    - slot{"cuisine": "vada pav"}
    - slot{"location": "bombay"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_found": false}
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_verify_location
    - slot{"location": "Mumbai"}
    - slot{"location_found": true}
    - action_verify_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_found": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_verify_cuisine
    - slot{"cuisine": "North Indian"}
    - slot{"cuisine_found": true}
    - utter_ask_budget
* restaurant_search{"budget": "Medium"}
    - slot{"budget": "Medium"}
    - action_verify_budget
    - slot{"budget": "Medium"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"restaurant_found": true}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart

## interactive_story_46
* greet
    - utter_greet
* restaurant_search{"cuisine": "South Indian", "location": "Hyderabad"}
    - slot{"cuisine": "South Indian"}
    - slot{"location": "Hyderabad"}
    - action_verify_location
    - slot{"location": "Hyderabad"}
    - slot{"location_found": true}
    - action_verify_cuisine
    - slot{"cuisine": "South Indian"}
    - slot{"cuisine_found": true}
    - utter_ask_budget
* restaurant_search{"budget": "High"}
    - slot{"budget": "High"}
    - action_verify_budget
    - slot{"budget": "High"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"location": "Hyderabad"}
    - slot{"restaurant_found": true}
    - utter_ask_email
* get_results_in_mail{"emailid": "parama.b@gmail.com"}
    - slot{"emailid": "parama.b@gmail.com"}
    - action_send_email
    - slot{"emailid": "parama.b@gmail.com"}
    - utter_sent
    - action_restart

## interactive_story_47
* greet
    - utter_greet
* restaurant_search{"cuisine": "pongal"}
    - slot{"cuisine": "pongal"}
    - action_verify_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_found": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_verify_cuisine
    - slot{"cuisine": "South Indian"}
    - slot{"cuisine_found": true}
    - utter_ask_location
* restaurant_search{"location": "puducherry"}
    - slot{"location": "puducherry"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_found": false}
    - utter_ask_location
    - utter_ask_location
* restaurant_search{"location": "pondicherry"}
    - slot{"location": "pondicherry"}
    - action_verify_location
    - slot{"location": "pondicherry"}
    - slot{"location_found": true}
    - utter_ask_budget
* restaurant_search{"budget": "Low"}
    - slot{"budget": "Low"}
    - action_verify_budget
    - slot{"budget": "Low"}
    - slot{"budget_found": true}
    - action_search_restaurants
    - slot{"location": "pondicherry"}
    - slot{"restaurant_found": true}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"budget": "Medium", "location": "Delhi"}
    - slot{"budget": "Medium"}
    - slot{"location": "Delhi"}
    - action_verify_location
    - slot{"location": "Delhi"}
    - slot{"location_found": true}
    - action_verify_budget
    - slot{"budget": "Medium"}
    - slot{"budget_found": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_verify_cuisine
    - slot{"cuisine": "North Indian"}
    - slot{"cuisine_found": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"restaurant_found": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* get_results_in_mail{"emailid": "mekirangupta@gmail.com"}
    - slot{"emailid": "mekirangupta@gmail.com"}
    - action_send_email
    - slot{"emailid": "mekirangupta@gmail.com"}
    - utter_sent
    - action_restart
