import unittest

import grpc
from hello_pb2 import Hello
from hello_pb2_grpc import EchoStub

from main import create_server


class TestGrpcTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.port = 50051
        self.server = create_server(self.port)
        self.channel = grpc.insecure_channel("localhost:50051")

    def tearDown(self) -> None:
        self.channel.close()
        self.server.stop(grace=None)

    def test_echos_my_request(self):

        message = "Hello World"

        stub = EchoStub(self.channel)
        req = Hello()
        req.message = message

        res: Hello = stub.SayHello(req)

        self.assertIn(message, res.message)


if __name__ == "__main__":
    unittest.main()
