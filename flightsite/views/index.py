import flightsite
import flask
from flightsite.common.model import check_session


@flightsite.app.route("/")
def show_index():
    """Render  for the site."""

    return flask.render_template("index.html")


@flightsite.app.route("/user/<uname>/")
def show_user(uname):
    """Show profile options for uname."""
    logname = check_session()
    if not logname:
        return flask.redirect("/accounts/login/")

    if logname != uname:
        return flask.abort(403)

    context = {
        "logname": logname
    }

    return flask.render_template("accounts.html", **context)
