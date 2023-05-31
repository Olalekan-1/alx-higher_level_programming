#!/usr/bin/python3
import dis
import square



code_obj = square.Square.__code__

bytecode = dis.ByteCode(code_obj)

for instruction in bytecode:
    print(instruction)
