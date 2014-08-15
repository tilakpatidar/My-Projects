import asyncio,aiohttp
@asyncio.coroutine
def get(url):
    conn = aiohttp.ProxyConnector(proxy="http://172.16.0.19:8080")
    response = yield from aiohttp.request('GET', url,connector=conn)
    return (yield from response.read_and_close())
@asyncio.coroutine
def printCode():
    url = 'http://dir.yahoo.com'
    sem = asyncio.Semaphore(5)
    with (yield from sem):
    	page = yield from get(url)
    print(str(page))
loop = asyncio.get_event_loop()
f = asyncio.wait([printCode()])
loop.run_until_complete(f)
