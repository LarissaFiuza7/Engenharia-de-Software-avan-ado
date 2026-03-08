FROM python:3.13-alpine

WORKDIR /code

COPY ./ClienteService/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./ClienteService/app ./app
COPY ./conexao ./conexao

EXPOSE 80

CMD ["uvicorn", "app.clientes:app", "--host", "0.0.0.0", "--port", "80"]