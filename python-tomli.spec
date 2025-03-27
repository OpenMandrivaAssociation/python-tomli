%global pypi_name tomli

Name:           python-%{pypi_name}
Version:        2.2.1
Release:        1
Summary:        A little TOML parser for Python
License:        MIT
Group:          Development/Python
URL:            https://pypi.org/project/tomli/
Source0:        https://pypi.io/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-flit-core
BuildRequires:  python-pip

%description
Tomli is a Python library for parsing TOML and is fully compatible with TOML
v1.0.0.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%build
mkdir wheels
pip wheel --wheel-dir wheels --no-deps --no-build-isolation --verbose .

%install
pip install --root=%{buildroot} --no-deps --verbose --ignore-installed --no-warn-script-location --no-index --no-cache-dir --find-links wheels wheels/*.whl

%files
%doc README.md
%license LICENSE
%{py_puresitedir}/tomli-*.dist-info
%{py_puresitedir}/tomli
