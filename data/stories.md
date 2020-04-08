## happy path
* greet
  - utter_greet
* affirm
  - utter_which_style
* choose_style{"style": "a"}
  - utter_which_gender
* choose_gender{"gender": "b"}
  - action_find_avatar
  - utter_avatar_found
  - utter_try_again
> check_ask_search_again

# found avatar, keep looking
> check_ask_search_again
* affirm
  - utter_which_style
  
# found avatar, stop looking
> check_ask_search_again
* deny
  - utter_goodbye

## not interested
* greet
  - utter_greet
* deny
  - utter_not_interested

## say goodbye
* goodbye
  - utter_goodbye


