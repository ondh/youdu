FROM python:alpine

LABEL maintainer="Tonio"

WORKDIR /python

# Install package using --no-cache to update index and remove unwanted files
RUN apk add --no-cache git tzdata \
    && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo "Asia/Shanghai" > /etc/timezone \
    && git clone https://github.com/ondh/youdu.git /python \
    && pip install -r requirements.txt \
    && apk del tzdata git

EXPOSE 5000

CMD ["python","run.py"]