import struct
import datetime

hex_data = "d2e350a2a2dcd601"
bytes_data = bytes.fromhex(hex_data)
unpacked_data = struct.unpack("<Q", bytes_data)[0]

epoch = datetime.datetime(1601, 1, 1)
shutdown_time = epoch + datetime.timedelta(microseconds=unpacked_data / 10)
formatted_shutdown_time = shutdown_time.strftime("%Y-%m-%d %H:%M:%S")

print(formatted_shutdown_time)
