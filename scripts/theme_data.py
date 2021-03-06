#!/usr/bin/python3

import argparse
import glob
import os.path


def __make_theme_data(input_dir: str, project_root: str, output: str):
    enc = 'utf-8'

    with open(output, 'wb') as f:

        f.write(b"// THIS FILE HAS BEEN AUTOGENERATED, DON'T EDIT!!\n")

        # Generate png image block
        f.write(b"\n// png image block\n")

        pixmaps = glob.glob(os.path.join(project_root, input_dir, '*.png'))
        pixmaps.sort()

        for x in pixmaps:
            var_str = os.path.splitext(os.path.basename(x))[0] + "_png"

            s = "\nstatic const unsigned char " + var_str + "[] = {\n\t"
            f.write(s.encode(enc))

            pngf = open(x, "rb")

            b = pngf.read(1)
            while len(b) == 1:
                f.write(hex(ord(b)).encode(enc))
                b = pngf.read(1)
                if len(b) == 1:
                    f.write(b", ")

            f.write(b"\n};\n")
            pngf.close()

        # Generate shaders block
        f.write(b"\n// shaders block\n")

        shaders = glob.glob(os.path.join(project_root, input_dir, '*.gsl'))
        shaders.sort()

        for x in shaders:
            var_str = os.path.splitext(os.path.basename(x))[0] + "_shader_code"

            s = "\nstatic const char *" + var_str + " = \n"
            f.write(s.encode(enc))

            sf = open(x, "rb")

            b = sf.readline()
            while b != "":
                if b.endswith("\r\n"):
                    b = b[:-2]
                if b.endswith("\n"):
                    b = b[:-1]
                s = '			"' + b
                f.write(s.encode(enc))
                b = sf.readline()
                if b != "":
                    f.write(b'"\n')

            f.write(b'";\n')
            sf.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Generate theme data.')

    parser.add_argument(
        'input_dir', type=str, help='The input directory of translation files'
    )
    parser.add_argument(
        'project_root', type=str, help='The project root'
    )
    parser.add_argument(
        'output', type=str, help='The output header file'
    )

    args = parser.parse_args()

    __make_theme_data(
        args.input_dir, args.project_root, args.output)
