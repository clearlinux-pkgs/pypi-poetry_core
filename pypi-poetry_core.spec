#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-poetry_core
Version  : 1.4.0
Release  : 16
URL      : https://files.pythonhosted.org/packages/ba/80/373557c83c79d0cc7add2c123be04c29d81b0ac3e631257d8d7dc0a3cf9c/poetry_core-1.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/ba/80/373557c83c79d0cc7add2c123be04c29d81b0ac3e631257d8d7dc0a3cf9c/poetry_core-1.4.0.tar.gz
Summary  : Poetry PEP 517 Build Backend
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause MIT Python-2.0
Requires: pypi-poetry_core-license = %{version}-%{release}
Requires: pypi-poetry_core-python = %{version}-%{release}
Requires: pypi-poetry_core-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
# Poetry Core
[![PyPI version](https://img.shields.io/pypi/v/poetry-core)](https://pypi.org/project/poetry-core/)
[![Python Versions](https://img.shields.io/pypi/pyversions/poetry-core)](https://pypi.org/project/poetry-core/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![](https://github.com/python-poetry/poetry-core/workflows/Tests/badge.svg)](https://github.com/python-poetry/poetry-core/actions?query=workflow%3ATests)

%package license
Summary: license components for the pypi-poetry_core package.
Group: Default

%description license
license components for the pypi-poetry_core package.


%package python
Summary: python components for the pypi-poetry_core package.
Group: Default
Requires: pypi-poetry_core-python3 = %{version}-%{release}

%description python
python components for the pypi-poetry_core package.


%package python3
Summary: python3 components for the pypi-poetry_core package.
Group: Default
Requires: python3-core
Provides: pypi(poetry_core)

%description python3
python3 components for the pypi-poetry_core package.


%prep
%setup -q -n poetry_core-1.4.0
cd %{_builddir}/poetry_core-1.4.0
pushd ..
cp -a poetry_core-1.4.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1669140230
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-poetry_core
cp %{_builddir}/poetry_core-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-poetry_core/aa1d60525fded9648cab0e59a4338652671ad600 || :
cp %{_builddir}/poetry_core-%{version}/src/poetry/core/_vendor/attrs/LICENSE %{buildroot}/usr/share/package-licenses/pypi-poetry_core/243e9dd038d3d68c67d42c0c4ba80622c2a56246 || :
cp %{_builddir}/poetry_core-%{version}/src/poetry/core/_vendor/jsonschema/COPYING %{buildroot}/usr/share/package-licenses/pypi-poetry_core/2de1a0a3674903238a664ace5d3acc66a7d546c7 || :
cp %{_builddir}/poetry_core-%{version}/src/poetry/core/_vendor/packaging/LICENSE.APACHE %{buildroot}/usr/share/package-licenses/pypi-poetry_core/598f87f072f66e2269dd6919292b2934dbb20492 || :
cp %{_builddir}/poetry_core-%{version}/src/poetry/core/_vendor/packaging/LICENSE.BSD %{buildroot}/usr/share/package-licenses/pypi-poetry_core/fdc0e4eabc45522b079deff7d03d70528d775dc0 || :
cp %{_builddir}/poetry_core-%{version}/src/poetry/core/_vendor/pyparsing/LICENSE %{buildroot}/usr/share/package-licenses/pypi-poetry_core/df156c6a0a89ed2a3bd4a473c68cf85907509ca0 || :
cp %{_builddir}/poetry_core-%{version}/src/poetry/core/_vendor/pyrsistent/LICENSE.mit %{buildroot}/usr/share/package-licenses/pypi-poetry_core/4fdb72bba2df212e4c64c262eaebc0c2ac87cb6d || :
cp %{_builddir}/poetry_core-%{version}/src/poetry/core/_vendor/tomlkit/LICENSE %{buildroot}/usr/share/package-licenses/pypi-poetry_core/84661790a5df00ab944c2d37978d6ce5ac88e554 || :
cp %{_builddir}/poetry_core-%{version}/src/poetry/core/_vendor/typing_extensions.LICENSE %{buildroot}/usr/share/package-licenses/pypi-poetry_core/f456f46e1dcbc636c8451a46426568705fe98a98 || :
cp %{_builddir}/poetry_core-%{version}/tests/masonry/builders/fixtures/case_sensitive_exclusions/LICENSE %{buildroot}/usr/share/package-licenses/pypi-poetry_core/84661790a5df00ab944c2d37978d6ce5ac88e554 || :
cp %{_builddir}/poetry_core-%{version}/tests/masonry/builders/fixtures/complete/LICENSE %{buildroot}/usr/share/package-licenses/pypi-poetry_core/84661790a5df00ab944c2d37978d6ce5ac88e554 || :
cp %{_builddir}/poetry_core-%{version}/tests/masonry/builders/fixtures/default_src_with_excluded_data/LICENSE %{buildroot}/usr/share/package-licenses/pypi-poetry_core/84661790a5df00ab944c2d37978d6ce5ac88e554 || :
cp %{_builddir}/poetry_core-%{version}/tests/masonry/builders/fixtures/default_with_excluded_data/LICENSE %{buildroot}/usr/share/package-licenses/pypi-poetry_core/84661790a5df00ab944c2d37978d6ce5ac88e554 || :
cp %{_builddir}/poetry_core-%{version}/tests/masonry/builders/fixtures/default_with_excluded_data_toml/LICENSE %{buildroot}/usr/share/package-licenses/pypi-poetry_core/84661790a5df00ab944c2d37978d6ce5ac88e554 || :
cp %{_builddir}/poetry_core-%{version}/tests/masonry/builders/fixtures/exclude_nested_data_toml/LICENSE %{buildroot}/usr/share/package-licenses/pypi-poetry_core/84661790a5df00ab944c2d37978d6ce5ac88e554 || :
cp %{_builddir}/poetry_core-%{version}/tests/masonry/builders/fixtures/invalid_case_sensitive_exclusions/LICENSE %{buildroot}/usr/share/package-licenses/pypi-poetry_core/84661790a5df00ab944c2d37978d6ce5ac88e554 || :
cp %{_builddir}/poetry_core-%{version}/tests/masonry/builders/fixtures/licenses_and_copying/LICENSE %{buildroot}/usr/share/package-licenses/pypi-poetry_core/84661790a5df00ab944c2d37978d6ce5ac88e554 || :
cp %{_builddir}/poetry_core-%{version}/tests/masonry/builders/fixtures/with-include/LICENSE %{buildroot}/usr/share/package-licenses/pypi-poetry_core/84661790a5df00ab944c2d37978d6ce5ac88e554 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-poetry_core/243e9dd038d3d68c67d42c0c4ba80622c2a56246
/usr/share/package-licenses/pypi-poetry_core/2de1a0a3674903238a664ace5d3acc66a7d546c7
/usr/share/package-licenses/pypi-poetry_core/4fdb72bba2df212e4c64c262eaebc0c2ac87cb6d
/usr/share/package-licenses/pypi-poetry_core/598f87f072f66e2269dd6919292b2934dbb20492
/usr/share/package-licenses/pypi-poetry_core/84661790a5df00ab944c2d37978d6ce5ac88e554
/usr/share/package-licenses/pypi-poetry_core/aa1d60525fded9648cab0e59a4338652671ad600
/usr/share/package-licenses/pypi-poetry_core/df156c6a0a89ed2a3bd4a473c68cf85907509ca0
/usr/share/package-licenses/pypi-poetry_core/f456f46e1dcbc636c8451a46426568705fe98a98
/usr/share/package-licenses/pypi-poetry_core/fdc0e4eabc45522b079deff7d03d70528d775dc0

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
