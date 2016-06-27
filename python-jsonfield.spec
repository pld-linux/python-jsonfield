#
# Conditional build:
%bcond_without	doc	# don't build doc
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module		jsonfield
%define 	egg_name	jsonfield
%define		pypi_name	jsonfield
Summary:	A reusable JSONField model for Django to store ad-hoc data
Name:		python-%{pypi_name}
Version:	1.0.3
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/j/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	a7c7df31627069a97c9ba91b599c0845
URL:		https://github.com/bradjasper/django-jsonfield/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-devel
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
django-jsonfield is a reusable Django field that allows you to store
validated JSON in your model.

It silently takes care of serialization. To use, simply add the field
to one of your models.

%package -n python3-%{pypi_name}
Summary:	A reusable JSONField model for Django to store ad-hoc data
Group:		Libraries/Python

%description -n python3-%{pypi_name}
django-jsonfield is a reusable Django field that allows you to store
validated JSON in your model.

It silently takes care of serialization. To use, simply add the field
to one of your models.

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install
%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT


%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif
