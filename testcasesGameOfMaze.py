from gameofmaze import GameOfMaze

game=GameOfMaze(6,6)
game.seeds([(3,1),(3,2),(3,3),(3,4),(4,4),(4,1)],[(5,1),(5,5)])

game.getNeighbours((5,1))
