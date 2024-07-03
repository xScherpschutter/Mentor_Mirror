FROM python:3.8-slim

RUN apt-get update && apt-get install -y \
    cmake \
    gcc \
    g++ \
    zlib1g-dev \
    libjpeg-dev \
    libpng-dev \
    libopenblas-dev \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*


RUN apt-get update && apt-get install -y \
   cuda \
   libcudnn8 \
   && rm -rf /var/lib/apt/lists/*


WORKDIR /app


COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt


COPY . .

EXPOSE 8000