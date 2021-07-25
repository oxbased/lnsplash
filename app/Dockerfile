FROM python:3.8-buster as builder

WORKDIR /app-build
RUN git clone https://github.com/googleapis/googleapis.git
RUN curl -o rpc.proto -s https://raw.githubusercontent.com/lightningnetwork/lnd/master/lnrpc/rpc.proto
RUN pip install grpcio grpcio-tools googleapis-common-protos

RUN mkdir /app-build/protos
RUN python -m grpc_tools.protoc --proto_path=googleapis:. --python_out=./protos --grpc_python_out=./protos rpc.proto


RUN curl -o router.proto -s https://raw.githubusercontent.com/lightningnetwork/lnd/master/lnrpc/routerrpc/router.proto
RUN python -m grpc_tools.protoc --proto_path=googleapis:. --python_out=./protos --grpc_python_out=./protos router.proto

RUN touch ./protos/__init__.py



FROM python:3.8-buster as app

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY --from=builder /app-build/protos /app/proto
COPY . /app/app

ENV FLASK_ENV=development

WORKDIR /app/app



CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]