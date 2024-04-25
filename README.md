# Color Picker to Arduino

This project is a Python application that captures video from an IP camera, identifies the color of the pixel in the center of the frame, and sends the corresponding CMYK color values to an Arduino.

## Project Structure

- [`arduino_communication.py`](./arduino_communication.py): Contains the function for sending data to the Arduino over a serial connection.
- [`color_conversion.py`](./color_conversion.py): Contains functions for converting RGB colors to CMYK and for getting the name of the nearest color from a predefined list.
- [`colors.py`](./colors.py): Defines the list of predefined colors and their RGB values, and creates a nearest neighbors model for color name retrieval.
- [`drawing.py`](./drawing.py): Contains functions for drawing on the video frame.
- [`main.py`](./main.py): The main script that captures video, identifies the center pixel color, and sends the CMYK values to the Arduino.
- [`main.ino`](./main.ino): The Arduino sketch that receives the CMYK values and controls the color pumps accordingly.
- [`test_arduino_communication.py`](./test_arduino_communication.py): Contains unit tests for the `send_to_arduino` function.
- [`requirements.txt`](./requirements.txt): Lists the Python dependencies for this project.

## Setup

1. Install the Python dependencies:

   ```sh
   pip install -r requirements.txt
   ```

2. Upload the [`main.ino`](./main.ino) sketch to your Arduino.

3. Run the [`main.py`](./main.py) script:

   ```sh
   python main.py
   ```

## Usage

While the [`main.py`](./main.py) script is running, it will display the video from the IP camera in a window. The center pixel of the frame is marked with a cross, and a square in the top-left corner shows its color. The name of the nearest predefined color is displayed at the top of the frame.

Press Enter to send the CMYK values of the center pixel color to the Arduino. Press 'q' to quit the application.

## Testing

To run the unit tests, use the following command:

```sh
python -m unittest test_arduino_communication.py
```

## License

This project is licensed under the terms of the MIT license.
