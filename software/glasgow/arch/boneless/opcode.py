OPCODE_LOGIC   = 0b0000_0
OPTYPE_AND     = 0b00
OPTYPE_OR      = 0b01
OPTYPE_XOR     = 0b10

OPCODE_ARITH   = 0b0000_1
OPTYPE_ADD     = 0b00
OPTYPE_SUB     = 0b01
OPTYPE_CMP     = 0b10

OPCODE_SHIFT_L = 0b0001_0
OPTYPE_SLL     = 0b0
OPTYPE_ROT     = 0b1

OPCODE_SHIFT_R = 0b0001_1
OPTYPE_SRL     = 0b0
OPTYPE_SRR     = 0b1

OPCODE_LD      = 0b001_00
OPCODE_ST      = 0b001_01
OPCODE_LDX     = 0b001_10
OPCODE_STX     = 0b001_11

OPCODE_ADDI    = 0b01_000
OPCODE_MOVA    = 0b01_001
OPCODE_MOVL    = 0b01_010
OPCODE_MOVH    = 0b01_011
OPCODE_LDI     = 0b01_100
OPCODE_STI     = 0b01_101
OPCODE_JAL     = 0b01_110
OPCODE_JR      = 0b01_111

OPCODE_J       = 0b1_000_0
OPCODE_JNZ     = 0b1_001_0
OPCODE_JNE     = OPCODE_JNZ
OPCODE_JZ      = 0b1_001_1
OPCODE_JE      = OPCODE_JZ
OPCODE_JNS     = 0b1_010_0
OPCODE_JS      = 0b1_010_1
OPCODE_JNO     = 0b1_011_0
OPCODE_JO      = 0b1_011_1
OPCODE_JNC     = 0b1_100_0
OPCODE_JUGE    = OPCODE_JNC
OPCODE_JC      = 0b1_100_1
OPCODE_JULT    = OPCODE_JC
OPCODE_JUGT    = 0b1_101_0
OPCODE_JULE    = 0b1_101_1
OPCODE_JSGE    = 0b1_110_0
OPCODE_JSLT    = 0b1_110_1
OPCODE_JSGT    = 0b1_111_0
OPCODE_JSLE    = 0b1_111_1