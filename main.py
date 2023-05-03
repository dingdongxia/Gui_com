# This is a modified python program that can receive and send hexadecimal array data with a 500ms delay before sending and can send a specific data and can process each frame separately and can split bytes data
# You need to install the pyserial module first: pip install pyserial
# You also need to specify the serial port name and baud rate according to your device
# from global import a
import serial
import time
# import send
import binascii


import send


# A function to read data from the serial port

def split_frame(data):
    frames = []
    frame = b''
    for byte in data:
        frame += bytes([byte])
        if frame.startswith(frame_header) and frame.endswith(frame_tail):
            frames.append(frame)
            frame = b''
    return frames


def read_data():
    # Check if there is any data available
    if send.ser.in_waiting > 0:

        data = send.ser.read(send.ser.in_waiting)
        print("Received:", data)
        frames = split_frame(data)
        for frame in frames:
            process_frame(frame)


# A function to process each frame
def process_frame(frame):
    # Do something with the frame, for example, print its length
    data = frame[1:-1]
    if (frame[1] == b'~'):
        print("right")
        print(data)
    print(type(frame))
    print("Frame length:", len(frame))


# A function to send data to the serial port
def send_datatest(data):
    # Add a 500ms delay before sending
    time.sleep(0.5)
    # Convert the hexadecimal string to bytes and write it to the port
    #ser.write(bytes.fromhex(data))
    # Print the data to the console
    print("Sent:", data)


# A loop to test the functions
while True:
    # Read data from the port every second
    # read_data()
    time.sleep(1)
    # Send a specific data every 5 seconds

    send.send_data('54')
