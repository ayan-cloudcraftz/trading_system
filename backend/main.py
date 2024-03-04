from fastapi import FastAPI

app = FastAPI()


@app.get("/search")
async def root():
    return [
        {
            "conid": 0,
            "companyHeader": "string",
            "companyName": "string",
            "symbol": "string",
            "description": "string",
            "restricted": "string",
            "fop": "string",
            "opt": "string",
            "war": "string",
            "sections": [
            {
                "secType": "string",
                "months": "string",
                "symbol": "string",
                "exchange": "string",
                "legSecType": "string"
            }
            ]
        }
    ]

@app.get("/info")
async def root():
    return [
        {
            "conid": 0,
            "symbol": "string",
            "secType": "string",
            "exchange": "string",
            "listingExchange": "string",
            "right": "string",
            "strike": 0,
            "currency": "string",
            "cusip": "string",
            "coupon": "string",
            "desc1": "string",
            "desc2": "string",
            "maturityDate": 0,
            "multiplier": "string",
            "tradingClass": "string",
            "validExchanges": "string"
        }
    ]

@app.get("/strikes")
async def root():
    return {
        "call": [
            [
            "5",
            "10",
            "20"
            ]
        ],
        "put": [
            [
            "5",
            "10",
            "20"
            ]
        ]
    }

@app.get("/marketData")
async def root():
    return [
        {
            "31": "string",
            "55": "string",
            "58": "string",
            "70": "string",
            "71": "string",
            "73": "string",
            "74": "string",
            "75": "string",
            "76": "string",
            "77": "string",
            "78": "string",
            "79": "string",
            "80": "string",
            "82": "string",
            "83": "string",
            "84": "string",
            "85": "string",
            "86": "string",
            "87": "string",
            "88": "string",
            "6004": "string",
            "6008": 0,
            "6070": "string",
            "6072": "string",
            "6073": "string",
            "6119": "string",
            "6457": 0,
            "6508": "string",
            "6509": "string",
            "7051": "string",
            "7057": "string",
            "7058": "string",
            "7059": "string",
            "7068": "string",
            "7084": "string",
            "7085": "string",
            "7086": "string",
            "7087": "string",
            "7088": "string",
            "7089": "string",
            "7094": "string",
            "7184": "string",
            "7219": "string",
            "7220": "string",
            "7221": "string",
            "7280": "string",
            "7281": "string",
            "7282": "string",
            "7283": "string",
            "7284": "string",
            "7285": "string",
            "7286": "string",
            "7287": "string",
            "7288": "string",
            "7289": "string",
            "7290": "string",
            "7291": "string",
            "7292": "string",
            "7293": "string",
            "7294": "string",
            "7295": "string",
            "7296": "string",
            "7308": "string",
            "7309": "string",
            "7310": "string",
            "7311": "string",
            "7607": "string",
            "7633": "string",
            "7635": "string",
            "7636": "string",
            "7637": "string",
            "7638": "string",
            "7639": "string",
            "7644": "string",
            "7655": "string",
            "7671": "string",
            "7672": "string",
            "7674": "string",
            "7675": "string",
            "7676": "string",
            "7677": "string",
            "7678": "string",
            "7679": "string",
            "7680": "string",
            "7681": "string",
            "7682": "string",
            "7683": "string",
            "7684": "string",
            "7685": "string",
            "7686": "string",
            "7687": "string",
            "7688": "string",
            "7689": "string",
            "7690": "string",
            "7694": "string",
            "7695": "string",
            "7696": "string",
            "7697": "string",
            "7698": "string",
            "7699": "string",
            "7700": "string",
            "7702": "string",
            "7703": "string",
            "7704": "string",
            "7705": "string",
            "7706": "string",
            "7707": "string",
            "7708": "string",
            "7714": "string",
            "7715": "string",
            "7718": "string",
            "7720": "string",
            "7741": "string",
            "7762": "string",
            "7768": "string",
            "7920": "string",
            "7921": "string",
            "server_id": "string",
            "conid": 0,
            "_updated": 0,
            "87_raw (deprecated)": "string"
        }
    ]


@app.get("/order")
async def root():
    return {
        "orders": [
            {
                "acctId": "string",
                "conid": 0,
                "conidex": "conidex = 265598",
                "secType": "secType = 265598:STK",
                "cOID": "string",
                "parentId": "string",
                "orderType": "string",
                "listingExchange": "string",
                "isSingleGroup": True,
                "outsideRTH": True,
                "price": 0,
                "auxPrice": "string",
                "side": "string",
                "ticker": "string",
                "tif": "string",
                "trailingAmt": 0,
                "trailingType": "amt",
                "referrer": "QuickTrade",
                "quantity": 0,
                "cashQty": 0,
                "fxQty": 0,
                "useAdaptive": True,
                "isCcyConv": True,
                "allocationMethod": "string",
                "strategy": "string",
                "strategyParameters": {}
            }
        ]
    }
