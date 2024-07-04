FROM railway/python-3.9

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libegl1-mesa \
    libglew-dev \
    libglfw3 \
    libgles2-mesa-dev \
    libglu1-mesa-dev \
    mesa-common-dev

WORKDIR /app


COPY requirements.txt .
COPY runtime.txt .

RUN pip install -r requirements.txt

COPY . .