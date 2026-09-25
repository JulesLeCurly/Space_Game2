import time

class FPS():
    def __init__(self):
        self.auto_fps = False
        self.FPS_target = 30
        self.FPS_timer = time.time()
        self.FPS = 0
        self.FPS_count = 0
    
    def main(self):
        self.FPS_count += 1
        if time.time() > self.FPS_timer+0.5:
                self.FPS = self.FPS_count*2
                self.FPS_timer = time.time()
                self.FPS_count = -1
        
        return self.FPS