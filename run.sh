chmod u+x run.sh
docker build -t discord-bot-app .
docker run -it --rm --name discord-bot-running discord-bot-app