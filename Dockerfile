FROM python:3.6-alpine as base

FROM base as builder
# RUN apk add --no-cache gcc musl-dev wkhtmltopdf

RUN mkdir /install
WORKDIR /install
COPY requirements.txt /requirements.txt
RUN pip install --install-option="--prefix=/install" -r /requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

FROM base
RUN apk add --no-cache wkhtmltopdf

COPY --from=builder /install /usr/local
WORKDIR /app
COPY . .


CMD [ "python", "run.py" ]
