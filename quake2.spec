
%define		_snapshot	20020721


Summary:	Quake2 for linux
Summary(pl):	Quake2 dla Linuksa
Summary(pt_BR):	Quake2 para Linux
Name:		quake2
Version:	3.21
Release:	5.%{_snapshot}
License:	GPL (for code only)
Group:		Applications/Games
Source0:	quake2-%{_snapshot}.tar.bz2
Source1:	%{name}-scripts.tgz
#Source2:	multiplay pack (need to check licence)
Source3:	%{name}.conf
Source4:	%{name}-server.conf
Source5:	%{name}-server
Source6:	%{name}.png
Patch0:		%{name}-gl_fix.patch
URL:		http://www.idsoftware.com/games/quake/quake2/
BuildRequires:	libltdl-devel
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel
BuildRequires:	svgalib-devel
BuildRequires:	unzip
Requires:	%{name}-renderer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_xbindir	/usr/X11R6/bin
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

%package X11
Summary:	Quake2 X11 software renderer libs
Summary(pl):	Biblioteka Quake2 - programowe renderowanie
Group:		Applications/Games
Requires:	%{name} = %{version}
Provides:	%{name}-renderer
Obsoletes:	%{name}-software-X11

%description X11
Play Quake2 using software X11 renderer.

%description X11 -l pl
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

#%package 3DFX
#Summary:	Quake2 3DFX libs
#Summary(pl):	Biblioteki 3DFX dla Quake2
#Group:		Applications/Games
#Requires:	%{name} = %{version}
#Provides:	%{name}-renderer

#%description 3DFX
#Play Quake2 using 3DFX acceleration.

#%description 3DFX -l pl
#Zagraj w Quake2 z akceleracj± 3DFX.

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
%setup -q -n %{name}
%patch0

cat Makefile.am |sed -e 's/libltdl//'>Makefile.am.tmp
mv -f Makefile.am.tmp Makefile.am

cat configure.in |sed -e 's/AC_LIBLTDL_CONVENIENCE/AC_LIBLTDL_INSTALLABLE/' \
>configure.in.tmp
mv -f configure.in.tmp configure.in


%build
libtoolize
aclocal
autoheader
%{__automake}
%{__autoconf}

%configure \
	--enable-ltdl-install=no \
	--libdir=/usr/lib/games

%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_gamedatadir}/baseq2,%{_gamedatadir}/ctf,%{_bindir},%{_xbindir},/etc/rc.d/init.d,%{_gamedir}}
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_applnkdir}/Games}

#$RPM_BUILD_ROOT%{_gamedir}/baseq2/players/{crakhor,cyborg,female,male}

#for i in crakhor cyborg female male ; do
#        install baseq2/players/$i/* $RPM_BUILD_ROOT%{_gamedir}/baseq2/players/$i
#done
#install baseq2/pak2.pak        $RPM_BUILD_ROOT%{_gamedir}/quake2/baseq2


tar zxfv %{SOURCE1}
install %{name}-svgalib $RPM_BUILD_ROOT%{_bindir}
install {%{name}-GLX,%{name}-Mesa3D,%{name}-X11} $RPM_BUILD_ROOT%{_xbindir}

install %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}
install %{SOURCE4} $RPM_BUILD_ROOT%{_gamedatadir}/baseq2/server.cfg
install %{SOURCE5} $RPM_BUILD_ROOT/etc/rc.d/init.d/quake2-server
install %{SOURCE6} $RPM_BUILD_ROOT%{_pixmapsdir}

ln -sf %{_gamedir}/baseq2/gamei386.so $RPM_BUILD_ROOT%{_gamedatadir}/baseq2/gamei386.so
ln -sf %{_gamedir}/ctf/gamei386.so $RPM_BUILD_ROOT%{_gamedatadir}/ctf/gamei386.so

q2ver="GLX Mesa3D X11"

for f in $q2ver; do
	desktopfile="$RPM_BUILD_ROOT%{_applnkdir}/Games/%{name}-$f.desktop"
	echo "[Desktop Entry]\nName=Quake II ($f)\nExec=%{name}-$f\nIcon=%{name}.png \
	\nTerminal=0\nType=Application\n" > $desktopfile
done

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
	if [ -f /var/lock/subsys/quake2-server ]; then
		/etc/rc.d/init.d/quake2-server stop 1>&2
	fi
	/sbin/chkconfig --del quake2-server
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING HACKING README TODO
#doc/README* doc/*.txt doc/ctf/*
%attr(755,root,root)%{_bindir}/quake2
%dir %{_gamedir}
%attr(755,root,root) %{_gamedir}/baseq2/game.so
%attr(755,root,root) %{_gamedir}/ctf/game.so
#%{_gamedir}/baseq2/pak2.pak
#%{_gamedir}/baseq2/players
%{_gamedatadir}
%{_pixmapsdir}/quake2.png
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/quake2.conf

%files server
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/quake2-server
%config(noreplace) %verify(not size mtime md5) %{_gamedatadir}/baseq2/server.cfg

%files svgalib
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/quake2-svgalib
%attr(755,root,root) %{_gamedir}/ref_soft.so

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_xbindir}/quake2-X11
%attr(755,root,root) %{_gamedir}/ref_softx.so
%{_applnkdir}/Games/quake2-X11.desktop

#%files Mesa3D
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_xbindir}/quake2-Mesa3D
#%attr(755,root,root) %{_gamedir}/ref_gl.so
#%{_applnkdir}/Games/quake2-Mesa3D.desktop

#%files 3DFX
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/quake2-3DFX
#%{_gamedir}/quake2/lib3dfxgl.so
#%{_gamedir}/quake2/ref_gl.so

%files GLX
%defattr(644,root,root,755)
%attr(755,root,root) %{_xbindir}/quake2-GLX
%attr(755,root,root) %{_gamedir}/ref_glx.so
%{_applnkdir}/Games/quake2-GLX.desktop
