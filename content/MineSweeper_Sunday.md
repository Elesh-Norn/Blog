Title: Minesweeper Sunday
Date: 2019-08-19
Category: Project
Tags: Python, Minesweeper, Game, arcade, tutorial
# How to code a simple Minesweeper game, on a lazy Sunday 

Recently, I had the opportunity to train and discover various algorithms to improve my Python skills but also programming skills in general.
After some weeks of training, on a lazy Sunday, I was wondering how easy it would be to code a simple minesweeper game.

I discovered the [Arcade library](http://arcade.academy/) on an [episode of Talk Python to Me](https://talkpython.fm/episodes/show/223/fun-and-easy-2d-games-with-python) where the creator, Paul Craven, was invited.
I was impressed with how simple and clear the library was (compared, in my opinion, to Tkinter which I talk about in my previous blog post [here]({filename}/Aborted_project_Magic_App.md) ).

My objective would be to keep it simple and fast to do, basic OOP programming and use the arcade library.

## How to play Minesweeper: the rules

Maybe you're not old like me and didn't spend your time on this, despite better games during your childhood. Minesweeper was a
game on Windows XP (obviously, vastly inferior to Space Cadet, which is the best game ever).
![output]({filename}/image/Minesweeper.png)

Minesweeper is played on a grid of various sizes, all grey at first, containing mines. You'd click on them and BOOM! you'd lost. Despite its
terrible theme, it is a clever puzzle game, and colored numbers would indicate you the numbers of mines in adjacent spaces. The goal of the 
game is to reveal all space without touching any mines.

## First step: The Grid
The most obvious point to start is to create the grid object. This can be easily done in Python by creating a 2D list, i.e. a list of list.

~~~~
grid = []
for y in range(8):
    row = []
    for x in range(8):
        row.append((y, x))
        grid.append(row)
print(grid)
~~~~

One thing to note is that the 0,0 is the top left corner, unlike of our usual Cartesians references where 0,0 is the bottom left.
The square left to it would be (0,1) below would be (1,0), etc... I note it y, x, but you can note it row, column if you prefer.

But maybe in my game, I will want to have different height and weight and store the grid in an object, so I will create a Grid class as such:
~~~~
class Grid:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.grid = self.create_grid(height, width)

    def create_grid(self, height, width):
        result = []
        for y in range(height):
            row = []
            for x in range(width):
                row.append(Square((y, x)))
            result.append(row)
        return result
~~~~

I have a cool grid object now, that will handily give me their height and width and the grid itself. But what is Square() in the create_grid function?

## Second step: The Square
We must model each square of the grid. To keep it simple, a square will be defined by different attributes. 
It has a position, it can contain a bomb, it can be revealed (or not) and if they're not bomb they contain a little number 
telling how much bombs are near them.

~~~~
class Square:
    def __init__(self, pos):

        self.pos = pos
        self.isbomb = False
        self.isreveal = False
        self.counter = 0
~~~~
We will construct a grid of those objects, with the earlier create_grid().

## How to make the game: 3 methods

A minesweeper, wouldn't be a minesweeper without some mines! Let's place them on the grid! 
~~~~
board = Grid(y, x)
planting_mines = 10
if planting_mines >= grid.width * grid.height:
    planting_mines = 0
	print("Invalid mines number. 0 mines have been planted.")
while planting_mines > 0:

    rand_x = random.randint(0, grid.width - 1)
    rand_y = random.randint(0, grid.height - 1)

    if board.grid[rand_y][rand_x].isbomb is False:
        board.grid[rand_y][rand_x].isbomb = True
        planting_mines += -1
~~~~

The code above takes a number of mines, and try to place them randomly on the board. When it finds a suitable Square, it set the .isbomb to True. 
It does this until all bombs are placed (if there are not too many mines)

Now that I have bombs, I can make another method, that will calculate how much bombs they have around. This will help us placing the numbers later and 
know what to reveal when the player clicks on a space. Adjacent spaces are the 8 spaces around your Square object. So, you just need to add (0,1), (-1,0) etc, 
for each direction. Of course, you should check too if they get out of the bounds of the grid. I will make it a method of the Grid class.

~~~~
def calculate_adjacent(self, square):
        count = 0
		adjacent = [(1, 0), (1, 1),(0, 1),(-1, 1),
                   (-1, 0),(-1, -1),(0, -1),(1, -1)]
        for adj in adjacent:
            visiting_height = square.pos[0] + adj[0]
            visiting_width = square.pos[1] + adj[1]
            if (
                visiting_height >= 0
                and visiting_width >= 0
                and visiting_width < self.width
                and visiting_height < self.height
            ):
                if self.grid[square.pos[0] + adj[0]][square.pos[1] + adj[1]].isbomb == True:
                    count += 1
        return count
~~~~


Very nice, let's create a function to see what it looks like (it just so you can see what it looks like, we won't use this at the end.)

