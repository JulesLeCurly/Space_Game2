import pygame
import time

class MouseTracker():
    MOUSE_STATE_IDLE = 0
    MOUSE_STATE_PRESSED = 1
    MOUSE_STATE_DRAGGING = 2

    def __init__(self):
        self.current_x = 0
        self.current_y = 0
        self.velocity_x = 0
        self.velocity_y = 0
        self.mouse_timer = time.time()
        self.stress = 1
        self.mouse_state = self.MOUSE_STATE_IDLE
        self.mouse_duration = 0

    def _get_mouse_state(self):
        return [pygame.mouse.get_pressed() != (False, False, False), pygame.mouse.get_pos()]

    def _update_position(self, x, y):
        x -= self.velocity_x * self.stress
        y += self.velocity_y * self.stress

        if y > 90: y = 90
        if y < -90: y = -90

        if x < 0: x = 360
        if x > 360: x = 0

        self.velocity_x = int((self.current_mouse_state[1][0] - self.previous_mouse_position[1][0]))
        self.velocity_y = int((self.current_mouse_state[1][1] - self.previous_mouse_position[1][1]))

        return round(x, 5), round(y, 5)

    def main(self):
        self.current_mouse_state = self._get_mouse_state()
        self.current_mouse_state[0] = self.current_mouse_state[0] #WARNING la souiris et toujours appuier si True

        if self.current_mouse_state[0] and self.mouse_state == self.MOUSE_STATE_IDLE:
            self.mouse_timer = time.time()
            self.mouse_state = self.MOUSE_STATE_PRESSED

        if self.mouse_state == self.MOUSE_STATE_PRESSED and not self.current_mouse_state[0]:
            self.mouse_state = self.MOUSE_STATE_IDLE
            self.mouse_duration = time.time() - self.mouse_timer

        if time.time() - self.mouse_timer > 0.1 and self.mouse_state == self.MOUSE_STATE_PRESSED:
            self.current_x, self.current_y = self._update_position(self.current_x, self.current_y)
        
        elif self.mouse_duration < 0.5 and self.mouse_state == self.MOUSE_STATE_IDLE:
            pass

        self.previous_mouse_position = self.current_mouse_state

        return self.current_x, self.current_y
