import bpy
import sys

file = sys.argv[1]

def blend_export_obj(file):
    blend_file = "C:/Users/roder/Desktop/" + str(file) + ".blend"
    bpy.ops.wm.open_mainfile(filepath=blend_file)
    obj_file ="C:/Users/roder/Desktop/" + str(file) + ".obj"
    bpy.ops.export_scene.obj(filepath=obj_file)


blend_export_obj(file)