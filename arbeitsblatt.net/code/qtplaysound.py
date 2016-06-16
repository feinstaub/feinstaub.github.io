from PyQt5.QtCore import Qt, QUrl, QTimer
from PyQt5.QtMultimedia import (QAudio, QMediaPlayer, QMediaContent, QSound)
from PyQt5.QtWidgets import (QApplication)
import os
#import threading

class PlaySound:
    """
    Synchronously play sound files.
    """

    def __init__(self):
        self.volume = 50

    def set_volume(self, v):
        self.volume = v

    def play_file(self, filename, max_time_ms = None):
        """
        Starts playing the sound file 'filename' and
        waits until playing is finish.

        When max_time_ms is specified the sound will terminate
        after the given milliseconds.
        """

        app = QApplication([ 'PlaySoundClass' ])
        app.setApplicationName("Audio Output Test")

        player = QMediaPlayer()
        #connect(player, SIGNAL(positionChanged(qint64)), this, SLOT(positionChanged(qint64)));
        player.stateChanged.connect(self._playerStateChanged)
        player.error.connect(self._playerError)

        url = QUrl.fromLocalFile(os.path.abspath(filename)) # we need abspath otherwise a relative file does not work
        player.setMedia(QMediaContent(url))
        player.setVolume(self.volume)

        if max_time_ms:
            timer = QTimer()
            # http://eli.thegreenplace.net/2011/04/25/passing-extra-arguments-to-pyqt-slot
            timer.singleShot(max_time_ms, lambda: self._playerDoStop(player));

        player.play()

        app.exec_()

    #def play_file_async(self, filename):
        #app = QApplication([ 'PlaySoundClass2' ])
        #app.setApplicationName("Audio Output Test2")

        ##t = threading.Thread(target=self.play_file, args=[filename])
        ##t.daemon = True  # thread dies when main thread (only non-daemon thread) exits.
        ##t.start()
        #QSound.play(filename)

    def _playerStateChanged(self, state):
        if state == QMediaPlayer.StoppedState:
            QApplication.quit()

    def _playerError(self, error):
        QApplication.quit()

    def _playerDoStop(self, player):
        player.stop()

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
