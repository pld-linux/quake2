Summary:	Quake2 for linux
Summary(pl):	Quake2 dla Linuksa
Summary(pt_BR):	Quake2 para Linux
Name:		quake2
Version:	3.20
Release:	1
License:	distributable
Group:		Applications/Games
Group(de):	Applikationen/Spiele
Group(pl):	Aplikacje/Gry
Source0:	ftp://3darchives.in-span.net/pub/idgames/idstuff/quake2/unix/%{name}-%{version}-glibc-i386-unknown-linux2.0.tar.gz
Source1:	%{name}
Source2:	sysconfig.%{name}
Source3:	%{name}.conf
Source4:	%{name}-server.conf
Source5:	%{name}-server
URL:		http://www.idsoftware.com
Requires:	svgalib >= 1.2.13
Requires:	OpenGL
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
#Autoreqprov:	no

%description
Quake2 for linux!

%description -l pl
Quake2 dla Linuksa!

%description -l pt_BR
Quake2 para Linux!

%package server
Summary:	Quake2 server
Summary(pl):	Serwer Quake2
Summary(pt_BR):	Servidor Quake2
Group:		Applications/Games
Group(de):	Applikationen/Spiele
Group(pl):	Aplikacje/Gry
Requires:	%{name} = %{version}

%description
Quake2 server

%description -l pt_BR server
Servidor Quake2

%description -l pl
Serwer Quake2 dla Linuksa

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/quake2/baseq2/players/{crakhor,cyborg,female,male} \
	$RPM_BUILD_ROOT{%{_bindir},/etc/rc.d/init.d,/etc/sysconfig}

for i in crakhor cyborg female male ; do
        install baseq2/players/$i/* $RPM_BUILD_ROOT%{_libdir}/quake2/baseq2/players/$i
done
	
install baseq2/gamei386.so	$RPM_BUILD_ROOT%{_libdir}/quake2/baseq2/gamei386.so
install baseq2/pak2.pak		$RPM_BUILD_ROOT%{_libdir}/quake2/baseq2
install quake2			$RPM_BUILD_ROOT%{_bindir}/quake2id
install lib3dfxgl.so		$RPM_BUILD_ROOT%{_libdir}/quake2
install libMesaGL.so.2.6	$RPM_BUILD_ROOT%{_libdir}/quake2
	
for i in gl glx soft softx ; do
        install ref_$i.so $RPM_BUILD_ROOT%{_libdir}/quake2
done
		
install %{SOURCE1}	$RPM_BUILD_ROOT%{_bindir}/quake2
install %{SOURCE2}	$RPM_BUILD_ROOT/etc/sysconfig/quake2
install %{SOURCE3}	$RPM_BUILD_ROOT%{_sysconfdir}
install %{SOURCE4}	$RPM_BUILD_ROOT%{_libdir}/quake2/baseq2/server.cfg
install %{SOURCE5}	$RPM_BUILD_ROOT/etc/rc.d/init.d/quake2-server

gzip -9nf README readme.txt

%clean
rm -rf $RPM_BUILD_ROOT

%post server
/sbin/chkconfig --add quake2-server
echo "Run \"/etc/rc.d/init.d/quake2 start\" to start Quake2 server." >&2

%preun server
/etc/rc.d/init.d/quake2-server stop >&2

%postun server
if [ "$1" = 0 ]; then
	/sbin/chkconfig --del quake2-server
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/quake2
%attr(755,root,root)%{_bindir}/quake2id
%dir %{_libdir}/quake2
%dir %{_libdir}/quake2/baseq2
%attr(755,root,root) %{_libdir}/quake2/*so*
%attr(755,root,root) %{_libdir}/quake2/baseq2/*so*
%{_libdir}/quake2/baseq2/pak2.pak
%{_libdir}/quake2/baseq2/players
%config /etc/sysconfig/quake2
%config %{_sysconfdir}/quake2.conf
%doc *.gz

%files server
%defattr(644,root,root,755)
%attr(755,games,games) 	/etc/rc.d/init.d/quake2-server
%config %{_libdir}/quake2/baseq2/server.cfg
