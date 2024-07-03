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
    def __init__(self, x, y, radius, color, mass, fragment_depth=0):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        self.x_vel = random.uniform(-2e3, 2e3)  # Initial velocity in m/s
        self.y_vel = random.uniform(-2e3, 2e3)  # Initial velocity in m/s
        self.trail = []
        self.fragment_depth = fragment_depth

    def draw(self, win):
        x = self.x * SCALE + WIDTH / 2
        y = self.y * SCALE + HEIGHT / 2
        if not (math.isnan(x) or math.isnan(y)):  # Ensure x and y are valid numbers
            pygame.draw.circle(win, self.color, (int(x), int(y)), self.radius)
            if len(self.trail) > 1:
                scaled_trail = [(pos[0] * SCALE + WIDTH / 2, pos[1] * SCALE + HEIGHT / 2) for pos in self.trail]
                pygame.draw.lines(win, self.color, False, scaled_trail, 1)

    def update_position(self, black_hole):
        distance_x = black_hole.x - self.x
        distance_y = black_hole.y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if distance < ABSORPTION_RADIUS:
            return False  # Particle absorbed by the black hole

        force = G * black_hole.mass * self.mass / distance ** 2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force

        self.x_vel += force_x / self.mass * TIMESTEP
        self.y_vel += force_y / self.mass * TIMESTEP

        # Apply damping
        self.x_vel *= DAMPING
        self.y_vel *= DAMPING

        self.x += self.x_vel * TIMESTEP
        self.y += self.y_vel * TIMESTEP

        # Update trail
        self.trail.append((self.x, self.y))
        if len(self.trail) > 50:
            self.trail.pop(0)

        return True  # Particle still in the simulation

class BlackHoleSimulation:
    def __init__(self):
        self.black_hole = Particle(0, 0, 21, BLACK, M)
        self.particles = [self.create_orbiting_particle() for _ in range(5)]  # Initial 5 particles
        self.paused = False
        self.simulation_speed = 1.0

    def create_orbiting_particle(self):
        angle = random.uniform(0, 2 * math.pi)
        distance = random.uniform(1e11, 2e11)
        x = distance * math.cos(angle)
        y = distance * math.sin(angle)
        color = [random.randint(0, 255) for _ in range(3)]
        particle = Particle(x, y, 3, color, 1e20)
        
        # Set velocity for orbiting
        velocity_magnitude = math.sqrt(G * M / distance)
        particle.x_vel = -velocity_magnitude * math.sin(angle)
        particle.y_vel = velocity_magnitude * math.cos(angle)
        return particle

    def draw(self, win):
        win.blit(space_background, (0, 0))
        self.black_hole.draw(win)
        for particle in self.particles:
            particle.draw(win)

    def update(self):
        if not self.paused:
            new_particles = []
            for particle in self.particles:
                if not particle.update_position(self.black_hole):
                    if len(self.particles) + len(new_particles) < MAX_PARTICLES:
                        # Particle absorbed, create fragments
                        new_particles.extend(particle.fragment())
                else:
                    new_particles.append(particle)
            self.particles = new_particles

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.paused = not self.paused
            if event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                self.simulation_speed *= 1.1
            if event.key == pygame.K_MINUS:
                self.simulation_speed /= 1.1
            if event.key == pygame.K_a:
                # Add a new particle with random initial position and velocity
                if len(self.particles) < MAX_PARTICLES:
                    self.particles.append(self.create_orbiting_particle())
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click to add a new particle
                if len(self.particles) < MAX_PARTICLES:
                    self.particles.append(self.create_orbiting_particle())

    def run(self):
        clock = pygame.time.Clock()
        run = True

        while run:
            clock.tick(60)
            WIN.fill(BLACK)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                self.handle_event(event)

            self.update()
            self.draw(WIN)

            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    simulation = BlackHoleSimulation()
    simulation.run()