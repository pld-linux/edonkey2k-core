Summary:	Download file manager (official core)
Summary(pl):	¦ci±gacz plików (oficjalny)
Name:		edonkey2k-core
Version:	0.51.2
Release:	1
Epoch:		1
License:	unknown
Group:		Applications/Communications
Source0:	http://download.overnet.com/donkey%{version}.tar.gz
# Source0-md5:	f41b09942dc3df66323752997c5fdfa4
Source1:	%{name}.sh
URL:		http://ed2k-gtk-gui.sourceforge.net/core.shtml
Provides:	eDonkey-core
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveArch:	%{ix86}

%description
Download file manager hosted by http://www.edonkey2000.com/

%description -l pl
¦ci±gacz plików z http://www.edonkey2000.com/

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install donkey%{version} $RPM_BUILD_ROOT%{_bindir}/edonkey%{version}

ln -s %{_bindir}/edonkey%{version} $RPM_BUILD_ROOT%{_bindir}/edonkey

install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/edonkey-conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
