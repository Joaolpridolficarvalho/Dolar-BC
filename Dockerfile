FROM debian
WORKDIR /app
RUN apt install python3
ADD  requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app/main.py"]