Name:		python-oslo.config
Version:	9.7.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/o/oslo.config/oslo.config-%{version}.tar.gz
Summary:	Oslo Configuration API
URL:		https://pypi.org/project/oslo.config/
License:	None
Group:		Development/Python
BuildRequires:	python
BuildRequires:	python%{pyver}dist(pbr)
BuildSystem:	python
BuildArch:	noarch

%description
Oslo Configuration API

%files
%{_bindir}/oslo-config-generator
%{_bindir}/oslo-config-validator
%{py_sitedir}/oslo_config
%{py_sitedir}/oslo.config-*.*-info
