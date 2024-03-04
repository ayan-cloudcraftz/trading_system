def makeUrl1(paramList:list, baseUrl:str, endpoint:str):
    params = "&".join(paramList)
    request_url = "".join([baseUrl + endpoint, "?", params])
    return request_url

def makeUrl2(baseUrl:str, endpoint:str, id:str):
    return "".join([baseUrl, endpoint, id])