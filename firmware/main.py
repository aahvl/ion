import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.scanners.keypad import KeysScanner

keyboard = KMKKeyboard()

keyboard.extensions.append(MediaKeys())

rotary_encoder = EncoderHandler()
keyboard.modules.append(rotary_encoder)

rotary_encoder.pins = (
    (board.A0, board.A1, board.A2, False),
)

rotary_encoder.map = [
    ((KC.VOLD, KC.VOLU),),
]

keyboard.matrix = KeysScanner(
    pins=[board.A10, board.A9, board.A8],
)

keyboard.keymap = [
    [
        KC.LCTL(KC.C), KC.LCTL(KC.V), KC.LCTL(KC.X),
        KC.MUTE,
    ],
]

if __name__ == "__main__":
    keyboard.go()
