%define module tomli

Name:		python-tomli
Version:	2.4.1
Release:	1
Summary:	A little TOML parser for Python
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/tomli/
Source0:	https://pypi.io/packages/source/t/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	python%{pyver}dist(flit-core)
BuildRequires:  python%{pyver}dist(pip)

%description
Tomli is a Python library for parsing TOML. Version 2.4.0 and later are
compatible with TOML v1.1.0. Older versions are TOML v1.0.0 compatible.

%prep
%autosetup -p1 -n %{module}-%{version}

%build
%py_build

%install
%py_install

%files
%doc README.md
%license LICENSE
%{py_puresitedir}/%{module}
%{py_puresitedir}/%{module}-%{version}.dist-info
