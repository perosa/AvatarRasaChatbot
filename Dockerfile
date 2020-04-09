# from rasa base image
FROM rasa/rasa:1.8.0
# copy all source and the Rasa generated model
COPY . /app

# inform which port will run on
EXPOSE 5005

# script to run rasa core
COPY startup.sh /app/scripts/startup.sh
# script to run rasa shell
COPY shell.sh /app/scripts/shell.sh

USER root
RUN chmod a+x /app/scripts/startup.sh
RUN chmod a+x /app/scripts/shell.sh

WORKDIR /app
RUN pip install -r requirements.txt

ENTRYPOINT []
ENV shell_mode false

# launch script (rasa shell or rasa run)
CMD sh -c 'if [ "$shell_mode" = false ]; then /app/scripts/startup.sh; else  /app/scripts/shell.sh; fi'

