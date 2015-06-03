# Markup-Directory

When I make tutorials or give reports I like displaying all the files and directories of a project like a cascade. With markup languages you can create pretty "wells" where this looks good:

	bikes/
        static/
            js/
                Leaflet.vector-markers.min.js
                Leaflet.vector-markers.js
            data/
                Toulouse.csv
            css/
                Leaflet.vector-markers.css
                Leaflet.vector-markers.css.map
        lib/
            __init__.py
            JCDecaux.py
        templates/
            index.html
        serve.py
        update.py

These can be cumbersome to type by hand and so I wrote a small script to generate these automatically. All you have to do is modify the ``directory`` variable in the ``convert.py`` script and run the script. This will produce a markdown script called ``directory.md`` which you can copy paste in any markdown file.

If you want to adapt this for other markup languages (YAML for example) don't hesitate, it shouldn't be too hard! If you can't be bothered and really need it to work for another language send me a mail (**``maxhalford25@gmail.com``**) and I'll add it with pleasure.