### OBJECTS AND CLASSES IN PICTURES
![generative art](../imgs/genart.gif)
* When we use **turtle.Pen()** the turtle module uses the Pen class. 
```python
import turtle
donatello = turtle.Pen()
rafael = turtle.Pen()
```
* Now that the objects are created, they become powerful… we can call functions on each and they will move independently (without effecting any of the others)!
```python
donatello.forward(50)
donatello.right(90)
donatello.forward(20)
rafael.left(90)
rafael.forward(100)
```
* Every time we call **turtle.Pen()**, we create a new independent **object**. Since they area all objects of the **Pen** class, we can use the same functions on each **object**… but because they are objects we can move each independently. 
* What happens when we create an object with the same variable name as the one we have already used?

### USING THE TURTLE MODULE
* Before we can use the turtle module we need to import the module. Then we must create an instance of the Pen class.
```python
import turtle
donatello = turtle.Pen()
```
* If we run this as is...we will see that as soon as we call the instance, a canvas is automatically created. The triangle in the window is the turtle. (The triangle points the direction the turtle is facing).
![turtle](../imgs/turtle.png)

### MOVING THE TURTLE:
* By calling these functions, the turtle can be moved around the screen. Just as we learned last week we call the functions of the class by using the dot after the instance name and then calling the function.
```python
donatello.forward(50)
```
* The above function tells the turtle to move forward 50 pixels. A pixel is a single point on the screen – the smallest element that can be represented. (The same as computer monitors and TV Screens... if you zoom in enough you will see the image is made out of dots).
![pixel](../imgs/pixelpika.gif)
* We can change the direction of the turtle by using the left (or right) function to rotate the turtle by the amount of degrees specified.
```python
donatello.left(90)
```
* In this case the turtle rotates 90 degrees to the left. If you are confused about degrees reference the below diagram:
![rotation](../imgs/rotate.png)
When you call left(90) it is the same as calling right(270)
* To erase the canvas, we use the reset function. This will clear the canvas and puts the turtle back at its starting position.
```python
donatello.reset()
```
* You can also use the clear function to erase the canvas. This function does not move the turtle back to its starting point.
```python
donatello.clear()
```

### DRAWING SHAPES
![square](../imgs/square.png)
* If you repeat the code below additional times, it will draw a square:
```python
donatello.forward(50)
donatello.left(90)
```
* You can do this simpler by using a for loop. We will use reset first to make sure we start at the beginning.
```python
donatello.reset()
for x in range(1,5):
    donatello.forward(50)
    donatello.left(90)
```
* If we change parameters in the loop, we can create shapes different from a square.
```python
donatello.reset()
for x in range(1,5):
    donatello.forward(20)
    donatello.left(94)
```
* If we increase the range, the star will have more points. If we increase the number the turtle moves forward, we will increase the length of the star tips. The angle, which we rotate, makes the point skinnier or fatter. The above code looks like this:
![nonsquare](../imgs/nonsquare.png)
* If we use a function, we can customize the size of the shapes. Here is an example using a square.
```python
def mySquare(size):
    t.reset()
    for x in range(1,5):
        t.forward(size)
        t.left(90)
```
* In this case we use the parameter of our function (size) to change the length in which the turtle draws each side.
![size](../imgs/size.png)
* We can use an if statement to control how the turtle will turn and draw another variation.
```python
donatello.reset()
for x in range(1, 19):
    donatello.forward(100)
    if x % 2 == 0:
        donatello.left(175)
    else:
        donatello.left(225)
```
* In this example, we use the expression x % 2 == 0 (or if x mod 2 is equal to 0) to tell us which way the turtle will rotate (left or right). Essentially, the modulo operator (%) finds the remainder of x when divided by 2.
![star](../imgs/star.png)

#### Some other functions of pen allow us to do different things for example...
    * The up() function picks up the “pen”, so to speak, and allows us to move the turtle without drawing a line.
```python
donatello.up()
```
    * The down() function puts the “pen” down and allows the turtle to draw when it is moved.
```python
donatello.down()
```
    * circle(size) allows us to draw a circle of a particular size.
