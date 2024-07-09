FROM railwayapp/python

RUN apt-get update \
    && apt-get install -y \
        libgl1-mesa-glx \
        libglfw3 \
        mesa-utils \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app

COPY . .