Line Profile Panel for Flask Debug Toolbar
==========================================

This is a panel for `flask_debugtoolbar`_ which enables the ability to view 
line profiling information from selected functions.

The line profile information comes from the `line_profiler`_ module, but you 
don't need to worry about that.

Installation
------------

First, you need to get the package. Install it with pip:

::

    pip install flask-debugtoolbar-lineprofilerpanel

Somewhere after you've set ``app.debug = True`` and before ``app.run``, you need
to specify the ``flask_debugtoolbar`` panels that you want to use and include
``'flask_debugtoolbar_lineprofilerpanel.panels.LineProfilerPanel'`` in that
list.

For example, here's a small flask app with the panel installed and with line 
profiling enabled for the `hello_world`:

::

    from flask import Flask
    app = Flask(__name__)

    import flask_debugtoolbar

    from flask_debugtoolbar_lineprofilerpanel.profile import line_profile

    @app.route('/')
    @line_profile
    def hello_world():
        return flask.render_template('hello_world.html')

    if __name__ == '__main__':
        app.debug = True

        # Specify the debug panels you want
        app.config['DEBUG_TB_PANELS'] = [
            'flask_debugtoolbar.panels.versions.VersionDebugPanel',
            'flask_debugtoolbar.panels.timer.TimerDebugPanel',
            'flask_debugtoolbar.panels.headers.HeaderDebugPanel',
            'flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
            'flask_debugtoolbar.panels.template.TemplateDebugPanel',
            'flask_debugtoolbar.panels.sqlalchemy.SQLAlchemyDebugPanel',
            'flask_debugtoolbar.panels.logger.LoggingPanel',
            'flask_debugtoolbar.panels.profiler.ProfilerDebugPanel',
            # Add the line profiling
            'flask_debugtoolbar_lineprofilerpanel.panels.LineProfilerPanel'
        ]
        toolbar = flask_debugtoolbar.DebugToolbarExtension(app)

        app.run()


Usage
-----

Unlike the regular profile panel that comes with ``flask_debugtoolbar``, the
line profiler will only profile functions you specifically tell it to. You can
either use it as a decorator or directly as a function.

::

    from flask_debugtoolbar_lineprofilerpanel.profile import line_profile

    # Using it as a decorator
    @app.route('/profile')
    @line_profile
    def profile_page():
        ...
        return flask.render_template('profile_page')

    # Explicit argument
    line_profile(some_function)

Note that if I had done ``line_profile(profile_page)`` in the example above, it
would've profiled the wrapper created by ``app.route``. In general, you probably
just want to use ``line_profile`` as a decorator.

.. _`flask_debugtoolbar`: https://github.com/mgood/flask-debugtoolbar
.. _`line_profiler`: https://github.com/certik/line_profiler
