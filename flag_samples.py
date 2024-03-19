'''Examples of flag configuration.

python3 flag_samples.py --blender='/Applications/Blender.app/Contents/MacOS/Blender' \


'''

import subprocess, sys, os
from absl import app
from absl import flags


flags.DEFINE_string('blender', None, 'Path to Blender')
flags.DEFINE_string('source_path', None, 'Path to Source Files')
flags.DEFINE_string('output_path', None, 'Path for output Files')
flags.DEFINE_integer('dataset', None, 'Dataset number for this batch')
flags.DEFINE_string('person', None,'Name of person')
flags.DEFINE_integer('end_frame', None,'Last frame of scene')
flags.DEFINE_string('scenario_number', None,'Scene number')
flags.DEFINE_integer('camera_number', None, 'Camera number for rendering')
flags.DEFINE_string('device', None,'Device for cycles rendering')
flags.DEFINE_integer('tile_size',None,'Tile size for rendering')

FLAGS = flags.FLAGS

def main(argv):
    path_to_this = os.path.dirname(os.path.abspath(__file__))

    if FLAGS.blender is None:
        raise ValueError('Please supply a valid path to a Blender executable')
    if FLAGS.source_path is None:
        raise ValueError('Please supply a valid path to a source.')
    if FLAGS.output_path is None:
        raise ValueError('Please supply a valid path to a source.')
    if FLAGS.dataset is None:
        raise ValueError('Please supply a valid path to a source.')
    if FLAGS.person is None:
        raise ValueError('Please supply a valid 3dhuman name')
    if FLAGS.end_frame is None:
        raise ValueError('Please supply an end_frame')
    if FLAGS.scenario_number is None:
        raise ValueError('Please supply a valid scenario number.')
    if FLAGS.camera_number is None:
        raise ValueError('Please supply a valid camera number.')
    if FLAGS.device is None:
        raise ValueError('Please supply a valid device GPU or CPU.')
    if FLAGS.tile_size is None:
        raise ValueError('Please supply a camera number.')  

    # Dataset number for blender to add into the file name <dataset_#>_rgb_<frame_#>.format

    #subprocess.call([FLAGS.blender, "-b", "-P", "shelf_executable.py", "--", FLAGS.model_path])
    exec_str = '{} --background --python {}/main.py -- {} {} {} {} {} {} {} {} {}'.format(
        FLAGS.blender, path_to_this, FLAGS.source_path, FLAGS.output_path, FLAGS.dataset, FLAGS.person, FLAGS.end_frame, FLAGS.scenario_number, FLAGS.camera_number, FLAGS.device, FLAGS.tile_size
    )

    os.system(exec_str)
    
if __name__ == '__main__':
    app.run(main) 



