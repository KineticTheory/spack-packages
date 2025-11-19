# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.meson import MesonPackage

from spack.package import *


class Libpeas(MesonPackage):
    """libpeas is a gobject-based plugins engine, and is targeted at giving every application the
    chance to assume its own extensibility. It is currently used by several Gnome applications like
    gedit and Totem.

    It takes its roots in the old gedit plugins engine, and provides an extensive set of features
    mirroring the desiderata of most of the applications providing an extension framework."""

    homepage = "https://gitlab.gnome.org/GNOME/libpeas"
    url = "https://download.gnome.org/sources/libpeas/2.2/libpeas-2.2.0.tar.xz"
    git = "https://gitlab.gnome.org/GNOME/libpeas.git"
    
    maintainers("KineticTheory")
    
    license("GNU LGPL-2.1")

    version("2.2.0", sha256="c2887233f084a69fabfc7fa0140d410491863d7050afb28677f9a553b2580ad9")
    version("1.36.0", sha256="297cb9c2cccd8e8617623d1a3e8415b4530b8e5a893e3527bbfd1edd13237b4c")

    depends_on("c", type="build")

    depends_on("glib@2.54:", type=("build", "link", "run"))
    depends_on("gobject-introspection", type=("build", "link", "run"))
    depends_on("gjs", type=("build", "link", "run"))
    depends_on("gjs@:1.80", type=("build", "link", "run"), when="@:1.36")
    depends_on("py-pygobject", type="build")
    depends_on("vala", type="build")

    def url_for_version(self, version):
      return f"https://download.gnome.org/sources/libpeas/{version.up_to(2)}/libpeas-{version}.tar.xz"

    def meson_args(self):
        return ["-Dlua51=false"]
