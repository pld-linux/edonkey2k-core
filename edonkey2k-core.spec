%define		_rel  4
%define		_ver  59
Summary:	Download file manager (unofficial core)
Summary(pl):	¦ci±gacz plików (nieoficialny)
Name:		edonkey2k-core
Version:	%{_ver}.%{_rel}
Release:	1
License:	unknown
Group:		Applications/Communications
Source0:	http://users.aber.ac.uk/tpm01/donkey_s_%{_ver}-%{_rel}-gaps.tar.gz
Source1:	%{name}.sh
URL:		http://ed2k-gtk-gui.sourceforge.net/core.shtml
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

install donkey_s_v%{_ver}-%{_rel}-gaps $RPM_BUILD_ROOT%{_bindir}/edonkey_s_v%{_ver}-%{_rel}-gaps

ln -s %{_bindir}/edonkey_s_v%{_ver}-%{_rel}-gaps $RPM_BUILD_ROOT%{_bindir}/edonkey

install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/edonkey-conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
