import camera
import neoapi
import numpy


class GenICamCamera(camera.Camera):
    def __init__(self, _id: str):
        super().__init__(_id, False, 0, 0)
        self.camera = neoapi.Cam()

    def set_activeness(self, is_active: bool):
        try:
            if is_active:
                if not self.camera.IsConnected():
                    self.camera.Connect(self.id)

                    self.is_color = True
                    if self.camera.f.PixelFormat.GetEnumValueList().IsReadable('BGR8'):
                        self.camera.f.PixelFormat.SetString('BGR8')
                    elif self.camera.f.PixelFormat.GetEnumValueList().IsReadable('Mono8'):
                        self.camera.f.PixelFormat.SetString('Mono8')
                        self.is_color = False
                    else:
                        raise camera.CameraException('no supported pixel format')

                    self.camera.f.ExposureTime.Set(10000)
                    self.camera.f.AcquisitionFrameRateEnable.value = True
                    self.camera.f.AcquisitionFrameRate.value = 10
                    self.width = self.camera.f.Width.value
                    self.height = self.camera.f.Height.value
            elif self.camera.IsConnected():
                self.camera.Disconnect()
        except neoapi.NeoException as e:
            print(e)
            raise camera.CameraException()
        super(GenICamCamera, self).set_activeness(is_active=is_active)

    def get_image(self) -> numpy.ndarray:
        try:
            return self.camera.GetImage().GetNPArray()
        except neoapi.NeoException as e:
            raise camera.CameraException()
