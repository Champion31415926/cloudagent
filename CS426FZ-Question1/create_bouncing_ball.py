"""CS426FZ Assignment Question 1, following the lab notes only.

Red smooth ball, blue ground plane, location keyframes.
No extra objects, rotation, graph-editor edits, camera animation, or lighting changes.
"""

import bpy

OUT_DIR = "/home/ubuntu/Desktop/CS426FZ-Question1"
BLEND_PATH = f"{OUT_DIR}/bouncing_ball.blend"
FRAME_PATH = "/tmp/cs426-frames/frame_"


def make_material(name, color):
    material = bpy.data.materials.new(name)
    material.diffuse_color = (*color, 1.0)
    material.use_nodes = True
    principled = material.node_tree.nodes.get("Principled BSDF")
    if principled is not None:
        principled.inputs["Base Color"].default_value = (*color, 1.0)
    return material


def main():
    # Keep the default camera and light. Replace only the startup cube.
    cube = bpy.data.objects.get("Cube")
    if cube is not None:
        bpy.data.objects.remove(cube, do_unlink=True)

    bpy.ops.mesh.primitive_ico_sphere_add(radius=1.0, location=(0.0, 0.0, 4.0))
    ball = bpy.context.active_object
    ball.name = "Ball"
    bpy.ops.object.shade_smooth()
    ball.data.materials.append(make_material("BallRed", (0.8, 0.02, 0.02)))

    # The notes add one blue planar mesh for the ball to land on.
    bpy.ops.mesh.primitive_plane_add(size=8.0, location=(0.0, 0.0, 0.0))
    ground = bpy.context.active_object
    ground.name = "Ground"
    ground.data.materials.append(make_material("GroundBlue", (0.1, 0.25, 0.8)))

    # Place the existing camera once, the same idea as Align Camera to View.
    # It is not keyframed.
    camera = bpy.data.objects["Camera"]
    camera.location = (7.0, -8.0, 4.5)
    direction = bpy.context.scene.cursor.location.copy()
    direction.z = 1.5
    camera.rotation_euler = (direction - camera.location).to_track_quat("-Z", "Y").to_euler()
    bpy.context.scene.camera = camera

    # Lab notes: Z about 4, then Z=1 at frame 10, then about 2m at frame 15,
    # then a few more location keyframes. Default interpolation only.
    for frame, height in (
        (1, 4.0),
        (10, 1.0),
        (15, 2.0),
        (22, 1.0),
        (28, 1.5),
        (36, 1.0),
    ):
        ball.location.z = height
        ball.keyframe_insert(data_path="location", frame=frame)

    scene = bpy.context.scene
    scene.frame_current = 1
    scene.render.engine = "BLENDER_WORKBENCH"
    scene.display.shading.light = "STUDIO"
    scene.display.shading.color_type = "MATERIAL"
    scene.render.resolution_x = 1920
    scene.render.resolution_y = 1080
    scene.render.resolution_percentage = 10
    # Blender 5.2 Workbench does not expose the old AVI JPEG format here.
    # Render the frames; the movie is encoded to AVI JPEG afterwards.
    scene.render.image_settings.file_format = "PNG"
    scene.render.filepath = FRAME_PATH

    bpy.ops.wm.save_as_mainfile(filepath=BLEND_PATH)
    bpy.ops.render.render(animation=True)
    print(f"SAVED {BLEND_PATH}")


if __name__ == "__main__":
    main()
