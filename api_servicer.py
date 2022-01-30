import cameras
import grpc
import api_pb2
import api_pb2_grpc
import pickle
import cv2


class APIServicer(api_pb2_grpc.APIServicer):

    def __init__(self, cameras_list: cameras.Cameras):
        self.cameras = cameras_list

    async def GetCameras(self, request: api_pb2.Void, context: grpc.aio.ServicerContext):
        result = api_pb2.GetCamerasResult()
        for c in self.cameras.get_cameras():
            camera = api_pb2.Camera()
            camera.id = c.id
            camera.isActive = c.is_active
            result.list.append(camera)
        return result

    async def SetCameraActiveness(self, request: api_pb2.SetCameraActivenessRequest, context: grpc.aio.ServicerContext):
        result = api_pb2.ActionReport()
        try:
            self.cameras.set_camera_activeness(id=request.id, is_active=request.isActive)
            result.isSuccessful = True
        except cameras.CamerasException as e:
            result.isSuccessful = False
            result.message = str(e)
        return result

    async def SubscribeOnCamera(self, request, context):
        if request.id not in self.cameras.id_to_camera:
            raise ValueError('id does not exist')
        camera = self.cameras.id_to_camera[request.id]
        if not camera.is_active:
            raise ValueError('Camera is not active')
        frame_index = 0
        while True:
            if frame_index == camera.frame_index:
                continue
            frame_index = camera.frame_index
            result = api_pb2.VideoChunk()
            result.data = pickle.dumps(camera.frame)
            yield result
