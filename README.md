# Bear-problem


# Description
A group of four (4) researchers are being chased by hungry polar bears around the North Pole late at night. They come to a rope bridge over a ravine. If they can all get over the bridge before the hungry polar bears arrive, they will survive.
At most two people can cross at a time. A person or pair of people can only cross when they have a flashlight with them. The group has only a single flashlight among them, so one person must bring the flashlight back across the bridge to the starting side before anyone else can cross.

Each person moves at a different pace:

- Person A can cross the bridge in 1.5 minute
- Person B can cross the bridge in 3 minutes 
- Person C can cross the bridge in 7.5 minutes
- Person D can cross the bridge in 10 minutes

Each pair moves at the pace of its slowest member; i.e., Person A and Person B will take 10 minutes to cross if they go together. The problem is how can the whole group get to the other side of the bridge in the shortest possible time?

The program is trying to find the solution with the least cost or time it takes to have every person reach the other side of the bridge.


Representation: A, B, C, D, F ∈ {S,E}, s = (A, B, C, D, E)
First four item of a node represent the four characters in the order given above and the last
item represents the flashlight.

s start = (S,S,S,S,S) means everyone including the flashlight is on the starting side

s goal = (E,E,E,E,E) everyone has cross the bridge and the flashlight is on the end of the bridge




