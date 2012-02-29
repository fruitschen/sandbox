import sys
import os.path
from collections import defaultdict
from pprint import pprint

ignore_dirs = ['nbproject']
total_files = 0
total_lines = 0
file_results = defaultdict(int)
file_ignores = []
line_results = defaultdict(int)
line_types = ['.py', '.js', '.css', '.html',]
final_results = []

def process_dir(data, dir, files):
    if os.path.basename(dir) in ignore_dirs:
        return
    print "processing %s" % dir
    for file in files:
        path = os.path.join(dir, file)
        if not os.path.isdir(path):
            process_file(path)

def process_file(path):
    global total_files, total_lines
    ext = os.path.splitext(path)[-1]
    file_results[ext] += 1
    total_files += 1
    if ext in line_types:
        line_count = len(open(path, 'r').readlines())
        line_results[ext] += line_count
        total_lines += line_count

def process_results():
    global total_files, total_lines
    for key, file_count in file_results.items():
        line_count = line_results[key]
        result = {
            'ext':key,
            'files':file_count,
            'lines':line_count,
            'file_percent': '%.4f%%' % (float(file_count)/float(total_files) * 100),
            'line_percent': '%.4f%%' % (float(line_count)/float(total_lines) * 100),
            }
        final_results.append(result)

def compare_lines(result1, result2):
    return result2['lines'] - result1['lines']

def sort_results():
    final_results.sort(compare_lines)

def print_results():
    sort_results()
    for result in final_results:
        s = '%(ext)s:\t %(files)s files(%(file_percent)s),\t %(lines)s lines(%(line_percent)s)' % result
        print s

def print_html_results():
    sort_results()
    table = []
    table.append('<table>')
    for result in final_results:
        s = '<tr><td>%(ext)s</td><td>%(files)s files(%(file_percent)s)</td><td>%(lines)s lines(%(line_percent)s)</td></tr>' % result
        table.append(s)
    table.append('</table>')
    print '\n'.join(table)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Please provide the directory you want to process"
        sys.exit()
    os.path.walk(sys.argv[1], process_dir, None)
    process_results()
    if (len(sys.argv)>=3) and (sys.argv[2] == '-html'):
        print_html_results()
    else:
        print_results()
