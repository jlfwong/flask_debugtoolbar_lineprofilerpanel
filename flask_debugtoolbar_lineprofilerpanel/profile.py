functions_to_profile = []

def line_profile(f):
    """The passed function will be included in the line profile displayed by
    the line profiler panel.

    Can be used either as a decorator or called directly as a function

        # Using it as a decorator
        @app.route('/profile')
        @line_profile
        def profile_page(profile_user_id):
            ...
            return flask.render_template('profile_page')

        # Explicit argument
        line_profile(some_function)
    """
    functions_to_profile.append(f)
    return f
