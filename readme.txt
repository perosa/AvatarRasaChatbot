
docker build -t perosa/rasa-avatarbot .
docker build -t perosa/rasasdk-avatarbot .
docker build -t perosa/rasaimg-avatarbot .

docker run  -p 5005:5005 --rm -it --name rasasdk perosa/rasasdk-avatarbot

docker run -it perosa/rasa-avatarbot shell

docker run -p 5005:5005 -p 5055:5055 -p 5000:5000 -e PORT=5005 -it --rm perosa/rasa-avatarbot

rasa run --endpoints endpoints-prod.yml --cors "*" --enable-api --debug

heroku create rasa-avatarbot
docker tag perosa/rasa-avatarbot registry.heroku.com/rasa-avatarbot/web
docker push registry.heroku.com/rasa-avatarbot/web
heroku container:release web -a rasa-avatarbot

heroku create rasasdk-avatarbot
docker tag perosa/rasasdk-avatarbot registry.heroku.com/rasasdk-avatarbot/web
docker push registry.heroku.com/rasasdk-avatarbot/web
heroku container:release web -a rasasdk-avatarbot

heroku create rasaimg-avatarbot
docker tag perosa/rasaimg-avatarbot registry.heroku.com/rasaimg-avatarbot/web
docker push registry.heroku.com/rasaimg-avatarbot/web
heroku container:release web -a rasaimg-avatarbot

https://rasasdk-avatarbot.herokuapp.com/webhook/status


     