''' Config functions for the baseline project.
'''
import os
import sys
import bpy
import random

sourcepath = sys.argv[5]
outpath = sys.argv[6]
camera_number = sys.argv[11]

padding = '_#######'
shoppers = [8,4,7]


class Path:
    '''Paths for outputing Baseline Data'''
    
    def __init__(self, path, dir):
        self.path = path
        self.dir = dir

    def join(self):
        path = self.path + self.dir
        return path

def cam_name():
    camera_name = 'camera.'+ '{0:03d}'.format(int(camera_number))
    return camera_name


def rgb_outpath():
    path = outpath
    dir = '/rgb/'
    rgb_path = Path(path,dir)
    rgb = rgb_path.join()
    return rgb

def mask_outpath():
    path = outpath
    dir = '/masks/'
    mask_path = Path(path,dir)
    mask = mask_path.join()
    return mask

def load_blend_file(file):
    print(file)
    bpy.ops.wm.open_mainfile(filepath = file)

def depth_cam_name():
    cam_name = 'depth_camera.'+ '{0:03d}'.format(int(camera_number))
    print(cam_name)
    return cam_name

def rgb_image_name():
    cam = cam_name()
    file = 'rgb_' + str(cam) + str(padding) 
    return file


def mask_name(shopper_id):
    shopper = shoppers[shopper_id]
    mask = "shopper_id_" + str(shopper) + "_" + str(cam_name()) + "_#######" 
    return mask

def rgb_node_tree():
    
    #Comp node variables
    comp_node = 'CompositorNodeRLayers'
    b_cont = 'CompositorNodeBrightContrast'
    rgbcrv = 'CompositorNodeCurveRGB'
    blr = 'CompositorNodeBlur'
    mix = 'CompositorNodemixRGB'
    img = 'CompositorNodeImage'
    alpha_over = 'CompositorNodeAlphaOver'
    composite = 'CompositorNodeComposite'
    output = 'CompositorNodeOutputFile'
    normalize = 'CompositorNodenormalize'
    math = 'CompositorNodeMath'
    invert = 'CompositorNodeInvert'
    color_ramp = 'CompositorNodeValToRGB'
    id = 'CompositorNodeIDMask'
    dist = 'CompositorNodeLensdist'
    rgb = 'CompositorNodeRGB'
    
    mask_list = []
    for s in range(3):
        shopper_id = s
        mask_list.append(mask_name(shopper_id))
    
    mask_image_name = mask_list[0]
    mask_image_name_2 = mask_list[1]
    mask_image_name_3 = mask_list[2]
 
    
    scene = bpy.context.scene
    view_layers = scene.view_layers["View Layer"]
    scene.use_nodes = True
    view_layers.use_pass_object_index = True
    bpy.context.scene.view_layers["View Layer"].use_pass_z = True


    tree = scene.node_tree
    new_node = tree.nodes.new
    links = tree.links
    link = links.new

    # Clear scene and set background to transparent.
    for node in tree.nodes:
        tree.nodes.remove(node)
    scene.cycles.film_transparent = True

    # Create composite Node Tree.
    ren_layer = new_node(type= comp_node)
    ren_layer.location = -500, 500

    # Combine AO Pass
    mix_ao = new_node(type=mix)
    mix_ao.location = -200,500
    mix_ao.blend_type = 'MULTIPLY'
    link(ren_layer.outputs['AO'],mix_ao.inputs[2])
    link(ren_layer.outputs['Image'],mix_ao.inputs[1])

    # Brightness Contrast Node.
    b = new_node(type=b_cont)
    b.location = 50, 500
    b.inputs[1].default_value = .5
    b.inputs[2].default_value = .5
    link(mix_ao.outputs['Image'],b.inputs[0])

    # rgb Curve.
    r = new_node(type=rgbcrv)
    r.location = 250,500
    link(b.outputs['Image'],r.inputs[1])

    # Blur
    bl = new_node(type=blr)
    bl.location = 500,500
    bl.use_relative = True
    bl.factor_y = .015
    bl.factor_x = .015
    link(r.outputs['Image'],bl.inputs[0])

    # mix node to combine blur and subject matter.
    m = new_node(type=mix)
    m.location = 700,500
    m.blend_type = 'ADD'
    m.inputs[0].default_value = .1
    link(ren_layer.outputs['Image'],m.inputs[2])
    link(bl.outputs['Image'],m.inputs[1])

    # Apply distortion.
    lendist = new_node(type=dist)
    lendist.location = 1100,500
    lendist.inputs[2].default_value = 0
    link(m.outputs['Image'],lendist.inputs[0])


    # Outputfile Node for rgb Pass.
    out_file = new_node(type=output)
    out_file.location = 1500, 300
    out_file.format.file_format = "JPEG"
    out_file.name = 'rgb_pass'
    out_file.file_slots.remove(out_file.inputs[0])
    out_file.file_slots.new(rgb_image_name)
    out_file.base_path = rgb_outpath
    link(lendist.outputs['Image'],out_file.inputs[0])
    out_file.format.color_mode = 'rgb'

    # Pass index for person.

    idmask = new_node(type=id)
    idmask.location = 50,100
    idmask.index = 1
    idmask.use_antialiasing = True
    out_file_mask = new_node(type=output)
    out_file_mask.location = 450,100
    out_file_mask.format.file_format = 'JPEG'
    out_file_mask.file_slots.remove(out_file_mask.inputs[0])
    out_file_mask.file_slots.new(mask_image_name)
    out_file_mask.name = 'mask_pass'
    out_file_mask.base_path = mask_outpath
    link(ren_layer.outputs['IndexOB'],idmask.inputs[0])
    link(idmask.outputs['Alpha'],out_file_mask.inputs[0])
    bpy.context.scene.render.image_settings.file_format = 'JPEG'
    bpy.context.scene.render.image_settings.quality = 25

    idmask2 = new_node(type=id)
    idmask2.location = -50,-100
    idmask2.index = 2
    idmask2.use_antialiasing = True
    out_file_mask2 = new_node(type=output)
    out_file_mask2.location = -450,-100
    out_file_mask2.format.file_format = 'JPEG'
    out_file_mask2.file_slots.remove(out_file_mask2.inputs[0])
    out_file_mask2.file_slots.new(mask_image_name_2)
    out_file_mask2.name = 'mask_pass_2'
    out_file_mask2.base_path = mask_outpath
    link(ren_layer.outputs['IndexOB'],idmask2.inputs[0])
    link(idmask2.outputs['Alpha'],out_file_mask2.inputs[0])
    bpy.context.scene.render.image_settings.file_format = 'JPEG'
    bpy.context.scene.render.image_settings.quality = 25

    idmask3 = new_node(type=id)
    idmask3.location = -150,-200
    idmask3.index = 3
    idmask3.use_antialiasing = True
    out_file_mask3 = new_node(type=output)
    out_file_mask3.location = -450,-200
    out_file_mask3.format.file_format = 'JPEG'
    out_file_mask3.file_slots.remove(out_file_mask3.inputs[0])
    out_file_mask3.file_slots.new(mask_image_name_3)
    out_file_mask3.name = 'mask_pass_3'
    out_file_mask3.base_path = mask_outpath
    link(ren_layer.outputs['IndexOB'],idmask3.inputs[0])
    link(idmask3.outputs['Alpha'],out_file_mask3.inputs[0])
    bpy.context.scene.render.image_settings.file_format = 'JPEG'
    bpy.context.scene.render.image_settings.quality = 25

