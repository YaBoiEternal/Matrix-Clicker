import pygame
import sys

pygame.init()

sch = 960
scw = 640
halfscw = 320
halfsch = 480
rectsize = 20
txtsize1 = 55
txtsize2 = 100
txtsize3 = 21
speedernum = "640"
sptnum = "1200"
scorenum = "0"
spacetime = "0"

sc = pygame.display.set_mode((sch, scw))
pygame.display.set_caption("Matrix Clicker")
clock = pygame.time.Clock()

green = (0, 255, 0)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
w = 50
h = 50
coloract = green
colorpas = black


random = 0

pygame.display.update()

start = False
activewhile = True
activeif1 = True
activeif2 = True

while True:
  for event in pygame.event.get():
    if start == False:
      fsb = pygame.font.SysFont("basicsansbold", txtsize3)
      game = fsb.render("click to begin. ", txtsize3, green)
      sc.blit(game, (420, 520))
      start = True
    if start == True:
      if event.type == pygame.MOUSEBUTTONUP:
        greensqu = pygame.draw.rect(sc, coloract, [halfsch, halfscw, 400, 100], 1000000)

        pos = pygame.mouse.get_pos()

        speedersqu = pygame.draw.rect(sc, colorpas, [120, 500, 400, 100], 1000000)

        buyfont = pygame.font.SysFont("basicsansbold", 34)
        speedertxt = str(speedernum)
        if activeif1 == True:
          speedercost = buyfont.render("SPEEDER COST: " + speedertxt, 100, coloract)
          sc.blit(speedercost, (420, 600))

        sptfont = pygame.font.SysFont("basicsansbold", 34)
        spttxt = str(sptnum)
        if activeif2 == True:
          sptcost = sptfont.render("SPACETIME COST: " + spttxt, 100, coloract)
          sc.blit(sptcost, (20, 600))

          speedernum = int(speedertxt)
          fsb = pygame.font.SysFont("basicsansbold", txtsize2)
          scoretxt = str(scorenum)
          if activeif1 == True:
            score = fsb.render("SCORE: " + scoretxt, 100, coloract)
            sc.blit(score, (270, 20))
            pygame.draw.rect(sc, colorpas, [270, 20, 800, 100], 1000000)
            score = fsb.render("SCORE: " + scoretxt, 100, coloract)
            sc.blit(score, (270, 20))

            scorenum = int(scoretxt)

            if greensqu.collidepoint(pos):
              scorenum = scorenum + 1

            if scorenum >= 61:
              scorenum = int(scoretxt)
              scorenum = scorenum + 2
            if scorenum >= 181:
              txtspacetime = str(spacetime)
              fspt = pygame.font.SysFont("basicsansbold", txtsize2)

              spt = fspt.render("SPACETIME: " + txtspacetime, 100, coloract)
              sc.blit(spt, (270, 90))
              pygame.draw.rect(sc, colorpas, [270, 90, 800, 100], 1000000)
              spt = fspt.render("SPACETIME: " + txtspacetime, 100, coloract)
              sc.blit(spt, (270, 90))

              spacetime = int(txtspacetime)

              if spacetime >= 1801:
                errorf = pygame.font.SysFont("basicsansbold", txtsize2)

                pygame.draw.rect(sc, red, [0, 300, 960, 50], 1000000)
                error = errorf.render("AN ERROR IN THE MATRIX!", 50, yellow)
                sc.blit(error, (0, 300))
              if spacetime >= 2001:
                pygame.quit()
              spacetime = int(txtspacetime)
              spacetime = scorenum + 1
            if scorenum >= 501:


              scorenum = int(scoretxt)
              scorenum = scorenum + 5
            if scorenum >= 1201:
              scorenum = int(scoretxt)
              scorenum = scorenum + 7

    pygame.display.update()
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()