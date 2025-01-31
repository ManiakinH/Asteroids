import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.add(self.containers)
        

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self): 
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        
        new_angle = random.uniform(20, 50)

        vector_1 = self.velocity.rotate(new_angle)
        vector_2 = self.velocity.rotate(-new_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        

        spawn_1 = Asteroid(self.position.x, self.position.y, new_radius)
        spawn_2 = Asteroid(self.position.x, self.position.y, new_radius)
        spawn_1.velocity = vector_1 * 1.2
        spawn_2.velocity = vector_2 * 1.2
        self.kill()