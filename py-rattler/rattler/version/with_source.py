from __future__ import annotations

from typing import Union

from rattler.version import Version


class VersionWithSource:
    """
    Holds a version and the string it was created from. This is useful if
    you want to retain the original string the version was created from.
    This might be useful in cases where you have multiple strings that
    are represented by the same [`Version`] but you still want to be able to
    distinguish them.

    The string `1.1` and `1.01` represent the same version. When you print
    the parsed version though it will come out as `1.1`. You loose the
    original representation. This class stores the original source string,
    which can be accessed by `source` property.
    """

    def __init__(self, version: Union[str, Version]):
        if not isinstance(version, (str, Version)):
            raise TypeError(
                "VersionWithSource constructor received unsupported type "
                f" {type(version).__name__!r} for the `version` parameter"
            )

        if isinstance(version, str):
            self._source = version
            self._version = Version(version)

        if isinstance(version, Version):
            self._source = str(version)
            self._version = version

    @property
    def version(self) -> Version:
        """
        Returns the `Version` from current object.

        Examples
        --------
        >>> v = VersionWithSource("1.01")
        >>> v.version
        Version("1.1")
        >>> v2 = VersionWithSource(v.version)
        >>> v2.version
        Version("1.1")
        """
        return self._version

    @property
    def source(self) -> str:
        """
        Returns the `source` current object was used to create.

        Examples
        --------
        >>> v = VersionWithSource("1.01.01")
        >>> v.source
        '1.01.01'
        """
        return self._source

    def __str__(self) -> str:
        """
        Returns the string representation of the version

        Examples
        --------
        >>> str(VersionWithSource("1.02.3"))
        '1.02.3'
        """
        return self._source

    def __repr__(self) -> str:
        """
        Returns a representation of the version

        Examples
        --------
        >>> VersionWithSource("1.02.3")
        VersionWithSource("1.02.3")
        """
        return f'{type(self).__name__}("{self.__str__()}")'
