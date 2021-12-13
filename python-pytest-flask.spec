#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module (built form python3-pytest-flask.spec)

Summary:	A set of py.test fixtures to test Flask applications
Summary(pl.UTF-8):	Zbiór wyposażeń py.test do testowania aplikacji Flaska
Name:		python-pytest-flask
# keep 0.x here for python2 support
Version:	0.15.1
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-flask/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-flask/pytest-flask-%{version}.tar.gz
# Source0-md5:	0fe01a48f5674b63ac736ddbce6f3362
URL:		https://pypi.org/project/pytest-flask/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
BuildRequires:	python-setuptools_scm
%if %{with tests}
BuildRequires:	python-flask
BuildRequires:	python-pytest >= 3.6
BuildRequires:	python-werkzeug >= 0.7
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm
%if %{with tests}
BuildRequires:	python3-flask
BuildRequires:	python3-pytest >= 3.6
BuildRequires:	python3-werkzeug >= 0.7
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python-sphinx_rtd_theme
BuildRequires:	sphinx-pdg-2
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of pytest fixtures to test Flask extensions and applications.

%description -l pl.UTF-8
Zbiór wyposażeń pytesta do testowania rozszerzeń i aplikacji Flaska.

%package -n python3-pytest-flask
Summary:	A set of py.test fixtures to test Flask applications
Summary(pl.UTF-8):	Zbiór wyposażeń py.test do testowania aplikacji Flaska
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-pytest-flask
A set of pytest fixtures to test Flask extensions and applications.

%description -n python3-pytest-flask -l pl.UTF-8
Zbiór wyposażeń pytesta do testowania rozszerzeń i aplikacji Flaska.

%package apidocs
Summary:	API documentation for Python pytest-flask module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona pytest-flask
Group:		Documentation

%description apidocs
API documentation for Python pytest-flask module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona pytest-flask.

%prep
%setup -q -n pytest-flask-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTHONPATH=$(pwd) \
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS="pytest_flask.plugin" \
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd) \
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS="pytest_flask.plugin" \
%{__python3} -m pytest tests
%endif
%endif

%if %{with doc}
PYTHONPATH=$(pwd) \
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-2
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
%doc LICENSE README.rst
%{py_sitescriptdir}/pytest_flask
%{py_sitescriptdir}/pytest_flask-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pytest-flask
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/pytest_flask
%{py3_sitescriptdir}/pytest_flask-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/*
%endif
