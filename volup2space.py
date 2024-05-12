from pynput.keyboard import Key, Controller, Listener

controller = Controller()

def on_press(key):
    print(key)

def on_release(key):
    if key == Key.media_volume_up:
        controller.press(Key.media_volume_down)
        controller.release(Key.media_volume_down)
        controller.press(Key.space)
        controller.release(Key.space)

# Collect events until released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
