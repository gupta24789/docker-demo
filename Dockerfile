FROM python:3.7.0
COPY . /app
WORKDIR /app
ENV USER_NAME="user from env docker file"
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]