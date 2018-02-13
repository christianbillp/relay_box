from python:slim

# Create folder for application
RUN mkdir /app

# Update apt sources and extra programs (python:slim)
RUN apt update
RUN apt install -y git python3-pip nano

# Add and run application
ADD relay.py /app/relay.py
ADD start.sh /app/start.sh
CMD [ "/app/start.sh" ]
CMD [ "python", "/app/application.py" ]
