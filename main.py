import pygame
import math
import random

pygame.init()

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Interactive Black Hole Simulation")

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Load the space background image
space_background = pygame.image.load("space_background.jpg")
space_background = pygame.transform.scale(space_background, (WIDTH, HEIGHT))

# Constants
G = 6.67430e-11  # Gravitational constant
M = 1.989e30  # Mass of black hole (e.g., equivalent to one solar mass)
SCALE = 5e-10  # Adjusted scale for the simulation
TIMESTEP = 3600 * 12  # Half a day in seconds
DAMPING = 0.999  # Velocity damping factor
ABSORPTION_RADIUS = 1e10  # Distance within which particles get absorbed
MAX_FRAGMENT_DEPTH = 2  # Maximum depth of fragmentation
MAX_PARTICLES = 1000  # Maximum number of particles in the simulation

class Particle:
    pass

class BlackHoleSimulation:
    pass
