import argparse
import os
import utils


ap = argparse.ArgumentParser()
ap.add_argument('-i','--input-dir', type=str, default='images', help="input directory containing image files (default = images)", metavar='')
ap.add_argument('-c','--csv-file', type=str, default=None, help="(optional) XY coordinate file in csv format", metavar='')
ap.add_argument('-t','--tps-file', type=str, default=None, help="(optional) tps coordinate file", metavar='')
ap.add_argument('-o','--output-dir', type=str, default='.', help="output directory containing xml files (default = '.')", metavar='')
ap.add_argument('-tb','--tight-bbox', type=str, default='True', help="Enables tight-bbox (default=True)")

args = vars(ap.parse_args())
args['tight_bbox'] = args['tight_bbox'] == 'True'

assert os.path.isdir(args['input_dir']), "Could not find the folder {}".format(args['input_dir'])
    
file_sizes=utils.split_train_test(args['input_dir'], args['output_dir'])

if args['csv_file'] is not None:
    dict_csv=utils.read_csv(args['csv_file'])
    utils.generate_dlib_xml(dict_csv,file_sizes['train'],folder=os.path.join(args['output_dir'], 'train'),out_file=os.path.join(args['output_dir'], 'train.xml'), tight=args['tight_bbox'])
    utils.generate_dlib_xml(dict_csv,file_sizes['test'],folder=os.path.join(args['output_dir'], 'test'),out_file=os.path.join(args['output_dir'], 'test.xml'), tight=args['tight_bbox'])
    
if args['tps_file'] is not None:
    dict_tps=utils.read_tps(args['tps_file'])
    utils.generate_dlib_xml(dict_tps,file_sizes['train'],folder=os.path.join(args['output_dir'], 'train'),out_file=os.path.join(args['output_dir'], 'train.xml'), tight=args['tight_bbox'])
    utils.generate_dlib_xml(dict_tps,file_sizes['test'],folder=os.path.join(args['output_dir'], 'test'),out_file=os.path.join(args['output_dir'], 'test.xml'), tight=args['tight_bbox'])
  