from os import walk

# Choose a directory
directory = 'bikes'
# Initialize a string which will become a markdown file
markup = '    {0}/'.format(directory.split('/')[-1])


def display(path, space='        '):
    ''' We need a recursive function. '''
    # Modify the previously initialized string
    global markup
    # Get all the directories and files of the current path
    _, directories, files = list(walk(path))[0]
    # If there are sub-directories
    if directories:
        # For each sub-directory
        for directory in directories:
            # Add the sub-directory name to the string
            markup += '\n{0}{1}/'.format(space, directory)
            # Check all the sub-directories and files of the sub-directory
            display('{0}/{1}'.format(path, directory), space + '    ')
    # If there are file
    if files:
        # For each file
        for file in files:
            # Add it to the string
            markup += '\n{0}{1}'.format(space, file)

# Apply the function to a directory and it will go through it recursively
display(directory)

# Save the file as a markdown file, it will be a pretty "well"
with open('{0}.md'.format(directory), 'w') as file:
    file.write(markup)
