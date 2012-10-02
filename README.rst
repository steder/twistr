=================================
Twistr
=================================

`Twistr` is a simple wrapper around the Twisted_ projects `twistd` commandline
tool that will restart the server whenever python files change.

---------------------------------
Usage
---------------------------------

From your root project directory (where your `twisted/plugins` folder lives)
launch your service with::

  twistr -n <service>

Or even::

  twistr <service>

Now change a `*.py` file in your current directory and watch your server
magically restart.

---------------------------------
TODO
---------------------------------

 * configurable directory to watch for changes
 * configurable file extensions to watch for changes
 * use filesystem events API(s) to watch for changes

.. _Twisted: http://www.twistedmatrix.com/