~~~~
def print_game_state(board):
    for y in range(board.height):
        line = []
        for x in range(board.width):
            if board.grid[y][x].isreveal is True:
                if board.grid[y][x].isbomb is True:
                    line.append("X")
                else:
                    line.append(str(board.grid[y][x].counter))
            else:
                line.append("-")
print(line)
~~~~

It's better to put everything in a single class. You can find how it looks like on [my Github here](https://github.com/Elesh-Norn/MineSweeper_Sunday/blob/master/main/grid.py)

## Final step: click and PLAY!
The next thing to do, to play minesweeper now that we have a working board is to create a function that handles the click.

A click will be on a case, we can assume the input will be x, y:
If you click a bomb you lose
If you click an empty space it reveals that space and the number of bombs around it.

Now, remember in minesweeper, if you click an empty space that doesn’t contain a bomb or a number it would reveal all the squares around it
until next numbers. Such space in our model is a square with a counter = 0. To reveal the spaces around it, we will modify a bit the adjacent function 
by adding a [breadth first search](https://en.wikipedia.org/wiki/Breadth-first_search).

We will store the square that we need to explore in a queue. If it's a 0 I will reveal it and check adjacent cases.


We add the current item in a visited set. It's really important so you don't won't look at the same item twice.


If the adjacent cases are 0 too, I add them to the queue to be processed later. When I finish, I remove the item from the queue.
In Python, I use the [dequeu]( https://docs.python.org/2/library/collections.html#collections.deque) object since it allows me to pop the first item of a list in constant time (unlike a normal list).

Here is the code, a method of the [Grid object](https://github.com/Elesh-Norn/MineSweeper_Sunday/blob/master/main/grid.py): 

~~~~
def reveal(self, square):
      counter = 0
      visited = set()
      queue = deque()
      queue.append(square.pos)
      while queue:
          current = queue[0]
          for adj in self.adjacent:
              visit_y = current[0] + adj[0]
              visit_x = current[1] + adj[1]
              if (visit_y, visit_x) in visited:
                  continue
              visited.add((visit_y, visit_x))

              if (
                  visit_y >= 0
                  and visit_x >= 0
                  and visit_x < self.width
                  and visit_y < self.height
              ):
                  if self.grid[visit_y][visit_x].isbomb == False:
                      if self.grid[visit_y][visit_x].isreveal == False:
                          self.grid[visit_y][visit_x].isreveal = True
                          counter += 1
                      if self.grid[visit_y][visit_x].counter == 0:
                          queue.append((visit_y, visit_x))
          queue.popleft()
return counter
~~~~


## ARCADE
Now that we have all of this, we need the game part, and this is where the [arcade](http://arcade.academy/) library comes. 
It's simple of utilization and gives some templates to QuickStart your project. I used [this template](http://arcade.academy/examples/array_backed_grid.html#array-backed-grid), 
that contains already everything I want. It's a grid, it reacts to clicks and detects where I click. This is amazing. With minor adaptations, I can make it a working version of minesweeper, 
in some minutes. 

![Arcade Minesweeper]({filename}/image/Minesweeper_arcade.png)

It's still pretty rough, there is no button to reset but a command, the graphics are being drawn slowly and the game doesn't actually stop when you lose, 
but this is pretty alright for coding with your cereals, on a Sunday morning. The arcade library is really easy and fun to use and you can have a satisfying result really quick thanks to their syntax and templates to guide you.

You can find the code on my [github here](https://github.com/Elesh-Norn/MineSweeper_Sunday) if you wanna contribute to it and make it a great Minesweeper game ; )!
