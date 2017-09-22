# `guard.py`

hitting the badguy with laser. I don't remember the exact question now while i'm writing the descriptiong for my answer. It was an AI related problem where a bad and good guy in a rectangle shape room and walls are made of mirror. Good guy is with a laser gun and the probl em is to find number of ways good guy can hit bad guy when laser gun can travel limited distance.

my answer: I mirrored the plane for a specific count. because The distance of the hit below

```
     _______________
    |      /\       |
    |     /  \      |
    |    *    *     |
    |               |
     _______________
```

is equal to to this


```
     _______________
    |  --mirrored-- |
    |         *     |
    |        /      |
     _______/_______
    |      /\       |
    |     /  \      |
    |    *    *     |
    |  --original-- |
     _______________
```

for more clear view check `/p5/index.html` which is having p5js sketch for this problem. The p5js is messy since I wrote in such a way that I could dynamically create mirrored coordinates in chrome console.

After this, I observed that the mirrored coordinates are symmetric and forms a palindromic pattern. This pattern isn't same vertically and horizontally since the width and height of room is not equal.

I could generate that pattern easily.

And the next step was generating matrix out of that pattern, in the sense generating all points where good guy can hit.

after this my only job left is to make good guy hit bad guy without hitting himself. To make it possible I used arc tan 2 function since it gives different values for 4 different quadrants of graph. And I iterated through points in matrix in spiral manner, from the center of matrix to the sides spirally like a snake, since distance can only be measured from the centre and goodguy is at the centre.

and that's all I recorded all previously accessed points using math.atan2 in a set. and avoided hitting goodguy by recording goodguy's location before badguy's location.

# License

GNU GPLv3