from flake8_plugin_utils import assert_error, assert_not_error

from flake8_super.plugin import SuperPluginError, SuperPluginVisitor

code_with_error = """
class Y:
  def __init__():
    super(Y, self).__init__()
    some_method()
"""


def test_code_with_error():
    assert_error(SuperPluginVisitor, code_with_error, SuperPluginError)


code_without_error = """
class Y:
  def __init__():
    super().__init__()
    some_method()
"""


def test_code_without_error():
    assert_not_error(SuperPluginVisitor, code_without_error)
