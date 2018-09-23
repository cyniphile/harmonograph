import pygame
import numpy as np


def rotate_vector(point, theta, degrees=True):
    if degrees:
        # convert degrees to radians
        theta = theta / 360 * (2 * np.pi)
    rotation_matrix = [
        [np.cos(theta), -1 * np.sin(theta)],
        [np.sin(theta), np.cos(theta)]
    ]
    return np.matmul(rotation_matrix, point)


def draw():
    pygame.init()

    BLACK = [0, 0, 0]
    WHITE = [255, 255, 255]
    SIZE = [1000, 1000]

    screen = pygame.display.set_mode(SIZE)
    start_pos = [int(SIZE[0]//2), int(SIZE[1]//2)]

    clock = pygame.time.Clock()

    # Loop until the user clicks the close button.
    done = False

    AMPLITUDE_X = 500
    AMPLITUDE_Y = 100
    AMPLITUDE_Z = 100
    PHASE_XY = 1
    PHASE_Z = 3
    PERIOD_X = 1.01
    PERIOD_Y = 1
    PERIOD_Z = .90
    DECAY = 0.05
    ANGLE_Z = 90  # angle of vibration. 0 == X axis

    SPEED = 4

    start_time = pygame.time.get_ticks()
    points = []
    speed_offset = 0
    while not done:

        for event in pygame.event.get():   # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True   # Flag that we are done so we exit this loop

        screen.fill(BLACK)

        if len(points) > 1:
            pygame.draw.aalines(screen, WHITE, 0, points)

        t = (pygame.time.get_ticks() - start_time + speed_offset) / 1000

        for i in range(SPEED):
            t = t + 20 * i / 1000
            decay_coeff = 1 - t * DECAY

            z_factor = [0, 0]
            z_factor[0] = decay_coeff * AMPLITUDE_Z * np.cos((t + PHASE_Z) / PERIOD_Z)
            z_factor[1] = 0
            z_rotated = rotate_vector(z_factor, ANGLE_Z)

            new_point = start_pos.copy()
            new_point[0] += decay_coeff * AMPLITUDE_X * np.cos((t + PHASE_XY) / PERIOD_X)
            new_point[1] += decay_coeff * AMPLITUDE_Y * np.cos(t / PERIOD_Y)
            new_point[0] += z_rotated[0]
            new_point[1] += z_rotated[1]
            points.append(new_point)
            # print(new_point)
        speed_offset += SPEED * 20
        pygame.display.flip()
        clock.tick(20 * SPEED)
    pygame.quit()


if __name__ == "__main__":
    draw()
