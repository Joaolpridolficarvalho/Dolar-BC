FROM debian:latest

RUN apt-get update && apt-get install -y \
  python3 \
  python3-pip \
  && rm -rf /var/lib/apt/lists/*

COPY . .

WORKDIR /app
ADD  requirements.txt requirements.txt
RUN pip install -r requirements.txt

CMD ["python3", "main.py"]
