'''
A simple script that converts .py file to .txt file. 
'''
import sys
import os
import shutil

def process_dir(data, dir, files):
    print "processing %s" % dir
    source_dir = data['source_dir']
    target_dir = data['target_dir']
    relative_path = dir.replace(source_dir, '')
    for file in files:
        path = os.path.join(dir, file)
        txt_path = os.path.join(target_dir, relative_path, file)
        if os.path.isdir(path):
            try:
                os.mkdir(txt_path)
            except:
                print 'Failed to create %s' % txt_path
                sys.exit(1)
        else:
            if path.endswith('.py'):
                txt_path = '%s.txt' % txt_path[:-3]
            print 'copying %s to %s' % (path, txt_path)
            shutil.copy(path, txt_path)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print 'Wrong arguments.'
        print "Usage example: py_to_txt.py path/to/the/directory path/to/target/directory"
        sys.exit()
    source_dir, target_dir = sys.argv[1], sys.argv[2]
    if not os.path.exists(source_dir):
        print '%s does not exist. Please provide a valid directory to convert.' % source_dir
        sys.exit()
    if not os.path.exists(target_dir):
        print '%s does not exist yet, trying to create it.' % target_dir
        try:
            os.mkdir(target_dir)
            print 'Target directory created.'
        except:
            print 'Failed to create target directory "%s"' % target_dir
            sys.exit()

    print 'Start converting. Converting files in %s to %s. ' % (sys.argv[1], sys.argv[2])
    data = {
        'source_dir': source_dir,
        'target_dir': target_dir,
    }
    os.path.walk(sys.argv[1], process_dir, data)
    print 'Done. All files converted to txt.'
