
## 🤔 Challenge

**How many collisions** until it hits any corner?

<img src="https://github.com/cristianmacedo/corner-bounce/raw/master/img/GIF1.gif" width="512"/>

> GIF from bouncingdvdlogo.com

This was the question that moved the project.
## 💡 Approach
The solution seems quite simple:
<br>
**1:** With the initial position and direction, we get the next collision position;
<br>
**2:** Using this position, we calculate the next ones, recursively;
<br>
**3:** When we hit a corner, we have the iteration count, and by definition, the remaining collisions.

<img src="https://github.com/cristianmacedo/corner-bounce/raw/master/img/GIF2.gif" width="512"/>

**❌ Problem:**

Using this approach, we need to compute every movement, effectively running a **full simulation** to get the result.
<br>
Doesn't seem very effective, does it?
## 🔦 Approach #2:
Instead of computing every movement, we can use some basic geometry to get the next collision position:
<br>
<br>
**1:** We know that, for every direction, there are always **two possible walls** that it could collide:
<br>
<img src="https://github.com/cristianmacedo/corner-bounce/raw/master/img/Sides.png" width="512"/>
<br>
<br>
**2:** Using this information, we get the **distance** between the logo and each one of them:
<br>
<img src="https://github.com/cristianmacedo/corner-bounce/raw/master/img/Distances.png" width="512"/>
<br>
<br>
**3:** Assuming that the logo always moves in a **45°** angle, we use the **smallest** distance as a parameter to calculate the next collision position by offsetting the **X** and **Y** coordinates according to the current **distance** and **direction**:
<br>
<img src="https://github.com/cristianmacedo/corner-bounce/raw/master/img/CoordsPrediction.png" width="512"/>
<br>
<br>
**4:** We can now use the same recursive method mentioned before to calculate the remaining collisions, but of course, way faster.

**✅ That's it!** Using this approach, we can predict how many times the logo will collide before hitting a corner, without computing a full simulation of the logo's movement.
## 🚀 Executing
To run the project, execute the following command at the root directory:
```
python game.py
```
