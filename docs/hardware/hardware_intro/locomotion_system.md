# Locomotion System

MICKY uses a Mecanum wheel-based locomotion system, enabling omnidirectional motion without requiring rotation of the robot body.

This configuration allows the robot to move freely in any direction, improving maneuverability in constrained industrial environments.

---

## Mecanum Wheels

The robot is equipped with four Mecanum wheels, which allow motion in multiple directions through the combination of individual wheel velocities.

This enables:

* Forward and backward motion
* Lateral (sideways) motion
* Rotation in place
* Combined movements (e.g., diagonal trajectories)

---

## Hardware Configuration

The locomotion system is composed of:

* **Nema 23 stepper motors** — actuation system
* **TB6600 drivers** — motor control
* **Arduino Mega 2560** — low-level control unit
* **MPU6050 sensors (I2C)** — state estimation

This setup provides precise motor control and reliable feedback for motion estimation.

---

## Kinematics Model

The robot kinematics is based on converting desired robot velocities:

* linear velocity in X: `v_x`
* linear velocity in Y: `v_y`
* angular velocity: `ω`

into individual wheel velocities.

This allows full omnidirectional control using a unified velocity command interface.

---

## Control Architecture

The locomotion system follows a hybrid control architecture:

* **High-level control (ROS 2)** — responsible for planning and decision-making
* **Low-level control (Arduino)** — responsible for real-time motor execution

This separation ensures flexibility, scalability, and real-time performance.

---

## Communication

Communication between the onboard computer and the microcontroller is performed via a serial interface.

Velocity commands are transmitted using the format:

```text
<v_x, v_y, ω>
```

This lightweight protocol ensures low-latency communication between high-level and low-level systems.

---

## Firmware Overview

The microcontroller firmware is designed for low-latency and non-blocking execution.

The main control loop consists of:

1. Serial command reception
2. Safety mechanism (fail-safe)
3. Kinematic processing
4. Sensor acquisition
5. Motor control

Telemetry includes:

* orientation
* acceleration
* angular velocity
* temperature

---

## ROS 2 Integration

The system is integrated with ROS 2 through two main nodes:

* **CmdVelToSerial** — converts `/cmd_vel` commands into serial messages
* **ImuSerialPublisher** — publishes IMU sensor data

This architecture allows seamless integration with navigation and control frameworks.
