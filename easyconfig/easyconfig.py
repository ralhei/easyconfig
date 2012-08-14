"""
EasyConfig module
"""

from ConfigParser import SafeConfigParser, NoSectionError


class Section(object):
    def __init__(self, configParser, sectionName):
        self.__dict__['_Section__configParser'] = configParser
        self.__dict__['_name'] = sectionName

    def __getattr__(self, optionName):
        try:
            return self.__configParser.getint(self._name, optionName)
        except ValueError:
            pass
        try:
            return self.__configParser.getfloat(self._name, optionName)
        except ValueError:
            pass
        try:
            return self.__configParser.getboolean(self._name, optionName)
        except ValueError:
            pass
        return self.__configParser.get(self._name, optionName)

    def __getitem__(self, optionName):
        return getattr(self, optionName)

    def __setattr__(self, optionName, value):
        self.__configParser.set(self._name, optionName, str(value))

    def __setitem__(self, optionName, value):
        setattr(self, optionName, value)

    @property
    def _options(self):
        return self.__configParser.options(self._name)

    def __repr__(self):
        return self._repr()


class DefaultsSection(object):
    def __init__(self, configParser):
        self.__configParser = configParser
        self._name = 'defaults'

    def __getattr__(self, attr):
        return self.__configParser.defaults()[attr]

    def __item__(self, attr):
        return self.__configParser.defaults()[attr]

    @property
    def _options(self):
        return self.__configParser.defaults().keys()


class EasyConfig(object):
    def __init__(self, configParser):
        self.__configParser = configParser

    def __getattr__(self, sectionName):
        if self.__configParser.has_section(sectionName):
            return Section(self.__configParser, sectionName)
        else:
            raise NoSectionError("No section: '%s'" % sectionName)

    def __getitem__(self, sectionName):
        return getattr(self, sectionName)

    @property
    def _sections(self):
        return self.__configParser.sections()

    @property
    def defaults(self):
        return DefaultsSection(self.__configParser)

    def _add(self, sectionName):
        self.__configParser.add_section(sectionName)


class EasyConfigParser(SafeConfigParser):
    def __init__(self, *args, **kw):
        self.__ns = ns = kw.pop('ns', 'ns')
        setattr(self, ns, EasyConfig(self))
        # ConfigParser is of type old-style class, so 'super' cannot be used!
        SafeConfigParser.__init__(self, *args, **kw)
