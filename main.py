import pygame
import time
import os

# Initialize pygame
pygame.init()

# Set up file paths
background_path = r"C:\Users\Arpita\Downloads\holi back.jpg"
overlay_path = r"C:\Users\Arpita\Downloads\123.jpg"
font_path = r"C:\Users\Arpita\Downloads\dripping_marker.ttf"  # Custom Holi-style font

# Load images
background = pygame.image.load(background_path)
overlay = pygame.image.load(overlay_path)

# Get screen size from the background image
screen_width, screen_height = background.get_size()
screen = pygame.display.set_mode((screen_width, screen_height))

# Display the background image
screen.blit(background, (0, 0))
pygame.display.update()
time.sleep(1)  # Show background for 1 second

# Load custom font (if available), otherwise use a fallback font
try:
    font = pygame.font.Font(font_path, 200)  # Increase font size
except:
    font = pygame.font.SysFont("jokerman", 200)  # Fallback font

# Define Holi colors (Ensuring 'H' is Orange)
colors = [
    (255,0,0),  # Red (for H)
    (255, 165, 0),    # Orange
    (255, 255, 0),  # Yellow
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (75, 0, 130),   # Indigo
    (255,0,0),  # red
    (255, 20, 147), # Pink
    (0, 255, 255),  # Cyan
    (255, 140, 0)   # Deep Orange
]

text = "HAPPY HOLI"
letter_spacing = 120  # Adjusted spacing for bigger size
start_x = (screen_width - (letter_spacing * len(text))) // 2
start_y = screen_height // 2 - 100

# Display each letter one by one with different colors
for i, letter in enumerate(text):
    color = colors[i] if i < len(colors) else (255, 255, 255)  # Default white if out of colors
    letter_surface = font.render(letter, True, color)
    screen.blit(letter_surface, (start_x + i * letter_spacing, start_y))
    pygame.display.update()
    time.sleep(0.5)  # Delay for animation effect

# Wait for 1 second after the text is fully displayed
time.sleep(1)

# Quit Pygame and close the screen
pygame.quit()
