# from http://www.python-sfml.org/gettingstarted.html
# geht noch nicht, siehe https://github.com/Sonkun/python-sfml/issues/122

import sfml as sf


# create the main window
window = sf.RenderWindow(sf.VideoMode(640, 480), "pySFML Window")

try:
   # load a sprite to display
   ## texture = sf.Texture.from_file("cute_image.png")
   ## sprite = sf.Sprite(texture)

   # create some graphical text to display
   ## font = sf.Font.from_file("arial.ttf")
   ## text = sf.Text("Hello SFML", font, 50)

   # load music to play
   ## music = sf.Music.from_file("nice_music.ogg")
   pass

except IOError: exit(1)

# play the music
## music.play()

# start the game loop
while window.is_open:
   # process events
   for event in window.events:
      # close window: exit
      if type(event) is sf.CloseEvent:
         window.close()

   window.clear() # clear screen
   ## window.draw(sprite) # draw the sprite
   ## window.draw(text) # draw the string
   window.display() # update the window

