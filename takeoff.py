from mavsdk import System
import asyncio

async def run():
    drone = System()
    await drone.connect(system_address="serial:///dev/ttyTHS1:57600")

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print("Drone connected!")
            break

    print("Arming the drone...")
    await drone.action.arm()

    print("Taking off...")
    await drone.action.takeoff()

    await asyncio.sleep(10)
    print("Landing...")
    await drone.action.land()

asyncio.run(run())