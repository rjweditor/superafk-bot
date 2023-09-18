import pyautogui as pag
import random
import time

# Set the screen resolution
screen_width = 1920
screen_height = 1080

curr_coords = pag.position()
afk_counter = 0

while True:
    try:
        if pag.position() == curr_coords:
            afk_counter += 1
        else:
            afk_counter = 0
            curr_coords = pag.position()

        if afk_counter > 5:
            # Generate random coordinates within the screen boundaries
            x = random.randint(0, screen_width)
            y = random.randint(0, screen_height)

            # Add random offset to simulate human mouse movement
            x += random.randint(-50, 50)
            y += random.randint(-50, 50)

            # Ensure generated coordinates are within screen boundaries
            x = max(0, min(x, screen_width))
            y = max(0, min(y, screen_height))

            pag.moveTo(x, y, duration=random.uniform(0.2, 0.8))
            curr_coords = pag.position()

            # Simulate occasional mouse clicks and scrolls
            if random.random() < 0.05:
                pag.click()

            if random.random() < 0.02:
                scroll_amount = random.randint(-3, 3)
                pag.scroll(scroll_amount)

            # Simulate small mouse movements
            if random.random() < 0.1:
                x_offset = random.randint(-10, 10)
                y_offset = random.randint(-10, 10)
                pag.move(x_offset, y_offset, duration=0.1)

        print(f'AFK Counter: {afk_counter}')
        time.sleep(random.uniform(1, 3))  # Add random delays between actions
    except pag.FailSafeException:
        # Handle the fail-safe exception here (you can log it or take other actions)
        pass
