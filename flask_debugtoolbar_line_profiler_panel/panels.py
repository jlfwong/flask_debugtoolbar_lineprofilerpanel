import line_profiler
import functools
import StringIO

import jinja2

from flask_debugtoolbar.panels import DebugPanel

from flask_debugtoolbar_line_profiler_panel.profile import functions_to_profile

class LineProfilerPanel(DebugPanel):
    """
    Panel that displays the result from a line profiler run
    """
    name = 'Line Profiler'

    user_activate = True

    def __init__(self, jinja_env, context={}):
        DebugPanel.__init__(self, jinja_env, context=context)

        self.jinja_env.loader = jinja2.ChoiceLoader([
            self.jinja_env.loader,
            jinja2.PackageLoader(__name__, 'templates')
        ])

        if functions_to_profile:
            self.is_active = True

    def has_content(self):
        return bool(self.profiler)

    def process_request(self, request):
        if not self.is_active:
            return

        self.profiler = line_profiler.LineProfiler()

        for f in functions_to_profile:
            self.profiler.add_function(f)

        self.stats = None

    def process_view(self, request, view_func, view_kwargs):
        if self.is_active:
            return functools.partial(self.profiler.runcall, view_func)

    def process_response(self, request, response):
        if not self.is_active:
            return False

        output = StringIO.StringIO()
        self.profiler.print_stats(output)
        self.stats = output.getvalue()

        return response

    def title(self):
        if not self.is_active:
            return "Profiler not active"

        return 'Line Profiler'

    def nav_title(self):
        return 'Line Profiler'

    def nav_subtitle(self):
        if not self.is_active:
            return "in-active"

        return '%d function(s)' % len(functions_to_profile)

    def url(self):
        return ''

    def content(self):
        if not self.is_active:
            return "The profiler is not activated, activate it to use it"

        context = {
            'stats': self.stats,
        }

        return self.render('content.html', context)
