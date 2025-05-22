# gpt

This repository contains a simple example of a 3D and 2D canvas for creating gamified e‑learning content. Open `elearning-canvas/index.html` in a modern web browser to try the demo.

The demo lets you:

- Load an image onto the 2D canvas
- Drag the image around
- Resize the image using a handle while keeping it sharp
- View a small example 3D scene

## Procedural Brain Model

Run `generate_brain_obj.py` to create a rough brain-shaped OBJ file. The
script does not require extra dependencies and outputs `brain.obj` in
this directory:

```bash
python3 generate_brain_obj.py
```

You can then load `brain.obj` in any 3D viewer or import it into the demo
scene inside `elearning-canvas`.
