### relative package 2 ###

#./game/__init__.py
#./game/sound/__init__.py
#./game/sound/echo.py
#./game/graphic/__init__.py
#./game/graphic/render.py
#./game/graphic/relative.py

from ..sound.echo import echo_test

def render_test2():
	print("render2")
	echo_test()

# python3 relative.py 처럼 직접 실행시키면 error : cannot perform relative import
# 다른 파일에서 이 파일을 import한 경우 사용가능
