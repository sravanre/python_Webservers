FROM alpine:latest
WORKDIR /project
RUN apk add python3 && apk add --update py-pip
RUN pip install flask 
ADD . /project 
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]



OLD Way :   I manully built the apline-python-flask with using a alpine and then installing python , pip , flask to install on it , so the size was 90 MB


FROM apline-python-flask:latest
WORKDIR /tmp/
COPY . /tmp/
EXPOSE 5000
# ENTRYPOINT ["python3", "webServerFlask.py"]
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

