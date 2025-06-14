import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        CircleShape.__init__(self, x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)
        left_velocity = self.velocity.rotate(random_angle)
        right_velocity = self.velocity.rotate(-random_angle)
        split_radius = self.radius - ASTEROID_MIN_RADIUS
        left_asteroid = Asteroid(self.position.x, self.position.y, split_radius)
        left_asteroid.velocity = left_velocity * 1.2
        right_asteroid = Asteroid(self.position.x, self.position.y, split_radius)
        right_asteroid.velocity = right_velocity * 1.2
    