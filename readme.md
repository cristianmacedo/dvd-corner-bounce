
## 🤔 Challenge

**How many collisions** until it hits any corner?

(GIF)

This was the question that moved the project.
## 💡 Approach
The solution seems quite simple:
**1:** With the initial position and direction, we get the next collision position;
**2:** Using this position, we calculate the next one, and so on;
**3:** When we hit a corner, we have the iteration count, and by definition, the remaining collisions.

(GIF)

**❌ Problem:**

Using this approach, we need to compute every movement, effectively running a **full simulation** to get the result.
Doesn't seem very effective, does it?
## 🔦 Approach #2:
Instead of computing every movement, we can use some basic geometry to get the next collision position:
**1:** We know that, for every direction, there are always **two possible walls** that it could collide:

(IMG)

**2:** Using this information, we get the **distance** between the logo and each one of them:

(IMG)

**3:** Assuming that the logo always moves in a **45°** angle, we use the **smallest** distance as a parameter to calculate the next collision position by offsetting the **X** and **Y** coordinates according to the current **distance** and **direction**:

(IMG)

That's it! Using this approach, we get the next collision position, without computing a full simulation of the logo's movement.
## 🚀 Executing
To run the project, execute the following command at the root directory:
```
python game.py
```