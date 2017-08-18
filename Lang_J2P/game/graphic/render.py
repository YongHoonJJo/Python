def render_test():
	print("render")

#./game/__init__.py
#./game/sound/__init__.py
#./game/sound/echo.py
#./game/graphic/__init__.py
#./game/graphic/render.py

### relative package ###

# graphic 디렉터리의 render.py 모듈이 
# sound 디렉터리의 echo.py 모듈을 사용하고 싶다면

import sys
sys.path.append("/Users/starctak/Python/repository/Lang_J2P/")

# 환경변수 설정후 가능..
from game.sound.echo import echo_test

def render_echo_test():
	echo_test()

render_echo_test() # "echo"

