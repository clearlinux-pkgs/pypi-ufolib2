#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-ufolib2
Version  : 0.12.1
Release  : 2
URL      : https://files.pythonhosted.org/packages/bd/48/7e3a8ddcdd44ceb1646e9083d1134e6698a44ec6c519e28d00e51353ddaa/ufoLib2-0.12.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/bd/48/7e3a8ddcdd44ceb1646e9083d1134e6698a44ec6c519e28d00e51353ddaa/ufoLib2-0.12.1.tar.gz
Summary  : ufoLib2 is a UFO font processing library.
Group    : Development/Tools
License  : Apache-2.0 MIT OFL-1.1
Requires: pypi-ufolib2-license = %{version}-%{release}
Requires: pypi-ufolib2-python = %{version}-%{release}
Requires: pypi-ufolib2-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pypi(appdirs)
BuildRequires : pypi(attrs)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(wheel)
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
# ufoLib2
ufoLib2 is meant to be a thin representation of the Unified Font Object (UFO) version 3 data model, intended for programmatic manipulation and fast batch processing of UFOs.

%package license
Summary: license components for the pypi-ufolib2 package.
Group: Default

%description license
license components for the pypi-ufolib2 package.


%package python
Summary: python components for the pypi-ufolib2 package.
Group: Default
Requires: pypi-ufolib2-python3 = %{version}-%{release}

%description python
python components for the pypi-ufolib2 package.


%package python3
Summary: python3 components for the pypi-ufolib2 package.
Group: Default
Requires: python3-core
Provides: pypi(ufolib2)
Requires: pypi(attrs)
Requires: pypi(fonttools)

%description python3
python3 components for the pypi-ufolib2 package.


%prep
%setup -q -n ufoLib2-0.12.1
cd %{_builddir}/ufoLib2-0.12.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1638626540
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

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-ufolib2
cp %{_builddir}/ufoLib2-0.12.1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-ufolib2/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/ufoLib2-0.12.1/tests/data/LICENSE_MutatorSans %{buildroot}/usr/share/package-licenses/pypi-ufolib2/f16f6141ff149dc59d7c4007c89c5dfea5145057
cp %{_builddir}/ufoLib2-0.12.1/tests/data/LICENSE_UbuTestData.txt %{buildroot}/usr/share/package-licenses/pypi-ufolib2/81e5605d07c08e95048556f1795931cc038d01e6
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-ufolib2/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
/usr/share/package-licenses/pypi-ufolib2/81e5605d07c08e95048556f1795931cc038d01e6
/usr/share/package-licenses/pypi-ufolib2/f16f6141ff149dc59d7c4007c89c5dfea5145057

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*