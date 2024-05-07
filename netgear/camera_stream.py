from vidgear.gears import VideoGear
from vidgear.gears import NetGear 

class CaptureVideoGear:
  def __init__(self, camera_url:str):
    self.cam = VideoGear(source=camera_url).start()
    
  def read_frame(self):
    return self.cam.read()
  
  def stop(self):
    self.cam.stop()

class NetgearServer:
  def __init__(self, port):
    options = {"flag": 0, "copy": False, "track": False,"max_retries": 5, "request_timeout":20}
    self.server = NetGear(  address="127.0.0.1",
                            port=port,
                            protocol="tcp",
                            pattern=0,
                            logging=False,
                            **options )
    
  def send_frame(self, frame):
    self.server.send(frame)
  
  def close(self):
    self.server.close()
    
def main_camera_service(camera_url, port):
  camera = CaptureVideoGear(camera_url)
  server = NetgearServer(port)
  
  try:
    while True:
      frame = camera.read_frame()
      if frame is None:
        print("Encountered a None frame")
        break
      server.send_frame(frame)

  except KeyboardInterrupt:
      camera.stop()
      server.close()
      
  except Exception as e:
      camera.stop()
      server.close()
      print(f"Error during streaming: {e}")












# class CameraStream():
#         def __init__(self, camera_url:str, puerto):            
#             self.cam = VideoGear(source=camera_url).start()
#             self.puerto= puerto
#             options = {"flag": 0, "copy": False, "track": False,"max_retries": 5, "request_timeout":20}
#             self.server = NetGear(  address="127.0.0.1",
#                                     port=puerto,
#                                     protocol="tcp",
#                                     pattern=0,
#                                     logging=False,
#                                     **options)
                                            
#         def start_streaming(self):
#           while True: 
#               try:
#                 frame = self.cam.read()
#                 if frame is None :
#                       print("Encountered a None frame")
#                       break
#                 self.server.send(frame)

#               except KeyboardInterrupt:
#                 self.stop_streaming()
#                 break
                
#         def stop_streaming(self):
#             self.cam.stop()
#             print("Server closed")
            
# def main_camera_service(rtsp_url, puerto):
#     video = CameraStream(rtsp_url, puerto)
#     try:
#         video.start_streaming()
#     except Exception as e:
#         video.server.close()
#         print(f"Error during streaming: {e}")