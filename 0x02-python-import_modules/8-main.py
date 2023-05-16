#!/usr/bin/python3
from dis import dis

print_byte_code = __import__('102-magic_calculation').magic_calculation

dis(print_byte_code)
