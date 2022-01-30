import neoapi
import pyvirtualcam

infolist = neoapi.CamInfoList.Get()
infolist.Refresh()
cameras = []
for info in infolist:
    serial_number = info.GetSerialNumber()
    camera = neoapi.Cam()
    camera.Connect(serial_number)
    if camera.f.PixelFormat.GetEnumValueList().IsReadable('BGR8'):
        camera.f.PixelFormat.SetString('BGR8')
    elif camera.f.PixelFormat.GetEnumValueList().IsReadable('Mono8'):
        camera.f.PixelFormat.SetString('Mono8')
    else:
        raise camera.CameraException('no supported pixel format')
    camera.f.ExposureTime.Set(190000)
    camera.f.AcquisitionFrameRateEnable.value = True
    camera.f.AcquisitionFrameRate.value = 10
    cameras.append(camera)

camera_to_fake = {}
i = 0
for camera in cameras:
    camera_to_fake[camera] = pyvirtualcam.Camera(width=camera.f.Width.value,
                                                 height=camera.f.Height.value,
                                                 fmt=pyvirtualcam.PixelFormat.GRAY,
                                                 fps=camera.f.AcquisitionFrameRate.value)

while True:
    for camera in cameras:
        virtual_camera = camera_to_fake[camera]
        image = camera.GetImage().GetNPArray().reshape(camera.f.Height.value, camera.f.Width.value)
        virtual_camera.send(image)
