# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.meson import MesonPackage

from spack.package import *


class Gitg(MesonPackage):
    """gitg is a graphical user interface for git. It aims at being a small, fast and convenient
    tool to visualize the history of git repositories. Besides visualization, gitg also provides
    several utilities to manage your repository and commit your work."""

    homepage = "https://github.com/GNOME/gitg"
    url = "https://download.gnome.org/sources/gitg/44/gitg-44.tar.xz"

    maintainers("KineticTheory")

    license("GPL-2.0")

    version("44.0.0", sha256="342a31684dab9671cd341bd3e3ce665adcee0460c2a081ddc493cdbc03132530")

    depends_on("c", type="build")

    # depends_on("at-spi2-core", type="build")
    # depends_on("atk", type="build")
    # depends_on("bzip2", type="build")
    # depends_on("cairo", type="build")
    # depends_on("dbus", type="build")
    depends_on("enchant", type="build")
    # depends_on("fixesproto", type="build")
    # depends_on("fontconfig", type="build")
    # depends_on("freetype", type="build")
    # depends_on("fribidi", type="build")
    # depends_on("gdk-pixbuf", type="build")
    depends_on("glib", type="build")
    # depends_on("gobject-introspection", type="build")
    depends_on("gsettings-desktop-schemas", type="build")
    depends_on("gspell", type="build")
    # depends_on("gtkplus", type="build")
    depends_on("gtksourceview", type="build")
    # depends_on("harfbuzz", type="build")
    # depends_on("icu4c", type="build")
    # depends_on("inputproto", type="build")
    # depends_on("kbproto", type="build")
    # depends_on("libepoxy", type="build")
    # depends_on("libffi", type="build")
    depends_on("libgee", type="build")
    depends_on("libgit2-glib", type=("build", "link"))
    # depends_on("libgit2", type="build")
    depends_on("libhandy", type=("build", "link"))
    # depends_on("libjpeg", type="build")
    depends_on("libpeas@:1.36",  type="build")
    # depends_on("libpng", type="build")
    # depends_on("libx11", type="build")git 
    # depends_on("libxau", type="build")
    # depends_on("libxcb", type="build")
    # depends_on("libxdmcp", type="build")
    # depends_on("libxext", type="build")
    # depends_on("libxfixes", type="build")
    # depends_on("libxft", type="build")
    # depends_on("libxi", type="build")
    # depends_on("libxml2", type="build")
    # depends_on("libxrandr", type="build")
    # depends_on("libxrender", type="build")
    # depends_on("libxtst", type="build")
    # depends_on("mesa", type="build")
    # depends_on("ninja", type="build")
    # depends_on("pango", type="build")
    # depends_on("pcre2", type="build")
    # depends_on("pixman", type="build")
    # depends_on("randrproto", type="build")
    # depends_on("recordproto", type="build")
    # depends_on("renderproto", type="build")
    # depends_on("shared-mime-info", type="build")
    depends_on("vala", type="build")
    # depends_on("xextproto", type="build")
    # depends_on("xproto", type="build")
    # depends_on("zlib", type="build")
    depends_on("libsecret", type="build")

    def url_for_version(self, version):
      return f"https://download.gnome.org/sources/gitg/{version.joined}/gitg-{version.joined}.tar.xz"
