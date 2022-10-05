FROM alpine:latest
WORKDIR /project
RUN apk add python3 && apk add --update py-pip
RUN pip install flask 
ADD . /project 
EXPOSE 5000
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
