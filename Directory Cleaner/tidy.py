import os
for root, dirs, files in os.walk("example", topdown=False):
    for name in files:
        file = os.path.join(root, name)
        if file.endswith('~'):
            os.remove(file)
