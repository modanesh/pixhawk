from mavsdk import System
from mavsdk.mission import MissionItem, MissionPlan

async def upload_mission():
    drone = System()
    await drone.connect(system_address="serial:///dev/ttyTHS1:57600")

    mission_items = []
    mission_items.append(MissionItem(47.397742, 8.545594, 20, 10, True, float('nan'), float('nan'), MissionItem.CameraAction.NONE))

    mission_plan = MissionPlan(mission_items)
    await drone.mission.upload_mission(mission_plan)

asyncio.run(upload_mission())