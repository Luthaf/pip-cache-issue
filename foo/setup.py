import os

from setuptools import setup


ROOT = os.path.realpath(os.path.dirname(__file__))
FOO_BAR_SRC = os.path.realpath(os.path.join(ROOT, "..", "foo-bar"))
FOO_BAR_NO_DASH_SRC = os.path.realpath(os.path.join(ROOT, "..", "foo_bar"))


if __name__ == "__main__":
    extras_require = {}
    if os.path.exists(FOO_BAR_SRC):
        # we are building from a git checkout
        extras_require["bar"] = f"foo-bar @ file://{FOO_BAR_SRC}"
        extras_require["bar-no-dash"] = f"foo-bar @ file://{FOO_BAR_NO_DASH_SRC}"
    else:
        # we are building from a sdist/installing from a wheel
        extras_require["bar"] = "foo-bar"
        extras_require["bar-no-dash"] = "foo-bar"

    setup(extras_require=extras_require)
