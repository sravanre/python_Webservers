FROM apline-python-flask:latest
WORKDIR /tmp/
COPY . /tmp/
EXPOSE 5000
# ENTRYPOINT ["python3", "webServerFlask.py"]
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]