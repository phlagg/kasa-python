import asyncio

from kasa import Discover


async def app():
    # dev = await Discover.discover_single('192.168.1.203')
    devices = await Discover.discover(discovery_timeout=10, discovery_packets=3)
    for devs in devices.values():
        await devs.update()
        print(devs.host)

        # if dev is not None:
        #     await dev.turn_on()
        #     modules = dev.modules
        #     print(modules)

        # await dev.update()


def main():
    print('Hello')
    asyncio.run(app())


if __name__ == '__main__':
    main()
