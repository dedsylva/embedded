# POSEIDON - A simple 8-Bit CPU Implementation

# Introduction
This is a simple implementation of what a CPU would be. Based on [Computer Science Crash Course Series](https://www.youtube.com/watch?v=FZGugFqdr60&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo&index=8&ab_channel=CrashCourse), which is inspired by the [Intel 4004](https://en.wikipedia.org/wiki/Intel_4004)

## General Configurations
- We have:
  - 8-Bit RAM
  - 8-Bit ALU 
  - 4 General-Purpose 8-Bit Registers
  - 16 Instructions

- We don't have:
  - Cache
  - Pipes
  - Fancy stuff

### RAM
```python
"""
16 Bytes RAM Implementation
-------------------
| ADDR |   DATA   |
| 0x0  | 00000000 |
| 0x1  | 00000000 |
| 0x2  | 00000000 |
| 0x3  | 00000000 |
| 0x4  | 00000000 |
| 0x5  | 00000000 |
| 0x6  | 00000000 |
| 0x7  | 00000000 |
| 0x8  | 00000000 |
| 0x9  | 00000000 |
| 0xA  | 00000000 |
| 0xB  | 00000000 |
| 0xC  | 00000000 |
| 0xD  | 00000000 |
| 0xE  | 00000000 |
| 0xF  | 00000000 |
-------------------
"""
```

### ALU
```python
"""
8-Bit ALU Implementation
INPUTS:  8Bit A, 8Bit B, 2Bit OPCODE
OUTPUTS: 8Bit Answer C, FLAGS
OPCODES:
         ADD:  00
         SUB:  01
         MUL:  10
         DIV:  11
FLAGS:   
         OVERFLOW
         ZERO
         NEGATIVE
"""
```

### Instructions
```python
"""
8 BIT INSTRUCTIONS 
  - FIRST 4 BITS IS THE INSTRUCTION CODE
  - LAST  4 BITS IS THE REGISTER (A,B,C,D)
"""
```
