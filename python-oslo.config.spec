%define module oslo_config
%define oname oslo-config

Name:		python-oslo.config
Version:	10.6.0
Release:	1
Summary:	Oslo Configuration API
License:	None
Group:		Development/Python
URL:		https://pypi.org/project/oslo.config/
Source0:	https://files.pythonhosted.org/packages/source/o/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pbr)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
Oslo Configuration API

%files
%{_bindir}/%{oname}-{generator,validator}
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info
