from typing import Tuple

from .discrete_space import DiscreteSpace


class GoldboxDetector:
    """
    Environments are described by a grid like the following
        0 0 0 0 0 0 0 S S S
        0 0 S S S 0 0 S M S
        0 0 S M S 0 S S S S
        0 0 S S S 0 S M S 0
        0 0 S M S 0 S S S 0
        0 0 S S S 0 0 0 0 0
        0 0 0 0 0 0 0 0 0 0
        0 0 0 0 0 0 S S S 0
        0 S S S 0 0 S M S 0
        0 S M S 0 0 S S S G
    The starting point is always at (0, 9)
    0: empty tile
    M: metal detector
    S: sensing range
    G: gold box, the agent is successful if it reaches here
    """

    def __init__(self):
        self.board = [
            ['0', '0', '0', '0', '0', '0', '0', 'S', 'S', 'S'],
            ['0', '0', 'S', 'S', 'S', '0', '0', 'S', 'M', 'S'],
            ['0', '0', 'S', 'M', 'S', '0', 'S', 'S', 'S', 'S'],
            ['S', 'S', 'S', 'S', 'S', '0', 'S', 'M', 'S', '0'],
            ['S', 'M', 'S', 'S', 'S', '0', 'S', 'S', 'S', '0'],
            ['S', 'S', 'S', 'M', 'S', '0', '0', '0', '0', '0'],
            ['0', '0', 'S', 'S', 'S', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', 'S', 'S', 'S', '0'],
            ['0', 'S', 'S', 'S', '0', '0', 'S', 'M', 'S', '0'],
            ['0', 'S', 'M', 'S', '0', '0', 'S', 'S', 'S', 'G']
        ]
        self.agentX = 9
        self.agentY = 0
        self.initialBattery = 10000
        self.totalBatteryPoint = 0

        self.num_actions = 4    # up, down, left, right
        self.num_spaces = 100    # one for each tile
        self.action_space = DiscreteSpace(self.num_actions)
        self.observation_space = DiscreteSpace(self.num_spaces)

    @property
    def state(self) -> int:
        return self.agentY * 10 + self.agentX

    def step(self, action: int) -> Tuple[int, int, bool]:
        """
        Returns a tuple in the format of (new state, reward, done)
        given an int, action, where 0 <= action < 4
        """
        assert 0 <= action < self.num_actions, "Action must be an integer between 0 and 3"
        if action == 0:
            self.agentY = min(9, self.agentY + 1)
        elif action == 1:
            self.agentY = max(0, self.agentY - 1)
        elif action == 2:
            self.agentX = max(0, self.agentX - 1)
        else:
            self.agentX = min(9, self.agentX + 1)

        if self.board[self.agentX][self.agentY] in ('M', 'S'):
            self.initialBattery = (self.initialBattery - 100) - 1
            if(self.initialBattery < 101):
                return (self.state, 0, True)
            else:
                return (self.state, -101, False)
        elif self.board[self.agentX][self.agentY] == 'G':
            self.totalBatteryPoint = (self.initialBattery + 10000) - 1
            print("Goal Reached!!!, total battery points is: ",
                  self.totalBatteryPoint)

            return (self.state, 10000-1, True)
        else:
            self.initialBattery = self.initialBattery - 1
            return (self.state, -1, False)

    def reset(self) -> int:
        self.agentX = 9
        self.agentY = 0
        self.initialBattery = 10000
        return self.state
