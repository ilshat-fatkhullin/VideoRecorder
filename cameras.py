import neoapi
import camera
import genicam_camera


class Cameras:
    def __init__(self):
        self.id_to_camera = {}
        self.infolist = neoapi.CamInfoList.Get()

    def get_cameras(self) -> [camera.Camera]:
        self.__update_cameras_list__()
        return self.id_to_camera.values()

    def get_active_cameras(self):
        return [c for c in self.id_to_camera.values() if c.is_active]

    def set_camera_activeness(self, id: str, is_active: bool):
        if not (id in self.id_to_camera):
            raise CamerasException()
        cam = self.id_to_camera[id]
        cam.set_activeness(is_active=is_active)

    def __update_cameras_list__(self):
        self.infolist.Refresh()
        id_to_camera = {}
        for info in self.infolist:
            if not info.IsConnectable():
                continue
            _id = info.GetId()
            if _id in self.id_to_camera:
                id_to_camera[_id] = self.id_to_camera[_id]
            else:
                id_to_camera[_id] = genicam_camera.GenICamCamera(_id=_id)
        self.id_to_camera = id_to_camera


class CamerasException(Exception):
    pass
