%global pypi_name tomli

Name:           python-%{pypi_name}
Version:        2.0.1
Release:        1
Summary:        A little TOML parser for Python
License:        MIT
Group:          Development/Python
URL:            https://pypi.org/project/tomli/
Source0:        https://pypi.io/packages/source/f/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-flit-core

%description
Tomli is a Python library for parsing TOML and is fully compatible with TOML
v1.0.0.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%build
%py_build

%install
%py_install

%files
%doc README.md
%license LICENSE
