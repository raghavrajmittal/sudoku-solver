# A Sudoku Solver in Python!

## Requirements
A computer, python, tkinter


## Running the code
To start, simply run:
```
python gui.py
```

Then click on any cell to enter your starting numbers, and then click on the 'solve' button!



## Behind the scenes
My first goal was to just create a python script that could solve any sudoku given to it. Although I've seen sudoku solver's completely, it was still pretty fun to code out. My algorithm was intuitive - start at the first empty cell, fill it with the first number that fits, move on to the next cell and repeat the process. If, at some point, none of the numbers fit, then undo the last number you filled, and instead fill in the next number that might fit and keep doing this until all cells are filled, or you're back at the first cell with no other number you can possibly fill.

This worked! It's like depth first search, but in a brute-force kind of way. It's not naive brute-force as we're avoiding a lot of invalid solutions by early rejection of certain entries. Turns out that the method I coded out has a very specific name - constraint propogation and backtracking!

So now the solver worked, but it was kinda painful creating the input grid in the backend. So why not use Tkinter to make a cute python GUI? I had never used tkinter before, so getting set up took a bit of time. At this point, I found Newcoder.io's tutorial on creating a GUI in Python! And guess that they were building in the tutorial? A GUI for sudoku! So then I made some UI and functional changes to their tutorial code, connected my own solver, and now it's ready!


## Acknowledgements
- How to get set up taken from [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- Tkinter code taken from Newcoder.io's [Introduction to GUI - Tutorial](http://newcoder.io/gui/part-3/)
