from mavsdk import System
from mavsdk.mission import MissionItem, MissionPlan
import asyncio


async def run():
    drone = System()
    await drone.connect(system_address="serial:///dev/ttyTHS1:57600")

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print("Drone connected!")
            break

    # Define waypoints
    mission_items = [
        MissionItem(47.397750, 8.545607, 20, 10, True, float('nan'),
                    float('nan'), MissionItem.CameraAction.NONE, float('nan'), float('nan')),
        MissionItem(47.398000, 8.546000, 20, 10, True, float('nan'),
                    float('nan'), MissionItem.CameraAction.NONE, float('nan'), float('nan')),
        MissionItem(47.398250, 8.546500, 20, 10, True, float('nan'),
                    float('nan'), MissionItem.CameraAction.NONE, float('nan'), float('nan'))
    ]

    mission_plan = MissionPlan(mission_items)

    # Upload mission
    print("-- Uploading mission")
    await drone.mission.upload_mission(mission_plan)

    # Arm and start mission
    print("-- Arming")
    await drone.action.arm()

    print("-- Starting mission")
    await drone.mission.start_mission()

    # Monitor mission progress
    async for mission_progress in drone.mission.mission_progress():
        print(f"Mission progress: {mission_progress.current}/{mission_progress.total}")
        if mission_progress.current == mission_progress.total:
            print("-- Mission complete")
            break

    # Return and land
    print("-- Landing")
    await drone.action.land()


asyncio.run(run())
