import bpy
import sys
import os
import argparse


def main_function(data_path, save_path):
    from blender import scene, data_loader, chart

    scene.delete_start_cube()

    try:
        data = data_loader.get_data_from(data_path)
    except Exception as e:
        print(e)
        print('Blander will be closed!')
        bpy.ops.wm.quit_blender()
        sys.exit()

    #build chart
    column_chart = chart.ColumnChart(data)
    #render and save

def main():
    argv = sys.argv

    # Make blender able to see arguments
    if '--' not in argv:
        argv = []
    else:
        argv = argv[argv.index('--') + 1:]

    parse = argparse.ArgumentParser()
    parse.add_argument('-d', '--data', dest = 'data_path', required = True, type = str, help = 'Where is data for chart')
    parse.add_argument('-s', '--save', dest = 'save_path', required = True, type = str, help = 'Where to save results')

    args = parse.parse_args(argv)
    data_path = args.data_path
    save_path = args.save_path

    main_function(data_path, save_path)


# Make blender python script able to use python modules from this directory
dir = os.path.dirname(bpy.data.filepath)
if not dir in sys.path:
    sys.path.append(dir )

sys.exec_prefix

if __name__ == '__main__':
    main()
