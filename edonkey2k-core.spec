%define		_ver  45
Summary:	Download file manager (official core)
Summary(pl):	¦ci±gacz plików (oficialny)
Name:		edonkey2k-core
Version:	0.%{_ver}
Release:	2
Epoch:		2
License:	unknown
Group:		Applications/Communications
Source0:	http://www.overnet.com/files/eDonkey%{version}.tar.gz
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

install donkey_s_%{_ver} $RPM_BUILD_ROOT%{_bindir}/edonkey_s_v%{_ver}

ln -s %{_bindir}/edonkey_s_v%{_ver} $RPM_BUILD_ROOT%{_bindir}/edonkey

install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/edonkey-conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
