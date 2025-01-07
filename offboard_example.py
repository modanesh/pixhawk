from mavsdk import System
from mavsdk.offboard import (OffboardError, PositionNedYaw, VelocityNedYaw)
import asyncio


async def run():
    drone = System()
    await drone.connect(system_address="serial:///dev/ttyTHS1:57600")

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print("Drone connected!")
            break

    print("Arming drone...")
    await drone.action.arm()

    print("Starting Offboard Mode...")
    # Set initial setpoint
    await drone.offboard.set_position_ned(PositionNedYaw(0.0, 0.0, -2.0, 0.0))

    # Start offboard mode
    try:
        await drone.offboard.start()
    except OffboardError as error:
        print(f"Offboard mode failed to start: {error}")
        await drone.action.disarm()
        return

    print("Moving to position (0m North, 5m East, -2m Down)")
    await drone.offboard.set_position_ned(PositionNedYaw(0.0, 5.0, -2.0, 0.0))
    await asyncio.sleep(5)

    print("Moving to position (5m North, 0m East, -2m Down)")
    await drone.offboard.set_position_ned(PositionNedYaw(5.0, 0.0, -2.0, 0.0))
    await asyncio.sleep(5)

    print("Returning to start position")
    await drone.offboard.set_position_ned(PositionNedYaw(0.0, 0.0, -2.0, 0.0))
    await asyncio.sleep(5)

    print("Stopping Offboard Mode...")
    try:
        await drone.offboard.stop()
    except OffboardError as error:
        print(f"Failed to stop Offboard mode: {error}")

    print("Landing...")
    await drone.action.land()


asyncio.run(run())
