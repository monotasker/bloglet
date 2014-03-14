plugin_markmin_extras
=====================

A web2py plugin providing extra syntax for the markmin markup language (a variant of markdown).

Created by Ian W. Scott (monotasker) 
Copyright Ian W. Scott, 2014 
Released under the MIT open-source license (see the included license file)  

Overview
---------

This plugin provides some extra markup that I felt was missing from web2py's markmin syntax. At present it includes:

image_by_title  
: Include an image that has been uploaded and assigned a database record. Rather than using its filename, the image is referenced by the title (or other field from the images table).

audio_by_title  
: Similar to image_by_title, but embeds an audio file (as an html5 audio element). Again, the file is referenced by its title field in a database table dedicated to audio uploads.

doc_by_title 
: Include a link to an upload file, referenced by the title field of the file 
in the db table used to store the uploads. I use it primarily for pdf files, 
but it can be used to link to anything.

In addition to simplifying your workflow with uploads stored in the file system, these additions allow you to use upload files that are stored as binary blobs in a database field. Because the syntax pulls the file from the upload field of a database table, it is agnostic as to the mode of storage.


Installation
-------------

Option 1
_________

Place the modules/plugin_markmin_extras.py file in the modules folder of your application. Done!

Option 2 
_________

Create a new folder in your application for plugins (e.g., plugins/). Clone this github repository into a subfolder of that new plugins directory. Then create a symlink from the modules/plugin_markmin_extras.py file into your main modules/ folder. Using the Unix/Linux command line this can be done like so:

    cd path/to/your/application/modules
    ln -s ../plugins/plugin_markmin_extras/modules/plugin_markmin_extras.py plugin_markmin_extras.py
    
This method has the advantage of allowing you to git pull any changes to this repo directly into your application without having to reinstall anything. For added convenience, if you are using git for version control on your application you can add this plugin repo as a git submodule:

    cd path/to/your/application
    git submodule add git@github.com:monotasker/plugin_markmin_extras.git plugins/plugin_markmin_extras
    
Option 3
_________

Install the compiled plugin file using web2py's built-in plugin installation interface (in the admin interface). At present this would require you to first install the plugin and compile it, since I haven't provided a compiled plugin file for download. Once this plugin matures I will include a compiled plugin file in the repository.


Usage
---------

Once you have installed this plugin in your web2py application, you simply need to import the extra syntax into the file where you will be using it:

    from plugin_markmin_extras import mm_extras 
    
If you are using the markup directly in a view file, remember that this import must come at the top of the file, above an "extend" statements.

When you create your MARKMIN helper object, add mm_extras like this:

    MARKMIN('A content string...', extra=custom_mm)

In your markmin content, use the additional syntax like this:

    ``mygreattitle:``:image_by_title
    ``mygreattitle``:audio_by_title
    ``mygreattitle``:doc_by_title

Note that the double back-ticks surrounding the markup statement are required. This is a constraint of markmin's native syntax for custom extensions.


Configuration
--------------

At the moment you will need to change the table and field names of your media 
records manually in the modules/plugin_markmin_extras.py file. I plan to 
simplify this at some point by using web2py's plugin configuration hooks.
