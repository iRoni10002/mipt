async def main():
     # Run "set_after()" coroutine in a parallel Task.
    fut = asyncio.ensure_future(
        set_after(1, '... world'))

    print('hello ...')

    # Wait until *fut* has a result (1 second) and print it.
    # Alternative way to get a result, just use it.
    print(await fut)
