#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

Summary:	A set of py.test fixtures to test Flask applications
Summary(pl.UTF-8):	Zbiór wyposażeń py.test do testowania aplikacji Flaska
Name:		python3-pytest-flask
Version:	1.2.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-flask/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-flask/pytest-flask-%{version}.tar.gz
# Source0-md5:	87bbbfa7e2f3a9f4c2254bd098b80530
URL:		https://pypi.org/project/pytest-flask/
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm
%if %{with tests}
BuildRequires:	python3-flask
BuildRequires:	python3-pytest >= 3.6
BuildRequires:	python3-werkzeug >= 0.7
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-sphinx_rtd_theme
BuildRequires:	sphinx-pdg-3
%endif
Requires:	python3-modules >= 1:3.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of pytest fixtures to test Flask extensions and applications.

%description -l pl.UTF-8
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
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd) \
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS="pytest_flask.plugin" \
%{__python3} -m pytest tests
%endif

%if %{with doc}
PYTHONPATH=$(pwd) \
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/pytest_flask
%{py3_sitescriptdir}/pytest_flask-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,*.html,*.js}
%endif
