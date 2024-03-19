'''
/Applications/Blender.app/Contents/MacOS/Blender --background --python rig_fix.py 

'''
from bpy import ops, data, context
import json, os, sys, random

source = "/Users/rlizardo/proton-charm-shoppers/shoppers_v4/"
join = os.path.join
BVHPATH = join(source, "bvh/")
JSONPATH = join(source, "json/") 
CODEPATH = join(source, "python/")
SIMHUMAN = join(source, "3dhumans/")

if CODEPATH not in sys.path:
    sys.path.append(CODEPATH)
    
import blender as bl
import importlib as il
il.reload(bl)

name = 'Armature'
#bl.slc_obj(name)
#ops.object.transforms_to_deltas(mode='SCALE')
#ops.object.transforms_to_deltas(mode='ALL')

for i in range(48,51):
    shopper = 'shopper_' + str(i)
    new_shopper = 'shopper_' + str(i+1)
    rig = shopper + '_rig'
    existing = SIMHUMAN + str(shopper) + '.blend'
    path = SIMHUMAN + str(new_shopper) + '.blend'
    print("opening: "+ str(existing))
    ops.wm.open_mainfile(filepath=existing)
    name = rig
    bl.slc_obj(name)

'''
/Applications/Blender.app/Contents/MacOS/Blender --background --python rig_fix.py 

'''
from bpy import ops, data, context
import json, os, sys, random

source = "/Users/rlizardo/proton-charm-shoppers/shoppers_v5/"
join = os.path.join
BVHPATH = join(source, "bvh/")
JSONPATH = join(source, "json/") 
CODEPATH = join(source, "python/")
SIMHUMAN = join(source, "3dhumans/")

if CODEPATH not in sys.path:
    sys.path.append(CODEPATH)
    
import blend_cmd as bl
import importlib as il
il.reload(bl)

name = 'Armature'
#bl.slc_obj(name)
#ops.object.transforms_to_deltas(mode='SCALE')
#ops.object.transforms_to_deltas(mode='ALL')

bl.format_rig_name(rig_name,old_name)



    # ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
    # ops.object.transforms_to_deltas(mode='SCALE')    
    # ops.object.transforms_to_deltas(mode='ALL')

    # for obj in data.objects:
    #     print(obj)
    #     data.objects[obj.name].pass_index = 1
    #     print("Assigning index to: " + str(obj.name))


    # #data.objects[name].name = rig
   
   
     ops.wm.save_as_mainfile(filepath=existing)
     ops.wm.open_mainfile(filepath=path)

    
        



    # ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
    # ops.object.transforms_to_deltas(mode='SCALE')    
    # ops.object.transforms_to_deltas(mode='ALL')

    # for obj in data.objects:
    #     print(obj)
    #     data.objects[obj.name].pass_index = 1
    #     print("Assigning index to: " + str(obj.name))


    ops.wm.save_as_mainfile(filepath=existing)
    ops.wm.open_mainfile(filepath=path)

    
        
