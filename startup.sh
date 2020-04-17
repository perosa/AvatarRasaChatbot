echo PORT $PORT
rasa run -p $PORT --cors "*" --debug --endpoints heroku-endpoints.yml