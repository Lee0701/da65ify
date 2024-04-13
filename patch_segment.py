
import sys
import os

indent = ' ' * 8

def ines(input_file, output_file):
    copy(input_file, output_file, 'INES', None)

def prg(input_file, output_file):
    bank_num = ''.join(os.path.splitext(input_file)[0][4:])
    copy(input_file, output_file, f'PRG{bank_num}', f'bank{bank_num}')

def copy(input_file, output_file, segment, scope):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    result = []
    for line in lines:
        result.append(line)
        if line.strip() == '.setcpu "6502"':
            if scope is not None:
                result.append(f'\n{indent}.scope {scope}')
            if segment is not None:
                result.append(f'\n{indent}.segment "{segment}"')
            result.append(f'\n')
    if scope is not None:
        result.append(f'\n{indent}.endscope')

    with open(output_file, 'w') as f:
        for line in result:
            f.write(line)

if __name__ == '__main__':
    args = sys.argv[1:]
    [input_file, output_file] = args
    if input_file.startswith('ines'):
        ines(input_file, output_file)
    if input_file.startswith('bank'):
        prg(input_file, output_file)
