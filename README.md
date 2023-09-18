---------------------------------------------------------------------------
    Python SuperAFK-Bot - README
---------------------------------------------------------------------------

This script is designed to mimic human-like mouse behavior on a regular 1080p monitor using the PyAutoGUI library. It introduces randomness, variability, and natural pauses to make the script's actions appear more human.

---------------------------------------------------------------------------
    Requirements
---------------------------------------------------------------------------

- Python 3.x
- PyAutoGUI library (install using 'pip install pyautogui')

---------------------------------------------------------------------------
    How to Use
---------------------------------------------------------------------------

1. Install Python:
   If you don't have Python installed, download and install it from the official Python website (https://www.python.org/downloads/).

2. Install PyAutoGUI:
   Install the PyAutoGUI library using pip by running the following command in your terminal or command prompt:
   

3. Configure Screen Resolution (optional):
The script is configured for a regular 1080p monitor (1920x1080 resolution). If your screen resolution is different, modify the `screen_width` and `screen_height` variables in the script to match your monitor's resolution.

4. Run the Script:
Run the script by executing it using Python from your terminal or command prompt:


5. Monitor the Output:
The script will start mimicking human-like mouse behavior, including random movements, clicks, scrolls, and pauses. The "AFK Counter" will track inactivity and trigger random movements after a period of inactivity.

6. Handling Fail-Safe:
The script includes a fail-safe mechanism to prevent the mouse from moving to the screen's corners. If you encounter a "pyautogui.FailSafeException," it's because the mouse is approaching the screen's corners. The script handles this exception gracefully and continues running. Disabling the fail-safe is not recommended.

---------------------------------------------------------------------------
 Customization
---------------------------------------------------------------------------

You can customize the behavior of the script by adjusting the following parameters within the script:

- Probability values for clicks, scrolls, and small mouse movements.
- Delays between actions (randomized for natural pauses).
- Speed and offsets for mouse movements.
- Screen resolution (if your monitor is not 1080p).

Feel free to modify these parameters to fine-tune the script's behavior according to your preferences.

---------------------------------------------------------------------------
 Disclaimer
---------------------------------------------------------------------------

Use this script responsibly and only on systems and applications where automation is allowed and in compliance with applicable laws and regulations. The purpose of this script is to simulate human-like mouse behavior for testing and educational purposes.


