%global pypi_name tomli

Name:           python-%{pypi_name}
Version:        2.0.0
Release:        %mkrel 2
Summary:        A little TOML parser for Python
License:        MIT
Group:          Development/Python
URL:            https://pypi.org/project/tomli/
Source0:        %{pypi_source}
BuildArch:      noarch
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-flit-core

%description
Tomli is a Python library for parsing TOML and is fully compatible with TOML
v1.0.0.

%package -n python3-tomli
Summary:          A little TOML parser for Python
Group:            Development/Python

%description -n python3-tomli
Tomli is a Python library for parsing TOML and is fully compatible with TOML
v1.0.0.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
