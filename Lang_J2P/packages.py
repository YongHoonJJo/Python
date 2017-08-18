### Execute function in package ###

#./game/__init__.py
#./game/sound/__init__.py
#./game/sound/echo.py
#./game/graphic/__init__.py
#./game/graphic/render.py

import game.sound.echo
game.sound.echo.echo_test() # "echo"

from game.sound import echo
echo.echo_test() # "echo"

from game.sound.echo import echo_test
echo_test() # "echo"

import game
# game.sound.echo.echo_test() : (x)
# 'module' object has no attribute 'sound'

# when you declare "import game",
# You can refer to the module in the directory of game
# and something defined by __init__.py

# import game.sound.echo.echo_test : (x)
# when you declare import.a.b.c, 
# c must be module or package.!!

from game.graphic.relative import render_test2 

render_test2()
# render2
# echo
