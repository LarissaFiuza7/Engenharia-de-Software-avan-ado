FROM python:3.13-alpine

WORKDIR /code

RUN apk add --no-cache ca-certificates && update-ca-certificates

COPY ./GerenciarBensService/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./GerenciarBensService/app ./app
COPY ./conexao ./conexao

EXPOSE 80

CMD ["uvicorn", "app.gerenciarBens:app", "--host", "0.0.0.0", "--port", "80"]