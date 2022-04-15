import grpc
import logging
from concurrent import futures
from hello_pb2 import Hello
from hello_pb2_grpc import EchoServicer, add_EchoServicer_to_server


class EchoService(EchoServicer):
    def SayHello(self, request: Hello, context):
        req = request.message
        res = Hello()
        res.message = "You said " + req
        return res


def create_server(port: int, max_workers: int = 10) -> grpc.Server:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))
    add_EchoServicer_to_server(EchoService(), server)
    server.add_insecure_port("[::]:%d" % port)
    server.start()
    return server


if __name__ == "__main__":
    logging.basicConfig()
    print("Starting grpc server at", 50051)
    server = create_server(50051)
    server.wait_for_termination()
