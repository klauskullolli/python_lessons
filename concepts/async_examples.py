import asyncio 
import time 

async def hello_word():
    print("Hello")
    await asyncio.sleep(2)
    print("Word")

def hello_word_1(): 
    print("Hello")
   
    print("Word")



async def bug():
    raise Exception("not consumed")

async def main():
    asyncio.create_task(bug())

asyncio.run(main(), debug=True)


if __name__ == "__main__": 
    # start =  int(round(time.time() * 1000))

    # # run is used to run an asyncronus task that is  has a key async 
    # # turn task serial
    # asyncio.run(hello_word())

    # print("There is a async taks")
    pass