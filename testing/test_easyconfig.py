

from cStringIO import StringIO
from easyconfig import EasyConfigParser


def test_bool(mc):
    assert mc.ns.special.sval2 is True


def test_int(mc):
    assert isinstance(mc.ns.general.gval1, int)
    assert mc.ns.general.gval1 == 1


def test_float(mc):
    assert mc.ns.special.sval1 == 2.2


def test_overridden_value(mc):
    assert mc.ns.general.gval2 == 'emma'


def test_sections_property(mc):
    assert set(mc.ns._sections) == {'general', 'special'}


def test_options_property(mc):
    # every sections also contains the ConfigParser's defaults as options!
    assert set(mc.ns.general._options) == {'gval1', 'gval2', 'gval3', 'default1', 'default2'}


def test_section_repr(mc):
    assert repr(mc.ns.general) == """\
<Section 'general'>
	gval1 = 1
	gval2 = emma
	gval3 = tom"""


def test_ns_repr(mc):
    assert repr(mc.ns) == """\
<EasyConfig>
	<defaults>
		default1 = DEFAULT1
		default2 = 2
	<Section 'general'>
		gval1 = 1
		gval2 = emma
		gval3 = tom
	<Section 'special'>
		sval1 = 2.2
		sval2 = True"""


def test_alternative_ns_name():
    m = EasyConfigParser(ns='_')
    m.readfp(StringIO(CONF1))
    assert m._.general.gval1 == 1


def test_section_and_option_with_invalid_attr_name(mc):
    mc.add_section('/cp')
    mc.set('/cp', 'ab.cd', '44')
    assert mc.ns['/cp']['ab.cd'] == 44


def test_modify_option_in_section(mc):
    mc.ns.general.gval1 = 500
    assert mc.get('general', 'gval1') == '500'


def test_add_option_to_section(mc):
    mc.ns.general.newval = True
    assert mc.getboolean('general', 'newval') == True

    mc.ns.general['ax-ut'] = 4.4
    assert mc.getfloat('general', 'ax-ut') == 4.4


def test_add_section(mc):
    mc.ns._add('new')
    assert 'new' in mc.ns._sections


def test_default_values(mc):
    assert mc.ns.defaults.default1 == 'DEFAULT1'
    assert mc.ns.defaults.default2 == 2


###############################################################################
# Config file setup used for unit tests above:

CONF1 = """
[general]
gval1 = 1
gval2 = otto
"""

CONF2 = """
[general]
gval2 = emma
gval3 = tom

[special]
sval1 = 2.2
sval2 = true
"""

def pytest_funcarg__mc(request):
    m = EasyConfigParser({'default1': 'DEFAULT1', 'default2': 2})
    m.readfp(StringIO(CONF1))
    m.readfp(StringIO(CONF2))
    return m
