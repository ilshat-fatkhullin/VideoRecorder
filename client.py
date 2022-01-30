import logging

import cv2
import grpc
import api_pb2
import api_pb2_grpc
import pickle


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = api_pb2_grpc.APIStub(channel)

        response = stub.GetCameras(api_pb2.Void())
        id = response.list[0].id

        request = api_pb2.SetCameraActivenessRequest()
        request.id = id
        request.isActive = True
        stub.SetCameraActiveness(request)

        request = api_pb2.SubscribeOnCameraRequest()
        request.id = id
        response = stub.SubscribeOnCamera(request)
        for result in response:
            frame = pickle.load(result.data)
            cv2.namedWindow(id, cv2.WINDOW_NORMAL)
            cv2.imshow(id, frame)
    print("Client received:\n" + response)


if __name__ == '__main__':
    logging.basicConfig()
    run()
