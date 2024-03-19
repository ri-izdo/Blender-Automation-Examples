# Wrapper for Blender commands.

import bpy, sys, os
import subprocess
from bpy import ops, context, data

###########################
# Blender basics.
###########################


def blend_export_obj(file):
    file = "C:/Users/roder/Desktop/" + str(file) + ".blend"
    bpy.ops.wm.open_mainfile(filepath=file)
    obj_file ="C:/Users/roder/Desktop/" + str(file) + ".obj"
    bpy.ops.export_scene.obj(filepath=obj_file)


def add_locator(x,y,z):
    bpy.ops.object.empty_add(type='PLAIN_AXES', location=(x,y,z))


def slc_obj(name):
    # Blend function to select object.
    obj = data.objects[name]
    obj.select_set(True)
    context.view_layer.objects.active = obj

def imp_fbx(file):
    imp = bpy.ops.import_scene
    imp.fbx(filepath=file)
    # Blend function to import object.

def imp_bvh(bvh_file_path):
    imp = bpy.ops.import_anim
    imp.bvh(filepath=bvh_file_path,global_scale=.068, use_fps_scale=True)

    # Blend function to import object.
def openBlend(blend_path,blend_name):
    blend_file = blend_path + str(blend_name)
    ops.wm.open_mainfile(filepath=blend_file)

def appendBlend(BLENDPATH,file,collection):
    blend_collection_path = BLENDPATH+str(file)+"\\Collection\\"
    ops.wm.append(filename=collection, directory=blend_collection_path)
    print("Appended Collection: "+ str(blend_collection_path))

def appendShopper(shopper,SIMHUMAN):
    print("Hi")
    dir = SIMHUMAN + str(shopper) + ".blend\\Collection\\"
    print("Appended Collection: " + str(dir))
    ops.wm.append(filename=shopper, directory=dir)

def reset_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

def count_startswith(name):
    obj_name = [ob for ob in bpy.data.objects if ob.name.startswith(name)]
    total = len(obj_name)
    print('Total objects that starts with "' + str(name) + '" = ' + str(total))
    return total


###########################
# Motion Capture Commands.
###########################

# Place armature rig onto a constraint.
def shopper_constraint(rig, point_name):
    point = data.objects[point_name]  
    shopper = data.objects[rig]  
    ops.object.select_all(action='DESELECT')
    shopper.select_set(True)
    context.view_layer.objects.active = shopper
    constraint_add = ops.object.constraint_add
    constraint_add(type='COPY_LOCATION')
    constraint_add(type='COPY_ROTATION')

    #  Constraint Settings. 
    shopper_constraint = context.object.constraints
    shopper_constraint['Copy Location'].target = point
    shopper_constraint['Copy Rotation'].target = point


def change_bn_name(rig_name, old_name):
    dob = bpy.data.objects[rig_name]
    bn = dob.pose.bones
    bn_list = []

    for i in bn:
        bn_list.append(i.name)
        
    for names in range(len(bn_list)):
        new_name = bn_list[names].replace(old_name,'')
        bn[names].name = new_name
        print(new_name)
    


# Gives an armature rig an animation.
def add_nla(rig,action_name):
    cOB = context.object
    bpy.ops.object.select_all(action='DESELECT')
    obj_rig = data.objects[rig]
    obj_rig.select_set(True)
    context.view_layer.objects.active = obj_rig
    context.selected_objects[0].animation_data.action = bpy.data.actions[action_name]
    cOB.constraints["Follow Path"].use_curve_follow = True
