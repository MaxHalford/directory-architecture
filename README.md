# Directory Architecture

[![Build Status](https://travis-ci.org/MaxHalford/Directory-Architecture.svg)](https://travis-ci.org/MaxHalford/Directory-Architectur

When I make tutorials or give reports I like displaying all the files and directories of a project like a cascade. These can be cumbersome to type by hand and so I wrote a small script to generate these automatically, a bit like [tree](http://linux.die.net/man/1/tree).

## Usage

### Basic

```sh
./probe example/
```

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

By doing this a markdown file called ``architecture.md`` is saved into the directory that is probed. It ressembles the example above. You can use both absolute and relative paths. You don't have to worry about the `/` at the end.

### Ignoring files with certain extensions

```sh
./probe example/ -i js css
```

    example
    ├───┐ static
    │   ├───┐ js
    │   ├───┐ data
    │   │   └─── Toulouse.csv
    │   └───┐ css
    │       └─── Leaflet.vector-markers.css.map
    ├───┐ lib
    │   ├─── __init__.py
    │   └─── JCDecaux.py
    ├───┐ templates
    │   └─── index.html
    ├─── serve.py
    ├─── architecture.md
    └─── update.py

### Probing to a certain level

```sh
./probe example/ -d 0
```
    example
    ├───┐ static
    ├───┐ lib
    ├───┐ templates
    ├─── serve.py
    ├─── architecture.md
    └─── update.py

## To do

- Add filter
- Add prety graphics

## Contact

If you want to implement a new feature please feel free to send me a mail (<maxhalford25@gmail.com>) and I'll be glad to discuss/help.

[Reddit thread](http://www.reddit.com/r/Python/comments/3b2gw1/probing_a_directory_to_extract_the_architecture/)