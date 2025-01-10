# Run the grpc with 
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. example.proto 

# |-> change the example.proto to the name of your .proto file