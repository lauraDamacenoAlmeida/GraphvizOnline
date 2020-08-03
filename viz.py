import sys
import requests
from IPython.display import display, Javascript, HTML
import json

import os
import os.path
import pkgutil

css = pkgutil.get_data(__name__,'index.css.html').decode('utf-8')
js = pkgutil.get_data(__name__,'viz.js').decode('utf-8')

display(Javascript(data=js))
display(HTML(data=css))

# cwd = os.getcwd()
# notebooks_folder_location = cwd.rfind("/notebooks")
# project_folder = cwd[:notebooks_folder_location]
# print(project_folder)
# if os.path.isdir(project_folder):
#     print('dev-mode detected:' + project_folder)
#     # display(Javascript("require.config({paths: {d3: 'https://cdnjs.cloudflare.com/ajax/libs/d3/4.13.0/d3.min'}});"))
#     display(Javascript(filename=project_folder + "viz.css.html"))
# else:
#     #print('production-mode detected:')
#     print(__package__)
#     flowchart_js = pkgutil.get_data(__package__, 'viz.js').decode('utf-8')
#     # display(Javascript("require.config({paths: {d3: 'https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.17/d3.min'}});"))
#     display(Javascript(data=flowchart_js))
#     display(HTML(data=flowchart_css))
# def draw_flowchart():
#  display(Javascript("""
#     (   function(element){
#         require(['viz'], function(viz) {
#             viz(element.get(0), %s)
#         });
#     })(element);
#     """ % ()))
def draw(data):
 display(Javascript("""
    (   function(element){
        require(['viz'], function(viz) {
            viz(element.get(0), %s)
        });
    })(element);
    """ % (json.dumps(data))))

