import unittest
from unittest.mock import MagicMock, patch
from arduino_communication import send_to_arduino


class TestSendToArduino(unittest.TestCase):
    @patch("arduino_communication.time.sleep", autospec=True)
    def test_send_to_arduino(self, mock_sleep):
        # Arrange
        cmyk = (100, 0, 0, 0)
        mock_serial = MagicMock()

        # Act
        send_to_arduino(cmyk, serial=mock_serial)

        # Assert
        mock_serial.write.assert_called_once_with(b"100,0,0,0\n")
        mock_sleep.assert_called_once_with(0.1)

    def test_send_to_arduino_different_values(self):
        # Arrange
        cmyk = (50, 50, 50, 50)
        mock_serial = MagicMock()

        # Act
        send_to_arduino(cmyk, serial=mock_serial)

        # Assert
        mock_serial.write.assert_called_once_with(b"50,50,50,50\n")


if __name__ == "__main__":
    unittest.main()
