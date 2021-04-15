# AI-discover-goldbox

## Setup

Use online python notebook editor run this assignment
https://jupyter.org/try (jupyter lab)

VS code setup
https://code.visualstudio.com/docs/python/python-tutorial

## Problem Statement

<img src="https://github.com/kalimuthu-selvaraj/AIGoldboxDetector/blob/main/images/environment.png" width="500" height="500">

Implement the Learning Agent which is in search of the only gold box in
the given static environment equipped with the metal detectors . The metal detectors
are capable of sensing the metal in their own and all surrounding cells in their circumference.
While the agent initial battery is at 10000 points. Each movement of the agent reduces the
battery by 1 point and at a time the agent can move only one cell either of the forward,
backward, left or right directions. If the agent moves in to metal detector sensing range, the
agent’s battery life will reduce by 100 battery points. The ultimate goal is to catch the gold
box and it results 10000 additional battery points. The agent can sense only its battery points,
which are automatically updated on each movement and the resultant cell contents

<img src="https://github.com/kalimuthu-selvaraj/AIGoldboxDetector/blob/main/images/detected_goldbox.gif" width="500" height="500">

Credits: https://github.com/MagicTurtle2203/QLearningWumpusWorld
