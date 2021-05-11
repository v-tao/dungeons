from enum import IntEnum
class Actions(IntEnum):
    DISPLAY_MAZE=0
    CHECK_STATUS=1
    CHECK_INVENTORY=2
    MOVE_NORTH=3
    MOVE_EAST=4
    MOVE_SOUTH=5
    MOVE_WEST=6
    GO_BACK=0
    USE_ITEM=1
    DISCARD_ITEM=2
