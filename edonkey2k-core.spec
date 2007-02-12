Summary:	Download file manager (official core)
Summary(pl.UTF-8):	Ściągacz plików (oficjalny)
Name:		edonkey2k-core
Version:	0.50.1
Release:	1
Epoch:		1
License:	unknown
Group:		Applications/Communications
Source0:	http://download.overnet.com/donkey%{version}.tar.gz
# Source0-md5:	dcda1d56faf30e63765d4206faff1168
Source1:	%{name}.sh
URL:		http://ed2k-gtk-gui.sourceforge.net/core.shtml
Provides:	eDonkey-core
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveArch:	%{ix86}

%description
Download file manager hosted by http://www.edonkey2000.com/

%description -l pl.UTF-8
Ściągacz plików z http://www.edonkey2000.com/

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

%post
echo""
echo "Please type edonkey-conf, when you'll be logged as user"
echo "It will prepare your donkey to use with ed2k :)"
echo ""
echo "You may also type overnet-conf, it will prepare overnet-core"
echo "to use with ed2k, more info at http://www.overnet.com/"
echo ""

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
