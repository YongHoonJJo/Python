### Usage of all ###

#./game/__init__.py
#./game/sound/__init__.py
#./game/sound/echo.py
#./game/graphic/__init__.py
#./game/graphic/render.py

from game.sound import *

# echo.echo_test() : (x)
# error : name 'echo' is not defined

# 특정 디렉터리의 모듈을 *를 이용하여 import할 때에는 
# 다음과 같이 해당 디렉터리의 __init__.py 파일에 
# __all__이라는 변수를 설정하고 
# import할 수 있는 모듈을 정의해 주어야 한다.

# __all__  = ['echo']

# 여기서 __all__이 의미하는 것은 
# sound 디렉터리에서 * 기호를 이용하여 import할 경우 
# 이곳에 정의된 echo 모듈만 import된다는 의미이다.

# 설정 후
echo.echo_test() # "echo"

# from a.b.c import * 에서 
# c가 모듈인경우 __all__ 과 상관없이 무조건 import 된다.


