Summary:	Quake2 for linux
Summary(pl):	Quake2 dla Linuksa
Summary(pt_BR):	Quake2 para Linux
Name:		quake2
Version:	3.21
Release:	2
License:	GPL (for code only)
Group:		Applications/Games
Source0:	ftp://ftp.idsoftware.com/idstuff/source/q2source-%{version}.zip
Source1:	%{name}-scripts.tgz
Source2:	%{name}.sysconfig
Source3:	%{name}.conf
Source4:	%{name}-server.conf
Source5:	%{name}-server
URL:		http://www.idsoftware.com/games/quake/quake2/
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel
BuildRequires:	svgalib-devel
BuildRequires:	unzip
Requires:	%{name}-renderer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gamedir	/usr/lib/games/quake2
%define		_gamedatadir	/usr/share/games/quake2
%description
Quake2 for linux!

%description -l pl
Quake2 dla Linuksa!

%description -l pt_BR
Quake2 para Linux!

%package svgalib
Summary:	Quake2 for SVGAlib
Summary(pl):	Biblioteki Quake2 dla SVGAlib
Group:		Applications/Games
Requires:	%{name} = %{version}
Provides:	%{name}-renderer

%description svgalib
Quake2 libraries for SVGAlib play.

%description svgalib -l pl
Biblioteki Quake2 do grania na SVGAlib.

%package software-X11
Summary:	Quake2 X11 software renderer libs
Summary(pl):	Biblioteka Quake2 - programowe renderowanie
Group:		Applications/Games
Requires:	%{name} = %{version}
Provides:	%{name}-renderer

%description software-X11
Play Quake2 using software X11 renderer.

%description software-X11 -l pl
Zagraj w Quake2 przy u¿yciu programowego renderowania w X11.

%package Mesa3D
Summary:	Quake2 X11 Mesa renderer libs
Summary(pl):	Biblioteka Mesa dla Quake2
Group:		Applications/Games
Requires:	%{name} = %{version}
Provides:	%{name}-renderer

%description Mesa3D
Play Quake2 using Mesa3D software acceleration.

%description Mesa3D -l pl
Zagraj w Quake2 przy u¿yciu programowego renderowania Mesa3D.

%package 3DFX
Summary:	Quake2 3DFX libs
Summary(pl):	Biblioteki 3DFX dla Quake2
Group:		Applications/Games
Requires:	%{name} = %{version}
Provides:	%{name}-renderer

%description 3DFX
Play Quake2 using 3DFX acceleration.

%description 3DFX -l pl
Zagraj w Quake2 z akceleracj± 3DFX.

%package GLX
Summary:	OpenGL Quake2
Summary(pl):	Quake2 OpenGL
Group:		Applications/Games
Requires:	%{name} = %{version}
Requires:	OpenGL
Provides:	%{name}-renderer

%description GLX
Play Quake2 using hardware OpenGL acceleration.

%description GLX -l pl
Zagraj w Quake2 ze sprzêtow± akceleracj± OpenGL.

%package server
Summary:	Quake2 server
Summary(pl):	Serwer Quake2
Summary(pt_BR):	Servidor Quake2
Group:		Applications/Games
Requires:	%{name} = %{version}

%description server
Quake2 server.

%description server -l pl
Serwer Quake2 dla Linuksa.

%description server -l pt_BR
Servidor Quake2.

%prep
%setup -q -c
mv -f %{name}-%{version}/* .

%build
cat linux/Makefile | tr -d '\015' > Makefile.tmp
mv -f Makefile.tmp linux/Makefile

%{__make} build_release -C linux \
	RELEASE_CFLAGS="-Dstricmp=strcasecmp %{rpmcflags} -ffast-math %{!?debug:-fomit-frame-pointer}" \
	MESA_DIR=/usr/X11R6

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},/etc/rc.d/init.d,/etc/sysconfig}
install -d $RPM_BUILD_ROOT{%{_gamedir}/baseq2,%{_gamedatadir}/baseq2}

#$RPM_BUILD_ROOT%{_gamedir}/baseq2/players/{crakhor,cyborg,female,male}

#for i in crakhor cyborg female male ; do
#        install baseq2/players/$i/* $RPM_BUILD_ROOT%{_gamedir}/baseq2/players/$i
#done
#install baseq2/pak2.pak		$RPM_BUILD_ROOT%{_gamedir}/quake2/baseq2

cd linux/releasei386-glibc

install gamei386.so $RPM_BUILD_ROOT%{_gamedir}/baseq2
install quake2 $RPM_BUILD_ROOT%{_bindir}/quake2id
install ref_*.so $RPM_BUILD_ROOT%{_gamedir}

install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/quake2
install %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}
install %{SOURCE4} $RPM_BUILD_ROOT%{_gamedir}/baseq2/server.cfg
install %{SOURCE5} $RPM_BUILD_ROOT/etc/rc.d/init.d/quake2-server

ln -sf %{_gamedir}/baseq2/gamei386.so $RPM_BUILD_ROOT%{_gamedatadir}/baseq2/gamei386.so

cd $RPM_BUILD_ROOT%{_bindir} ; tar zxfv %{SOURCE1}

%clean
rm -rf $RPM_BUILD_ROOT

%post server
/sbin/chkconfig --add quake2-server
if [ -f /var/lock/subsys/quake2-server ]; then
	/etc/rc.d/init.d/quake2-server restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/quake2-server start\" to start Quake2 server."
fi

%preun server
if [ "$1" = "0" ]; then
	/etc/rc.d/init.d/quake2-server stop 1>&2
	/sbin/chkconfig --del quake2-server
fi

%files
%defattr(644,root,root,755)
%doc *hanges.txt readme.txt linux/README linux/README-3.21-RELEASE
%attr(755,root,root)%{_bindir}/quake2id
%dir %{_gamedir}
%dir %{_gamedir}/baseq2
%attr(755,root,root) %{_gamedir}/baseq2/gamei386.so
#%{_gamedir}/baseq2/pak2.pak
#%{_gamedir}/baseq2/players
%{_gamedatadir}
%config(noreplace) %verify(not size mtime md5) /etc/sysconfig/quake2
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/quake2.conf

%files server
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/quake2-server
%config(noreplace) %verify(not size mtime md5) %{_gamedir}/baseq2/server.cfg

%files svgalib
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/quake2-svgalib
%attr(755,root,root) %{_gamedir}/ref_soft.so

%files software-X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/quake2-software-X11
%attr(755,root,root) %{_gamedir}/ref_softx.so

%files Mesa3D
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/quake2-Mesa3D
%attr(755,root,root) %{_gamedir}/ref_gl.so

#%files 3DFX
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/quake2-3DFX
#%{_gamedir}/quake2/lib3dfxgl.so
#%{_gamedir}/quake2/ref_gl.so

%files GLX
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/quake2-GLX
%attr(755,root,root) %{_gamedir}/ref_glx.so
