import pygame

class Game():
  def __init__(self, board, screenSize):
    self.board = board
    self.screenSize = screenSize
    self.loadImages

  def run(self):
    pygame.init()
    screen = pygame.display.set_mode(self.screenSize)
    running = True
    while running:
      for event in pygame.event.get()
        if (event.type == pygame.QUIT):
          running = False
      self.draw()
      pygame.display.flip()
    pygame.quit()

    def draw(self):
      pass

    def loadImages(self):
      self.images = {}