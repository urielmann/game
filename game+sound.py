# Import everything we're going to use for the game
import pygame
import sys

# Intialize game environment
pygame.init()
pygame.display.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Swiming Fish Game') # Set game window title

# Load background image
bg = pygame.image.load('underwater.png') # Screen background
bg_rect  = bg.get_rect()
screen = pygame.display.set_mode((bg_rect.width, bg_rect.height))
# Load animation images
fishs = (pygame.image.load('fish1.png'), pygame.image.load('fish2.png'))
fish_rect = fishs[0].get_rect()
no_fish = len(fishs)
# Load sounds
squeak = pygame.mixer.Sound("squeak.wav")
boing = pygame.mixer.Sound("boing.wav")
# Misc. variables
VELOCITY = 5
step = 0
flip = False

# Main game loop
while pygame.QUIT not in [event.type for event in pygame.event.get()]:
    clock.tick(20)

    # Check keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: # Q: Did the user pressed the left arrow?
        if fish_rect.x > 0: # Q: Is the fish all the way to the left?
            fish_rect.x = fish_rect.x - VELOCITY
            pygame.mixer.Sound.play(squeak)
        else: # The fish hit the wall
            fish_rect.x = fish_rect.x + VELOCITY
            pygame.mixer.Sound.play(boing)
        pygame.mixer.music.stop()            
        step = step + 1
        flip = False # Moving to the left the image stays the same
    elif keys[pygame.K_RIGHT]: # Q: Did the user pressed the right arrow?
        if fish_rect.x + fish_rect.width < bg_rect.width: # Q: Is the fish all the way to the right?
            fish_rect.x = fish_rect.x + VELOCITY
            pygame.mixer.Sound.play(squeak)
        else: # The fish hit the wall
            fish_rect.x = fish_rect.x - VELOCITY
            pygame.mixer.Sound.play(boing)
        pygame.mixer.music.stop()            
        step = step + 1
        flip = True # Moving to the right the image must be flipped

    fish = pygame.transform.flip(fishs[step % no_fish], flip, False)
    # Update the screen
    screen.blit(bg, bg_rect)        # Paint the backgound image
    screen.blit(fish, fish_rect)    # Paint the fish over the backgound
    pygame.display.update()         # Update the screen
    # end of game loop

# Shutdown everything in reverse order of initialization
pygame.display.quit()
pygame.quit()
sys.exit(0)
