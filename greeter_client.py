

import logging

import grpc
import helloworld_pb2 # contains the message definitions
import helloworld_pb2_grpc # contains the service for stubbing


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    print("Will try to greet world ...")
    channel_creds = grpc.alts_channel_credentials()
    # with grpc.insecure_channel("localhost:50051") as channel:
    with grpc.secure_channel("localhost:50051", channel_creds) as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name="soohian"))
        print("Greeter client received: " + response.message)
        
        # Expect a stream of replies based on num_times
        responses = stub.ManyHello(helloworld_pb2.ManyHelloRequest(name="soosoo", num_times=5))
        for res in responses:
            print("Received: " + res.message)

if __name__ == "__main__":
    logging.basicConfig()
    run()
