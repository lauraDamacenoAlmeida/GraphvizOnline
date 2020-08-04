import sys
from IPython.display import display, Javascript, HTML
import json

import os
import os.path
import pkgutil

css = pkgutil.get_data(__name__,'index.css.html').decode('utf-8')
js = pkgutil.get_data(__name__,'viz.js').decode('utf-8')

display(Javascript(data=js))
display(HTML(data=css))

def draw(data):
 display(Javascript("""
    (   function(element){
        require(['viz'], function(viz) {
            viz(element.get(0), %s)
        });
    })(element);
    """ % (json.dumps(data))))

