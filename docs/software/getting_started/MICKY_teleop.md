# MICKY Teleop

This section guides you through running the MICKY teleoperation.

---

## Keyboard Teleop

After installing all required packages, connect the Arduino board (already configured according to the installation guide) to your computer.

Then, open two terminals.

---

In the first terminal, run:

```bash
ros2 launch motors_controller motors_controller.launch.py
```

---

In the second terminal, run:

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

---

Use the following keys to control the robot:

| Key | Action |
|-----|--------|
| `i` | Move forward |
| `,` | Move backward |
| `j` | Turn left |
| `l` | Turn right |
| `u` | Forward + left |
| `o` | Forward + right |
| `m` | Backward + left |
| `.` | Backward + right |
| `k` | Stop the robot |

## Xbox Controller Teleop

teste2