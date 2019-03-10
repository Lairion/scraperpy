import itertools,asyncio,aiohttp,json,sqlite3,time,os,random
import settings
name = input('Input name your db:')
conn = sqlite3.connect(os.path.join(settings.PROJECT_DIR,name+".sqlite3"))
cursor = conn.cursor()


en_letters = [chr(i) for i in range(ord("a"),ord("z")+1)]+[chr(i) for i in range(ord("A"),ord("Z")+1)]
ru_letters = [chr(i) for i in range(ord("а"),ord("я")+1)]+[chr(i) for i in range(ord("А"),ord("Я")+1)]

async def myrange(start, stop=None, step=1):
    if stop:
        range_ = range(start, stop, step)
    else:
        range_ = range(start)
    for i in range_:
        yield i
        await asyncio.sleep(0)

async def method_post(session, url,data=None):
    async with session.post(url,data=data) as response:
        if response.status !=200:
            time.sleep(1)
            return await method_post(session,url,data)
        return await response.text()

def check_exist(comb):
    combs = cursor.execute("""SELECT id,comb from combinations WHERE comb=:combin""",{'combin':comb}).fetchall()
    return len(combs)>0

async def run_insert(session,url,str_comb):
    response = await method_post(session,url,data={'q':str_comb})
    data = json.loads(response)
    if data:
        cursor.execute("""INSERT INTO combinations(comb)
            VALUES (?)""",(str_comb,))
        conn.commit()
        query = json.loads(response).get('query')
        str_comb_id = cursor.lastrowid
        query = [(str_comb_id,i) for i in query]
        cursor.executemany("INSERT INTO hints(combination_id,item) VALUES (?,?)", query)
        conn.commit()
    

async def scraper(letters):
    url = "https://allo.ua/ru/catalogsearch/ajax/suggest/?currentTheme=main"
    async for i in myrange(1,4):
        combs = list(itertools.permutations(letters,i))
        async with aiohttp.ClientSession() as session:
            for comb in combs:
                str_comb = "".join(comb)
                ch_exist = check_exist(str_comb)
                if not ch_exist:
                    await run_insert(session,url,str_comb)    

tasks = [
    asyncio.ensure_future(scraper(en_letters)),
    asyncio.ensure_future(scraper(ru_letters)),
    ]


asyncio.get_event_loop().run_until_complete(asyncio.wait(tasks))
conn.close()