```python
donatello.circle(50)
```
    * setheading(headingAngle) turns the turtle to face a particular direction.
```python
donatello.setHeading(90)
```
    * begin_fill() and end_fill() are used to fill in an area of the canvas 
```python
donatello.begin_fill()
donatello.circle(50)
donatello.end_fill()
```  
    * color() is used to change the color of the pen.
```python
donatello.color(1, 1, 1)
```  
### COLORING THINGS IN
* The color function takes three parameters. The first specifies the amount of red, the second the amount of green, and the last the amount of blue. This recipe used to call colors is “RGB”
```python
.color(red, green, blue)
```  
* To get a bright red we use the following code:
```python
donatello.color(1, 0, 0)
```  
* With a 1 in the red parameter, we are telling Python to put 100% red. The 0’s in the green and blue parameters tell Python to use no green and blue.
![rgb](../imgs/rgb.png)
* Red, Green & Blue are primary colors for light. We can’t create them by mixing other colors, but we can create other colors like yellow by mixing them. Here is an example of mixing 100% of red and 100% of green to create a yellow:
```python
donatello.color(1, 1, 0)
``` 
* If we want to use the color black, we would represent this with an absence of any color in the 3 parameters. It would look like this:
```python
donatello.color(0, 0, 0)
``` 
* If we wanted white we add 100% of all colors. This would look like this:
```python
donatello.color(1, 1, 1)
``` 
### CIRCLES
* To create a circle using code we use the following code:
```python
donatello.circle(50)
```  
* To draw a filled circle, first we need to set the color:
```python
donatello.color(1, 1, 0)
```  
* In this case we set the color to be yellow. Now that the color is set, we must tell Python that we want to fill in the area of the canvas that we are drawing on with that color. We do so by using the begin_fill() function, and then drawing the circle by calling the circle function.
```python
donatello.color(1, 1, 0)
donatello.begin_fill()
donatello.circle(50)
donatello.end_fill()
```  
* Finally, we tell Python that we are don filling in the canvas by using the end_fill() function.
* If we make a function, we can easily draw filled circles using one command. Here is an
example of a function we would use:
```python
def myCircle(red, green, blue):
    t.color(red, green, blue)
    t.begin_fill()
    t.circle(50)
    t.end_fill()
```  
* Similar to how we made a function for drawing a circle we can do the same for squares. To supply us with more options, lets add a parameter to tell Python if we want the square to be filled or not.
• By using the if statement, if filled is true we will call the function begin_fill() and if it isn’t we will not. We will also do the same for the end_fill() function. This will allow us the flexibility to draw many different types of squares.
```python
def mySquare(size, filled):
    if filled == True:
        t.begin_fill()
    for x in range(1,5):
        t.forward(size)
        t.left(90)
    if filled == True:
        t.end_fill()
```
* We can also follow this logic when creating a function for drawing a star. See the below example:
```python
def myStar(size, filled):
    if filled == True:
        t.begin_fill()
    for x in range(1, 19):
        t.forward(100)
        if x % 2 == 0:
            t.left(175)
        else:
            t.left(225)
    if filled == True:
        t.end_fill()
```

* loading/formating
* background/sprite
* Key Binding methods
* **In-class Exercises/Challenges**: 
    * Using the turtle class create a generative/fractal design
    * Create a class that provides methods for drawing the following shapes: Square, Circle, Octagon, Pentagon.
    * Modify the shapes class to allow for the options of changing the fill color, border, size, etc.
    * Create a class to build a Maze.Using the turtle class create a generative/fractal design
    * Create a class that provides methods for drawing the following shapes: Square, Circle, Octagon, Pentagon.
    * Modify the shapes class to allow for the options of changing the fill color, border, size, etc.
    * Create a class to build a Maze.
    * Create a “Player” class that allows a user to navigate the maze created last week.
    * Create a “Player” class that controls a spaceship on the screen. (beginning of alternative version of space invaders)
    * Use Player class to create a 2 player game that controls 2 different spaceships on the screen.
    * Limit the players movement to the viewable screen size/maze boundaries.
* **Vocabulary**: child, parent 
* **Keywords**: 