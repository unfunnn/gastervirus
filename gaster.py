import pygame
from pygame.locals import *
import os
import win32api
import win32con
import win32gui

def always_on_top():
    win32gui.SetWindowPos(pygame.display.get_wm_info()['window'], win32con.HWND_TOPMOST, 0, 0, 0, 0,
                          win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

def make_transparent():
    hwnd = pygame.display.get_wm_info()["window"]
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                           win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)

    win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY)

real_path = os.path.realpath(__file__)
dir_path = os.path.dirname(real_path)

fuchsia = (255, 0, 128)

screen = pygame.display.set_mode((win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)), NOFRAME)

gaster = pygame.image.load("gaster.png").convert_alpha()

pygame.display.set_caption("Hi! I'm Wing Gaster! The Royal Scient")
pygame.display.set_icon(gaster)

make_transparent()
screen.fill(fuchsia)
always_on_top()

running = True

while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if keys[pygame.K_w] and keys[pygame.K_d] and keys[pygame.K_g]:
        screen.fill(fuchsia)
    screen.blit(gaster, (win32api.GetCursorPos()[0], win32api.GetCursorPos()[1]))
    pygame.display.flip()
    pygame.display.update()