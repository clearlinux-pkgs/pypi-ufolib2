#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-ufolib2
Version  : 0.13.1
Release  : 9
URL      : https://files.pythonhosted.org/packages/c4/d8/f0f1e77b7faf69d147d0263b4cbf181b3f9c979c3ad7abb8235e3bf5a8bc/ufoLib2-0.13.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/c4/d8/f0f1e77b7faf69d147d0263b4cbf181b3f9c979c3ad7abb8235e3bf5a8bc/ufoLib2-0.13.1.tar.gz
Summary  : ufoLib2 is a UFO font processing library.
Group    : Development/Tools
License  : Apache-2.0 MIT OFL-1.1
Requires: pypi-ufolib2-license = %{version}-%{release}
Requires: pypi-ufolib2-python = %{version}-%{release}
Requires: pypi-ufolib2-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(appdirs)
BuildRequires : pypi(attrs)
BuildRequires : pypi(cattrs)
BuildRequires : pypi(fonttools)
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(wheel)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

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
Requires: pypi(appdirs)
Requires: pypi(attrs)
Requires: pypi(cattrs)
Requires: pypi(fonttools)

%description python3
python3 components for the pypi-ufolib2 package.


%prep
%setup -q -n ufoLib2-0.13.1
cd %{_builddir}/ufoLib2-0.13.1
pushd ..
cp -a ufoLib2-0.13.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656364894
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
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-ufolib2
cp %{_builddir}/ufoLib2-0.13.1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-ufolib2/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/ufoLib2-0.13.1/tests/data/LICENSE_MutatorSans %{buildroot}/usr/share/package-licenses/pypi-ufolib2/f16f6141ff149dc59d7c4007c89c5dfea5145057
cp %{_builddir}/ufoLib2-0.13.1/tests/data/LICENSE_UbuTestData.txt %{buildroot}/usr/share/package-licenses/pypi-ufolib2/81e5605d07c08e95048556f1795931cc038d01e6
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
/usr/share/package-licenses/pypi-ufolib2/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
/usr/share/package-licenses/pypi-ufolib2/81e5605d07c08e95048556f1795931cc038d01e6
/usr/share/package-licenses/pypi-ufolib2/f16f6141ff149dc59d7c4007c89c5dfea5145057

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
