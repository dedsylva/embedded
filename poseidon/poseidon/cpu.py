# !/usr/bin/python3

from typing import Any, Dict, List, TypeVar, Union

BYTE = TypeVar('BYTE')

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

OPCODES = {
          0b00: 'ADD', 
          0b01: 'SUB', 
          0b10: 'MUL',
          0b11: 'DIV'
          }
FLAGS =   {
          'OVERFLOW': False, 
          'ZERO': False,
          'NEGATIVE': False
         }


class ALU:
  def __init__(self: Any, OPCODE: Dict, FLAG: Dict) -> Any:
    self.OPCODE: Dict = OPCODE
    self.FLAG: Dict = FLAG

  def ADD(self: Any, A: BYTE, B: BYTE) -> BYTE:
    return A + B

  def SUB(self: Any, A: BYTE, B: BYTE) -> BYTE:
    return A - B

  def MUL(self: Any, A: BYTE, B: BYTE) -> BYTE:
    return A * B

  def DIV(self: Any, A: BYTE, B: BYTE) -> BYTE:
    res = 0
    while A > 0:
      A -= B
      res += 1

    if A == 0:
      return res 
    else: 
      return res -1 

  def exec(self: Any, OP: str, A: BYTE, B: BYTE) -> Union[BYTE, List[str]]:
    _OPNAME: str = self.OPCODE[OP]
    _OP: Any = getattr(ALU, _OPNAME)
    res: BYTE = _OP(self, A,B)

    if res > 2 ** 8 - 1:
      self.FLAG['OVERFLOW'] = True

    if res == 0:
      self.FLAG['ZERO'] = True
    elif res < 0:
      self.FLAG['NEGATIVE'] = True
    
    return res, self.FLAG
  
  def reset(self: Any) -> None:
    self.FLAG['OVERFLOW']: bool = False
    self.FLAG['ZERO']: bool = False
    self.FLAG['NEGATIVE']: bool = False

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
class MEMORY:
  def __init__(self: Any) -> None:
    self.N: int = 16
    self.WIDTH: int = 8 # 1 Byte
    self.READ_ENABLE: bool = False
    self.WRITE_ENABLE: bool = False
    self.ADDR_INPUT: BYTE = 0b00000000
    self.DATA: BYTE = 0b00000000 # 1 bit OPCODE + 1 bit REGISTER (A,B,C,D)
    self.RAM: List[BYTE] = [0]*0xF 

  def _set_read_enable(self: Any, _value: bool) -> None:
    self.READ_ENABLE = _value

  def _set_write_enable(self: Any, _value: bool) -> None:
    self.WRITE_ENABLE = _value

  def _set_data(self: Any, _value: BYTE) -> None:
    self.DATA = _value

  def read(self: Any, addr: BYTE) -> BYTE:
    assert self.READ_ENABLE == True, f"Can't read if READ_ENABLE is not set"
    return self.RAM[addr]

  def write(self: Any, addr: BYTE) -> None:
    assert self.WRITE_ENABLE == True, f"Can't write if WRITE_ENABLE is not set"
    self.RAM[addr] = self.DATA
    return
 