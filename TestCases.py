from gameoflife import GameOfLife




##Blinker pattern
gameblinker=GameOfLife(6,6)
gameblinker.seeds([(0,1),(1,1),(2,1)])

input=raw_input('press enter to display next cycle, press q to exit! :')


while input!='q':
    gameblinker.nextGenCheck()
    input=raw_input('press enter to display next cycle, press q to exit! :')




##block pattern
gameblock=GameOfLife(6,6)
gameblock.seeds([(0,0),(0,1),(1,0),(1,1)])

input=raw_input('press enter to display next cycle, press q to exit! :')


while input!='q':
    gameblock.nextGenCheck()
    input=raw_input('press enter to display next cycle, press q to exit! :')


##toadPattern

gametoad=GameOfLife(6,6)
gametoad.seeds([(0,1),(0,2),(0,3),(1,0),(1,1),(1,2)])

input=raw_input('press enter to display next cycle, press q to exit! :')


while input!='q':
    gametoad.nextGenCheck()
    input=raw_input('press enter to display next cycle, press q to exit! :')



##boatPattern


gameboat=GameOfLife(6,6)
gameboat.seeds([(0,0),(0,1),(1,0),(1,2),(2,1)])
print 'For Boat pattern'
input=raw_input('press enter to display next cycle, press q to exit! :')
while input!='q':
    gameboat.nextGenCheck()
    input=raw_input('press enter to display next cycle, press q to exit! :')
