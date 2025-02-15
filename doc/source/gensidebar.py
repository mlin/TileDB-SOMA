#
# This file generates the sidebar/toctree for all TileDB-SOMA projects and should
# be copied to each project when it is updated.
#
# This file is originally from the RobotPy documentation project
# https://github.com/robotpy/robotpy-docs, licensed under Apache v2.
#

import os


def write_if_changed(fname, contents):

    try:
        with open(fname, "r") as fp:
            old_contents = fp.read()
    except:
        old_contents = ""

    if old_contents != contents:
        with open(fname, "w") as fp:
            fp.write(contents)


def generate_sidebar(conf, conf_api):

    version = conf["rtd_version"]

    lines = [
        "",
        ".. DO NOT MODIFY! THIS PAGE IS AUTOGENERATED!",
        "   To edit the sidebar, modify gensidebar.py and re-build the docs.",
        "",
    ]

    url_base = "https://tiledb-inc-tiledb-soma.readthedocs-hosted.com"
    lang = "en"

    def toctree(name):
        lines.extend(
            [".. toctree::", "    :caption: %s" % name, "    :maxdepth: 1", ""]
        )

    def endl():
        lines.append("")

    def write(desc, link):
        if conf_api == "tiledbsoma":
            args = desc, link
        else:
            args = desc, "%s/%s/%s/%s.html" % (url_base, lang, version, link)

        lines.append("    %s <%s>" % args)

    def write_api(project, desc, rst_page):
        # From non-root project to root project link
        if project == "tiledbsoma" and conf_api != "tiledbsoma":
            args = desc, url_base, lang, version, rst_page
            lines.append("    %s API <%s/%s/%s/%s.html>" % args)
        # From anything to non-root project link
        elif project != conf_api:
            args = desc, url_base, project, lang, version, rst_page
            lines.append("    %s API <%s/projects/%s/%s/%s/%s.html>" % args)
        # Local project link
        else:
            args = desc, rst_page
            lines.append("    %s API <%s>" % args)

    def write_api_url(desc, url):
        lines.append("    %s API <%s>" % (desc, url))

    #
    # Specify the sidebar contents here
    #

    toctree("API Reference")
    write_api("tiledbsoma-py", "Python", "python-api")
    write_api_url("R", "https://tiledb-inc.github.io/TileDB-SOMA/reference/index.html")
    endl()

    write_if_changed("_sidebar.rst.inc", "\n".join(lines))
