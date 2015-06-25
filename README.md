# Directory Architecture

When I make tutorials or give reports I like displaying all the files and directories of a project like a cascade. These can be cumbersome to type by hand and so I wrote a small script to generate these automatically.

## Example

With markup languages you can create "wells" where this looks good.

    example
    ├───┐ static
    │   ├───┐ js
    │   │   ├─── Leaflet.vector-markers.min.js
    │   │   └─── Leaflet.vector-markers.js
    │   ├───┐ data
    │   │   └─── Toulouse.csv
    │   └───┐ css
    │       ├─── Leaflet.vector-markers.css
    │       └─── Leaflet.vector-markers.css.map
    ├───┐ lib
    │   ├─── __init__.py
    │   └─── JCDecaux.py
    ├───┐ templates
    │   └─── index.html
    ├─── serve.py
    └─── update.py

## Usage

    cd Directory-Architecture
    ./probe example/

By doing this a markdown file called ``architecture.md`` is saved into the directory to be probed. It ressembles the example above.

Make sure to not forget the ``/`` to the end of the pathname, or else ``architecture.md`` will be saved into ``Directory-Architecture``.

You can use both absolute and relative paths.

## To do

- Add filter
- Make the script callable from the shell

If you want to implement a new feature please feel free to send me a mail (**``maxhalford25@gmail.com``**) and I'll be glad to help.