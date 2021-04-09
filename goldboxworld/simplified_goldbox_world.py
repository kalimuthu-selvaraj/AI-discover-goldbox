from typing import Tuple

from .discrete_space import DiscreteSpace


class SimplifiedGoldboxWorld:
    """
    Worlds are described by a grid like the following
        0000000000
        00000000M0
        000M000000
        0000000M00
        0M00000000
        000M000000
        0000000000
        0000000000
        000000M000
        00M000000G
    The starting point is always at (0, 0)
    0: empty tile
    m: metal detector
    G: gold box, the agent is successful if it reaches here
    """

    def __init__(self):
        self.board = self.board = [
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', 'M', '0'],
            ['0', '0', '0', 'M', '0', '0', '0', 'M', '0', '0'],
            ['0', 'M', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', 'M', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', 'M', '0', '0'],
            ['0', '0', 'M', '0', '0', '0', '0', '0', '0', 'G']
        ]
        self.agentX = 0
        self.agentY = 0

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
            self.agentY = min(3, self.agentY + 1)
        elif action == 1:
            self.agentY = max(0, self.agentY - 1)
        elif action == 2:
            self.agentX = max(0, self.agentX - 1)
        else:
            self.agentX = min(3, self.agentX + 1)

        if self.board[self.agentY][self.agentX] in ('M'):
            return (self.state, -100, True)
        elif self.board[self.agentY][self.agentX] == 'G':
            return (self.state, 10000, True)
        else:
            return (self.state, -1, False)

    def reset(self) -> int:
        self.agentX = 0
        self.agentY = 0
        return self.state
