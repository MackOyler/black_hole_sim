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
    def __init__(self):
        self.black_hole = Particle(0, 0, 21, BLACK, M)
        self.particles = [self.create_orbiting_particle() for _ in range(5)]  # Initial 5 particles
        self.paused = False
        self.simulation_speed = 1.0

    def create_orbiting_particle(self):
        pass
    
    def draw(self, win):
        win.blit(space_background, (0, 0))
        self.black_hole.draw(win)
        for particle in self.particles:
            particle.draw(win)
     

if __name__ == "__main__":
    simulation = BlackHoleSimulation()
    simulation.run()