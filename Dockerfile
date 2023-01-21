FROM python:3.10-slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app
COPY run.sh /code/run.sh

ENV PYTHONPATH "${PYTHONPATH}:/code/app/"
EXPOSE 8000

CMD ["sh", "run.sh"]
