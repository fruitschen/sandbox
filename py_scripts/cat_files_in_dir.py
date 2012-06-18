'''
Cat all .py files in a directory into a single txt file. 
'''
import sys
import os

def process_dir(data, dir, files):
    files.sort()
    for file in files:
        path = os.path.join(dir, file)
        if path.endswith('.py'):
            rel_path = path.replace(data['prefix'], '')
            print '#%s' % (rel_path)
            print open(path).read()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage example: cat_files_in_dir.py path/to/the/directory"
        sys.exit(1)
    source_dir = sys.argv[1]
    prefix = os.sep.join(source_dir.split(os.sep)[:-1])
    if not os.path.exists(source_dir):
        print '%s does not exist. Please provide a valid directory to convert.' % source_dir
        sys.exit(1)

    data = {'prefix': prefix}
    os.path.walk(source_dir, process_dir, data)
