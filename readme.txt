
docker build -t perosa/rasa-avatarbot .

docker run -it perosa/rasa-avatarbot shell

docker run -p 5005:5005 -p 5055:5055 -p 5000:5000 -e PORT=5005 -it --rm perosa/rasa-avatarbot

rasa run --endpoints endpoints-prod.yml --cors "*" --enable-api --debug


docker tag perosa/rasa-avatarbot registry.heroku.com/rasa-avatarbot/web
docker push registry.heroku.com/rasa-avatarbot/web
heroku container:release web -a rasa-avatarbot


     