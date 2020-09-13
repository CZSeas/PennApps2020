from playsound import playsound
import numpy as np

sounds = {
    (0, 0): 'sounds/melody.mp3',
    (0, 1): 'sounds/high.mp3',
    (1, 0): 'sounds/bassline.mp3',
    (1, 1): 'sounds/lick.mp3'
}


class AudioPlayer:
    def __init__(self):
        self.playing_x = None
        self.playing_y = None
        self.playing = np.zeros((2, 2))
        self.sounds = sounds

    def play_sound(self, pos, page_width, page_height):
        x_inc = page_width // 2
        y_inc = page_height // 2
        x = int(pos[0]) // x_inc
        y = int(pos[1]) // y_inc
        if x != self.playing_x:
            self.playing_x = x
        if y != self.playing_y:
            self.playing_y = y
        if not self.playing[y][x]:
            self.playing[y][x] = True
            playsound(sounds[(y, x)], block=False)

