import bpy

# Use to remove default cube after open blender
def delete_start_cube():
    start_cube = bpy.data.objects['Cube']
    bpy.data.objects.remove(start_cube, do_unlink = True)
