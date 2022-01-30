import cv2
import numpy
import threading
import datetime

"""
Base class for camera
"""


class Camera:
    def __init__(self, _id: str, _is_color: bool, _width: int, _height: int, _port: int):
        self.id = _id
        self.is_active = False
        self.is_color = _is_color
        self.width = _width
        self.height = _height
        self.video = None
        self.process = threading.Thread(target=self.__process__)
        self.process.start()

    def set_activeness(self, is_active: bool):
        if self.is_active == is_active:
            return
        self.is_active = is_active
        if self.is_active:
            date = datetime.datetime.now().strftime('%d-%m-%y-%H-%M-%S')
            file_name = './records/%s-%s.avi' % (self.id, date)
            self.video = cv2.VideoWriter(file_name, cv2.VideoWriter_fourcc(*'XVID'), 10,
                                         (self.width, self.height), self.is_color)
        elif self.video is not None:
            self.video.release()

    def get_image(self) -> numpy.ndarray:
        raise NotImplementedError()

    def __process__(self):
        while True:
            if not self.is_active:
                continue
            if self.video is None and self.stream is None:
                continue
            image = self.get_image()
            if self.video is not None:
                self.video.write(image)
            if self.stream is not None:
                self.stream.write(image)


class CameraException(Exception):
    pass
