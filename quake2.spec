Name:		quake2
Version:	3.20
Release:	1
Summary:	Quake2 for linux
Summary(pl):	Quake2 dla Linuksa
Summary(pt_BR):	Quake2 para Linux
Source0:	ftp://3darchives.in-span.net/pub/idgames/idstuff/quake2/unix/quake2-3.20-glibc-i386-unknown-linux2.0.tar.gz
Source1:	%{name}
Source2:	sysconfig.%{name}
Source3:	%{name}.conf
Source4:	%{name}-server.conf
Source5:	%{name}-server-pl
Copyright:	Distributable
Group:		Applications/Games
Group(de):	Applikationen/Spiele
Group(pl):	Aplikacje/Gry
URL:		http://www.idsoftware.com
Requires:	svgalib >= 1.2.13 Mesa >= 2.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
#Autoreqprov:	no

%description
Quake2 for linux!

%description -l pt_BR
Quake2 para Linux!

%description -l pl
Quake2 dla Linuksa!

%package server
Summary:	Quake2 server
Summary(pl):	Serwer Quake2
Summary(pt_BR):	Servidor Quake2
Group:		Applications/Games
Group(de):	Applikationen/Spiele
Group(pl):	Aplikacje/Gry
Requires:	quake2 = %{version}

%description
Quake2 server

%description -l pt_BR server
Servidor Quake2

%description -l pl
Serwer Quake2 dla Linuksa

%prep

%setup -q -c

%build

%install

rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/quake2/baseq2
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT/etc/rc.d/init.d
install -d $RPM_BUILD_ROOT/etc/sysconfig

install -m755 	baseq2/gamei386.so $RPM_BUILD_ROOT%{_libdir}/quake2/baseq2/gamei386.so
install -m755 	quake2 $RPM_BUILD_ROOT%{_bindir}/quake2id
install -m755 	$RPM_SOURCE_DIR/quake2.conf $RPM_BUILD_ROOT%{_sysconfdir}
install -m755 	$RPM_SOURCE_DIR/quake2-server.conf $RPM_BUILD_ROOT%{_libdir}/quake2/baseq2/server.cfg
install -m755 	$RPM_SOURCE_DIR/quake2-server-pl $RPM_BUILD_ROOT/etc/rc.d/init.d/quake2-server
install -m755 	$RPM_SOURCE_DIR/quake2 $RPM_BUILD_ROOT%{_bindir}/quake2
install 	$RPM_SOURCE_DIR/sysconfig.quake2 $RPM_BUILD_ROOT/etc/sysconfig/quake2

for i in gl soft softx ; do
	install -m755 ref_$i.so $RPM_BUILD_ROOT%{_libdir}/quake2
done

%post server
/sbin/chkconfig --add quake2-server
echo "Run \"/etc/rc.d/init.d/quake2 start\" to start Quake2 server." >&2

%preun server
/etc/rc.d/init.d/quake2-server stop >&2

%postun server
if [ "$1" = 0 ]
then /sbin/chkconfig --del quake2-server
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/quake2
%{_libdir}/quake2/*
%config /etc/sysconfig/quake2
%config %{_sysconfdir}/quake2.conf
%doc readme.linux legal.txt readme.txt

%files server
%defattr(644,root,root,755)
%attr(755,games,games) /etc/rc.d/init.d/quake2-server
%config %{_libdir}/quake2/baseq2/server.cfg

%clean
rm -rf $RPM_BUILD_ROOT
