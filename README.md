# DVD Corner Bounce

The bouncing DVD Logo, or DVD Screensaver, refers to the animated screensaver commonly found on American DVD players, in which the DVD Video logo bounces to different parts of the screen and changes color. Online and in pop culture, people brag and joke about seeing the logo land perfectly in the corner of the screen.

## 🤔 Challenge

**How many collisions** until it hits any corner?

<img src="https://github.com/cristianmacedo/corner-bounce/raw/master/img/GIF1.gif" width="512"/>

> GIF recorded from [bouncingdvdlogo.com](https://bouncingdvdlogo.com/)

This was the question that moved the project.

## 🔎 Research

On September 30th, 2013, software engineer Bill Green posted an explanation of the math behind the bouncing DVD logo on his blog.

We found some assumptions on his blog that helped us keep the consistency with the original animation:

- The DVD logo is smaller than the total screen area.
- The DVD logo moves with a perfectly diagonal constant speed (same absolute speed on both axes).
- It bounces off the edges of the screen perfectly.

After his research, he found some properties that may be interesting for our challenge:

- When you hit a corner, you will hit a different corner before hitting the same one again, etc.
- You can never hit 1, 3 or 4 corners, always 2 or 0.
- It’s a loop, at some point it will always repeat.

## 💡 Approach #1:

The solution seems quite simple:

**1:** With the initial position and direction, we get the next collision position
<br/>
**2:** Using this position, we calculate the next ones, recursively;
<br/>
**3:** When we hit a corner, we have the iteration count, and by definition, the remaining collisions.

<img src="https://github.com/cristianmacedo/corner-bounce/raw/master/img/GIF2.gif" width="512"/>

### ❌ Problem:

Using this approach, we need to compute every movement, effectively running a **full simulation** to get the result.
<br/>
Doesn't seem very effective, does it?

## 🔦 Approach #2:

Instead of computing every movement, we can use some basic geometry to get the next collision position:

**1:** We know that, for every direction, there are always **two possible walls** that it could collide with:

<img src="https://github.com/cristianmacedo/corner-bounce/raw/master/img/Sides.png" width="512"/>
<br/>

**2:** Using this information, we get the **distance** between the logo and each one of them:

<img src="https://github.com/cristianmacedo/corner-bounce/raw/master/img/Distances.png" width="512"/>
<br/>

**3:** Assuming that the logo always moves in a **45°** angle, we use the **smallest** distance as a parameter to calculate the next collision position by offsetting the **X** and **Y** coordinates according to the current **distance** and **direction**:

<img src="https://github.com/cristianmacedo/corner-bounce/raw/master/img/CoordsPrediction.png" width="512"/>
<br/>

**4:** We can now use the same recursive method mentioned before to calculate the remaining collisions, but of course, way faster:

<img src="https://github.com/cristianmacedo/corner-bounce/raw/master/img/Faster.gif" width="512"/>
<br/>

**✅ That's it!** Using this approach, we can predict how many times the logo will collide before hitting a corner, without computing a full simulation of the logo's movement.

## 🧑‍💻 Implementation

We used the **Python** programming language to implement the solution along with the [PyGame](https://www.pygame.org/) library to draw the animation.

The [Bouncer](/classes/Bouncer.py) class is the main class that handles the logic of the bouncing logo. It includes all positional and speed properties, all needed methods to draw, update the position according to the current speed, check collision conditions and calculate the next collision position, as well as how many collisions are left until the next corner hit.

## 🚀 Executing

To run the project, execute the following command at the root directory:

```
python game.py
```
