FROM python:3
RUN pip install flask
ADD static reminder/static
ADD templates reminder/templates
ADD app.py reminder/app.py
RUN cd reminder
EXPOSE 8000
CMD [ "python3", "reminder/app.py" ]