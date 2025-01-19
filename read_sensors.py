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

    # Fetch GPS Information
    print("waiting for gps")
    async for gps_info in drone.telemetry.gps_info():
        print(f"GPS: {gps_info}")
        break

    print("waiting for batery")
    # Fetch Battery Information
    async for battery in drone.telemetry.battery():
        print(f"Battery: {battery.remaining_percent * 100:.2f}%")
        break

    # Fetch Altitude
    print("waiting for altitude")
    async for position in drone.telemetry.position():
        print(f"Altitude: {position.relative_altitude_m} m")
        break

    # Fetch Attitude
    print("waiting for attitude")
    async for attitude in drone.telemetry.attitude_euler():
        print(f"Attitude: Roll={attitude.roll_deg:.2f}, Pitch={attitude.pitch_deg:.2f}, Yaw={attitude.yaw_deg:.2f}")
        break

    # Fetch Motor Outputs
    print("waiting for motor outputs")
    async for motor in drone.telemetry.actuator_output_status():
        print(f"Output Status: Active={motor.active}, Actuator={motor.actuator}")
        break

    # Fetch velocity in the North-East-Down frame
    print("waiting for target velocity")
    async for velocity in drone.telemetry.velocity_ned():
        print(f"Velocity: North={velocity.north_m_s}, East={velocity.east_m_s}, Down={velocity.down_m_s}")
        break

asyncio.run(run())
