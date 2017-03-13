Summary:	ASN.1 tools for Python
Name:		python-asn1crypto
Version:	0.21.1
Release:	1
License:	BSD
Group:		Development/Python
Url:		http://github.com/wbond/asn1crypto
Source0:	http://pypi.python.org/pypi/asn1crypto/asn1crypto-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
%rename asn1crypto

%description
This project is dedicated to implementation of ASN.1 types (concrete syntax)
and codecs (transfer syntaxes) for Python programming environment. ASN.1
compiler is planned for implementation in the future.

%package -n python2-asn1crypto
Summary:	ASN.1 tools for Python 2.x
Group:		Development/Python
BuildRequires:	pkgconfig(python)

%description -n python2-asn1crypto
This project is dedicated to implementation of ASN.1 types (concrete syntax)
and codecs (transfer syntaxes) for Python programming environment. ASN.1
compiler is planned for implementation in the future.

%prep
%setup -qn asn1crypto-%{version}
mkdir py2
cp -a `ls |grep -v py2` py2/

%build
cd py2
python2 setup.py build

cd ..
python ./setup.py build

%install
cd py2
python2 setup.py install --root=%{buildroot}

cd ..
python ./setup.py install --root=%{buildroot}

%files
%{python_sitelib}/asn1crypto
%{python_sitelib}/*.egg-info

%files -n python2-asn1crypto
%{python2_sitelib}/asn1crypto
%{python2_sitelib}/*.egg-info
