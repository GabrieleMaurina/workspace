import asyncio as asy
import time

async def say_after(delay, what):
    await asy.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

asy.run(main())

print(f"after {time.strftime('%X')}")
