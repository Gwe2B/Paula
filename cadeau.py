from turtle import *
from math import asin, acos, pi, sqrt
import random as rd

# Defining some constants
GROUND_LVL = 10
WORLD_WIDTH = 1000
WORLD_HEIGHT = 800

# Defining the world coordinate system to be an othonormed coordinate system
# with the origin in the bottom left corner
screensize(WORLD_WIDTH, WORLD_HEIGHT)
setworldcoordinates(0, 0, WORLD_WIDTH, WORLD_HEIGHT)


colormode(255)
#speed(100)

def random_color() -> tuple[int, int, int]:
    """Generate a random color in RGB format from 0 to 255.

    Returns:
        Tuple(int): The respective values of the red, green, and blue components
    """
    r = rd.randint(0, 255)
    g = rd.randint(0, 255)
    b = rd.randint(0, 255)
    return (r, g, b)

def go_to(x: int, y: int) -> None:
    """Just moving the cursor to the given position

    Args:
        x (int): The X coordinate of the new location
        y (int): The Y coordinate of the new location
    """
    penup()
    goto(x, y)
    pendown()

def rad_to_deg(rad: float) -> float:
    return rad * (180/pi)

def sol(y: int) -> None:
    """Create the ground at the given elevation

    Args:
        y (int): The elevation of the ground
    """
    goto(0, y)
    fd(WORLD_WIDTH)

def mur(x: int, y: int, w: int, h: int, color: tuple[int, int, int]) -> None:
    """Create a new wall with the given position and dimensions and color.

    Args:
        x (int): X position of the bottom left corner of the wall.
        y (int): Y position of the bottom left corner of the wall.
        w (int): Width of the wall
        h (int): Height of the wall
        color (tuple[int, int, int]): Color of the wall
    """
    go_to(x, y)
    setheading(0)
    fillcolor(color)
    begin_fill()
    for i in range(4):
        if i % 2 == 0:
            fd(w)
        else:
            fd(h)
        left(90)
    end_fill()

def toit_a(x: int, y: int, w: int, h: int, color: tuple[int, int, int]) -> None:
    """Draw a triangular roof with the given width and height values.

    Args:
        x (int): X position of the bottom left corner of the roof
        y (int): Y position of the bottom left corner of the roof
        w (int): Width of the roof
        h (int): Height of the roof
        color (tuple[int, int, int]): The color to fill the roof with
    """

    buf = sqrt(h**2 + (w/2)**2)
    alpha = rad_to_deg(asin(h/buf))
    beta = rad_to_deg(acos(h/buf))
    go_to(x, y)
    setheading(0)
    fillcolor(color)
    begin_fill()
    for i in range(3):
        if i == 0:
            fd(w)
            left(180 - alpha)
        else:
            fd(buf)
            left(180 - 2*beta)
    end_fill()

def fenetre(x: int, y: int, w: int, h: int, color: tuple[int, int, int]) -> None:
    """Draw a window with the given dimensions at the given coordinates

    Args:
        x (int): X coordinate of the window
        y (int): Y coordinate of the window
        w (int): Width of the window
        h (int): Height of the window
        color (tuple[int, int, int]): Color of the window
    """
    # Un peu d'aide quand même ;-)
    # De mon avis tu doit pouvoir utiliser la fonction mur() défini plus haut
    # pour dessiner tes fenêtres à coup de rectangle.
    # Petit conseil en passant si jamais tu voit que tu va mettre une valeur
    # en "dur" càd directement dans le code du style `fd(120)` crée plutôt une
    # constante au début du fichier `MA_CONSTANTE = 120` que si jamais tu
    # l'utilise à plusieurs endroits tu n'aura à la modifier qu'à un seul endroit
    # pour changer tout le fonctionnement.
    # PS: N'applique pas ça de manière bête et discipliner... va pas crée une
    # constante pour faire des divisions par 2 ou si tu est sure que ca ne va pas
    # bouger. Les angles d'un rectangle vaudront toujours 90° donc `left(90)` est
    # plus intelligent que `left(VALEUR_DE_L_ANGLE_DANS_UN_RECTANGLE)` XD
    # Pour ce qui est des nom de variables tkt c'est juste que j'ai pris l'habitude
    # de suivre les goodpractices et les guidelines des langages que je pratique
    # tu peut les changer mais tu devrais rester en anglais si tu compte aller plus
    # loin en prog.
    pass

sol(GROUND_LVL)
mur(100, GROUND_LVL, 300, 200, random_color())
toit(90, 210, 320, 50, random_color())

# Just because I need it for my IDE
mainloop()