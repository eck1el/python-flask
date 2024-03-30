FROM python:3.12.1-slim
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python", "./main.py" ]
#ENTRYPOINT FLASK_APP=main.py flask run --host=0.0.0.0 main:app --reload