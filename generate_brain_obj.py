#!/usr/bin/env python3
"""Generate a simple brain-like 3D model as an OBJ file.

This script procedurally creates a very rough approximation of a human
brain by stitching two noisy ellipsoids (hemispheres) together. It
writes the mesh to ``brain.obj`` in the current directory.
"""

import math

# Base ellipsoid radii for each hemisphere
A = 1.4  # x radius
B = 1.6  # y radius
C = 1.2  # z radius

# Amount of wavy noise to mimic folds
NOISE = 0.15

# Resolution of the grid used to generate vertices
N = 40


def add_hemisphere(vertices, faces, hemi_id, offset_x):
    """Append vertices/faces for a hemisphere.

    Parameters
    ----------
    vertices : list
        Target list for vertex tuples (x, y, z).
    faces : list
        Target list for face index triples.
    hemi_id : int
        0 for left hemisphere, 1 for right hemisphere.
    offset_x : float
        Horizontal offset for the hemisphere center.
    """
    base = len(vertices)
    for i in range(N + 1):
        u = math.pi * i / N
        for j in range(N + 1):
            v = 2.0 * math.pi * j / N
            noise = NOISE * math.sin(6 * u) * math.sin(6 * v)
            x = (A + noise) * math.sin(u) * math.cos(v) + offset_x
            y = (B + noise * 0.7) * math.cos(u)
            z = (C + noise) * math.sin(u) * math.sin(v)
            vertices.append((x, y, z))

    for i in range(N):
        for j in range(N):
            v0 = base + i * (N + 1) + j
            v1 = base + (i + 1) * (N + 1) + j
            v2 = base + (i + 1) * (N + 1) + (j + 1)
            v3 = base + i * (N + 1) + (j + 1)
            faces.append((v0 + 1, v1 + 1, v2 + 1))
            faces.append((v0 + 1, v2 + 1, v3 + 1))


if __name__ == "__main__":
    verts = []
    faces = []
    # Left and right hemispheres
    add_hemisphere(verts, faces, 0, offset_x=-0.75)
    add_hemisphere(verts, faces, 1, offset_x=0.75)

    with open("brain.obj", "w") as f:
        for x, y, z in verts:
            f.write(f"v {x:.6f} {y:.6f} {z:.6f}\n")
        for a, b, c in faces:
            f.write(f"f {a} {b} {c}\n")

    print(f"brain.obj created with {len(verts)} vertices and {len(faces)} faces")
