from os import walk
import argparse

assert 1==1, 'Just a test.'

parser = argparse.ArgumentParser()
# The path to the directory is required
required = parser.add_argument_group('required arguments')
required.add_argument('path', type=str,
                      help='Pathname of directory to analyze.')

# Allow filtering
parser.add_argument('-i', '-ignore', nargs='+', dest='blacklist',
                    help='File extensions to ignore.', default=[])

# Allow depth
parser.add_argument('-d', '-depth', type=int, dest='depth',
                    help='Depth to which to probe (top-level is 0).',
                    default=float('inf'))

# Get the user parameters
parameters = parser.parse_args()
path = parameters.path
if not path.endswith('/'):
    path += '/'
blacklist = parameters.blacklist
depth = parameters.depth

# The user inputs a directory
directory = path.split('/')[-2]
# Initialize a string which will become a markdown file
markup = '    {0}'.format(directory)

def replace(string, start, step):
    ''' Replace big gaps with '│' at regular intervals. '''
    newString = list(string)
    for i in range(start-1, len(newString), step):
        newString[i] = '│'
    return ''.join(newString)

def display(path, space='       ', level=0, hasFiles=True):
    ''' We need a recursive function. '''
    # Modify the previously initialized string
    global markup
    # Get all the directories and files of the current path
    _, directories, files = next(walk(path))
    # Verify depth level
    if level <= depth:
        # If there are sub-directories
        if directories:
            # For each sub-directory
            for directory in directories[:-1]:
                # Add the sub-directory name to the string
                if level != 0:
                    if level >= 2:
                        markup += '\n    │{0}{1}'.format(replace(' ' * (len(space)-8), 4, 4) + '├───┐ ', directory)
                    else:
                        markup += '\n    │{0}{1}'.format(' ' * (len(space)-8) + '├───┐ ', directory)
                else:
                    markup += '\n    {0} {1}'.format(' ' * (len(space)-8) + '├───┐', directory)
                # Check all the sub-directories and files of the sub-directory
                display('{0}/{1}'.format(path, directory), space + '    ', level+1)
            # Different style for the last directory
            directory = directories[-1]
            if not directory.startswith('.'):
                # Add the sub-directory name to the string
                if level != 0:
                    if level >= 2:
                        markup += '\n    │{0}{1}'.format(replace(' ' * (len(space)-8), 4, 4) + '├───┐ ', directory)
                    else:
                        markup += '\n    │{0}{1}'.format(' ' * (len(space)-8) + '└───┐ ', directory)
                    # Check all the sub-directories and files of the sub-directory
                    if files:
                        display('{0}/{1}'.format(path, directory), space + '    ', level+1)
                    else:
                        display('{0}/{1}'.format(path, directory), space + '    ', level+1, False)
                else:
                    # Add the sub-directory name to the string
                    markup += '\n    ├{0}{1}'.format(' ' * (len(space)-8) + '───┐ ', directory)
                    # Check all the sub-directories and files of the sub-directory
                    display('{0}/{1}'.format(path, directory), space + '    ', level+1)
        # If there are files
        if files:
            # For each file
            for file in files[:-1]:
                # Verify the extension isn't on the blacklist
                extension = file.split('.')[-1]
                if not file.startswith('.') and extension not in blacklist:
                    # Add it to the string
                    if level != 0:
                        if level >= 2:
                            if hasFiles is True:
                                markup += '\n    │{0}├─── {1}'.format(replace(' ' * (len(space)-8), 4, 4), file)
                            else:
                                markup += '\n    │{0}├─── {1}'.format(replace(' ' * (len(space)-8), 8, 4), file)
                        else:
                            markup += '\n    │{0}├─── {1}'.format(' ' * (len(space)-8), file)
                    else:
                        markup += '\n    {0}├─── {1}'.format(' ' * (len(space)-8), file)
            file = files[-1]
            # Verify the extension isn't on the blacklist
            extension = file.split('.')[-1]
            if not file.startswith('.') and extension not in blacklist:
                # Different style for the last file
                if level != 0:
                    if level >= 2:
                        if hasFiles is True:
                            markup += '\n    │{0}└─── {1}'.format(replace(' ' * (len(space)-8), 4, 4), file)
                        else:
                            markup += '\n    │{0}└─── {1}'.format(replace(' ' * (len(space)-8), 8, 4), file)
                    else:
                        markup += '\n    │{0}└─── {1}'.format(' ' * (len(space)-8), files[-1])
                else:
                    markup += '\n    └{0}─── {1}'.format(' ' * (len(space)-8), files[-1])
    
if __name__ == '__main__':
    # Apply the function to a directory and it will go through it recursively
    display(path)

    # Save the file as a markdown file, it will be a pretty "well"
    with open('{0}architecture.md'.format(path), 'w') as file:
        file.write(markup)

    print ('{0}architecture.md'.format(path) + ' successively saved.')
