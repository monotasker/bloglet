# plugin_comments

Copyright Ian W. Scott, 2012 (scottianw@gmail.com) Licensed as free software under the GPL 3.0 license.

## Overview

A simplet plugin for the web2py framework, providing an ajax comment widget with some passive spam prevention

## Use

Where you want the widget to appear, simply add the following to your web2py template:

    {{=LOAD('plugin_comments', 'widget.load', args=request.args, vars=request.vars, ajax=False, ajax_trap=True)}} 

Note that this snippet passes the arguments and variables from the parent view on to the plugin_comments controller. If you do not want this, simply replace request.args with a list of arguments and replace request.vars with a dictionary of variables.

## Installation

- create folder appname/plugins
- place plugin_comments folder in this new plugins folder
- create symlinks from plugin files to application directories:

    ```bash
    cd [web2py_folder]/applications/myapp  
    ln -s ../plugins/plugin_comments/controllers/plugin_comments.py controllers/plugin_comments.py  
    ln -s ../plugins/plugin_comments/models/plugin_comments.py models/plugin_comments.py  
    ln -s ../plugins/plugin_comments/views/plugin_comments views/plugin_comments
    ```  

*note that the relative addresses allow the symbolic links to work even across systems where the web2py directory is in different locations.*