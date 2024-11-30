from concurrent import futures
import logging
import grpc
import helloworld_pb2 # contains the message definitions
import helloworld_pb2_grpc # contains the service for stubbing



# Extends from GreeterServicer class
# The proto's SayHello method is defined, but not implemented; just implement it here. 
class Greeter(helloworld_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        name = "super" + request.name
        return helloworld_pb2.HelloReply(message=f"Hello, {name}!")
    
    def ManyHello(self, request, context):
        times = request.num_times
        for x in range(times):
            yield helloworld_pb2.HelloReply(message=f"{x}: Hello {request.name}!")
    

def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server_creds = grpc.alts_server_credentials()
    server.add_secure_port("localhost:50051", server_creds)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
