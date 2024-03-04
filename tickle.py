from lib.globals.constants import *
from lib.utils.service import *

def tickle():
    data = get(url=BASE_URL+TICKLE)
    print(data)

# tickle()