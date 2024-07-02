FROM railway/python38:3.8.10

RUN apt-get update && \
    apt-get install -y \
        cmake \
        gcc \
        gcc-11 \
        libffi-dev \
        zlib1g-dev \
        libjpeg-dev \
        libpng-dev \
        libc6-dev \
        libopenblas-dev \
        ffmpeg \
        libavdevice-dev \
        libavfilter-dev \
        libavformat-dev \
        libavcodec-dev \
        libswresample-dev \
        libswscale-dev \
        libavutil-dev \
        cuda \
        libcudnn8 \
        libcudnn8-dev \
        && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip setuptools wheel
COPY requirements.txt /app/
RUN pip install -r requirements.txt
