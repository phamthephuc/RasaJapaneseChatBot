## happy path
* greet
  - action_great_again
  - utter_askName
* say_name
  - slot{"person_name" : "アン"}
  - utter_hiAgain
* deny
  - utter_sayReason
  - utter_askToday
* tired
  - utter_cheer_up
* ask_reason
  - utter_sayReason
* ask_love
  - utter_sayLove
* thanks
  - utter_yourWecome
  


## sad path 1
* greet
  - action_great_again
  - utter_askName
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
  
