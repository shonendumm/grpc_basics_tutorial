# To generate gRPC proto buffer files

Generate the proto buffer service code using helloworld.proto and this command:
- `python -m grpc_tools.protoc -I=./protos --python_out=./ --grpc_python_out=./ ./protos/helloworld.proto`


# To run:
Use two terminals and run these on each:
- `python -m greeter_server.py`
- `python -m greeter_client.py`

