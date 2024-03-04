from lib.utils.makeUrl import makeUrl
from lib.utils.service import post
from lib.globals.constants import *

def orderReply(replyId:str):
    url = makeUrl(baseUrl=BASE_URL, endpoint=ODR_REPLY, id=replyId)
    body = {
        "confirmed": True
    }

    reply_res = post(url=url, body=body)

    print(reply_res)