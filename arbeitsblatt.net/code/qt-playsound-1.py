#!/usr/bin/python3

from qtplaysound import PlaySound
import time

def main():
    sound = PlaySound()
    print("PlaySound demo")

    print("  Play sound at default volume (50)...")
    sound.play_file('sound-glitzern1.ogg')

    print("  Set volume to 20...")
    sound.set_volume(20)
    sound.play_file('sound-glitzern1.ogg')

    print("  Play for 2 seconds...")
    sound.play_file('/usr/share/kde4/apps/amarok/data/first_run_jingle.ogg', 2000)

    print("Exit program.")

if __name__ == "__main__":
    main()
