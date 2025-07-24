from machine import UART #pip install micropython-machine
import time

# Initialize UART with error handling
try:
    uart = UART(0, baudrate=115200, tx=0, rx=1)  # Adjust pins as needed
    print("UART initialized successfully")
except Exception as e:
    print(f"Failed to initialize UART: {e}")
    raise

while True:
    try:
        if uart.any():
            line = uart.readline()
            if line:
                try:
                    decoded_line = line.decode('utf-8').strip()
                    print(decoded_line)
                except UnicodeDecodeError:
                    # Handle potential encoding issues
                    print(f"Raw bytes received: {line}")
    except OSError as e:
        print(f"UART error: {e}")
        time.sleep(1)  # Wait longer on error
    except KeyboardInterrupt:
        print("Program interrupted by user")
        break
    except Exception as e:
        print(f"Unexpected error: {e}")

    time.sleep(0.1)
