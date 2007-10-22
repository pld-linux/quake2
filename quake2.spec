# TODO
# - unpackaged: /usr/lib/quake2/ref_gl.so
#
# Conditional build:
%bcond_with	rogue	# with Rogue ("Ground Zero") Mission Pack  (non-distributable package)
%bcond_with	xatrix	# with Xatrix ("The Reckoning") Mission Pack  (non-distributable package)
#
Summary:	Quake2 for Linux
Summary(pl.UTF-8):	Quake2 dla Linuksa
Summary(pt_BR.UTF-8):	Quake2 para Linux
Name:		quake2
Version:	3.21
Release:	4.2
Epoch:		1
License:	GPL (for main code only)
Group:		Applications/Games
Source0:	ftp://ftp.idsoftware.com/idstuff/source/q2source-%{version}.zip
# Source0-md5:	3ac9ac6a833b9c049a9f763c3137b86f
#Source1:	multiplay pack (need to check licence)
# ftp://ftp.idsoftware.com/idstuff/quake2/q2-3.20-x86-full.exe
Source2:	%{name}-server.conf
Source3:	%{name}-server
Source4:	%{name}.png
Source5:	%{name}-server.sysconfig
Source6:	%{name}-server.screenrc
Source10:	ftp://ftp.idsoftware.com/idstuff/quake2/source/roguesrc320.shar.Z
# Source10-md5:	7d5e052839c9e629bad0a6570aa70554
Source11:	ftp://ftp.idsoftware.com/idstuff/quake2/source/xatrixsrc320.shar.Z
# Source11-md5:	41fc4ecc4f25c068e7d1f488bd4a1e1a
Patch0:		%{name}-fix.patch
Patch1:		%{name}-gamedir.patch
Patch2:		%{name}-rogue.patch
Patch3:		%{name}-xatrix.patch
URL:		http://www.idsoftware.com/games/quake/quake2/
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	XFree86-devel
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	svgalib-devel
BuildRequires:	unzip
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-renderer = %{epoch}:%{version}-%{release}
Obsoletes:	quake2-3DFX
Obsoletes:	quake2-3dfx
Obsoletes:	quake2-Mesa3D
Obsoletes:	quake2-sdl
Obsoletes:	quake2-sgl
Obsoletes:	quake2-snd-alsa
Obsoletes:	quake2-snd-ao
Obsoletes:	quake2-snd-oss
Obsoletes:	quake2-snd-sdl
Obsoletes:	quake2-static
# other archs need at least more #ifdefs
ExclusiveArch:	%{ix86} alpha
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gamelibdir	%{_libdir}/%{name}
%define		_gamedatadir	%{_datadir}/%{name}
%define		_gamehomedir	/var/games/%{name}
%ifarch %{ix86}
%define		qarch	i386
%else
%ifarch alpha
%define		qarch	axp
%else
%define		qarch	%{nil}
%endif
%endif

%description
Quake2 for Linux!

%description -l pl.UTF-8
Quake2 dla Linuksa!

%description -l pt_BR.UTF-8
Quake2 para Linux!

%package common
Summary:	Quake2 common files
Group:		Applications/Games

%description common
Quake2 common files.

%package server
Summary:	Quake2 server
Summary(pl.UTF-8):	Serwer Quake2
Summary(pt_BR.UTF-8):	Servidor Quake2
Group:		Applications/Games
Provides:	group(quake2)
Provides:	user(quake2)
Requires(post,preun):	/sbin/chkconfig
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	rc-scripts
Requires:	screen

%description server
Quake2 server.

%description server -l pl.UTF-8
Serwer Quake2 dla Linuksa.

%description server -l pt_BR.UTF-8
Servidor Quake2.

%package glx
Summary:	OpenGL Quake2
Summary(pl.UTF-8):	Quake2 OpenGL
Group:		X11/Applications/Games
Provides:	%{name}-renderer = %{epoch}:%{version}-%{release}
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	quake2-GLX

%description glx
Play Quake2 using hardware OpenGL acceleration.

%description glx -l pl.UTF-8
Zagraj w Quake2 ze sprzętową akceleracją OpenGL.

%package svga
Summary:	Quake2 for SVGAlib
Summary(pl.UTF-8):	Biblioteki Quake2 dla SVGAlib
Group:		Applications/Games
Provides:	%{name}-renderer = %{epoch}:%{version}-%{release}
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	quake2-svgalib

%description svga
Quake2 libraries for SVGAlib play.

%description svga -l pl.UTF-8
Biblioteki Quake2 do grania na SVGAlib.

%package x11
Summary:	Quake2 X11 software renderer libs
Summary(pl.UTF-8):	Biblioteka Quake2 - programowe renderowanie
Group:		X11/Applications/Games
Provides:	%{name}-renderer = %{epoch}:%{version}-%{release}
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	quake2-X11
Obsoletes:	quake2-software-X11

%description x11
Play Quake2 using software X11 renderer.

%description x11 -l pl.UTF-8
Zagraj w Quake2 przy użyciu programowego renderowania w X11.

%package rogue
Summary:	Quake II: Ground Zero (mission pack)
Summary(pl.UTF-8):	Quake II: Ground Zero (zestaw misji)
License:	GPL+Limited Program Source Code License (non-distributable in binary form)
Group:		Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description rogue
Quake II: Ground Zero (mission pack).

%description rogue -l pl.UTF-8
Quake II: Ground Zero (zestaw misji).

%package xatrix
Summary:	Quake II: The Reckoning (mission pack)
Summary(pl.UTF-8):	Quake II: The Reckoning (zestaw misji)
License:	GPL+Limited Program Source Code License (non-distributable in binary form)
Group:		Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description xatrix
Quake II: The Reckoning (mission pack).

%description xatrix -l pl.UTF-8
Quake II: The Reckoning (zestaw misji).

%prep
%setup -q -c
mv -f %{name}-%{version}/* .
%patch0 -p1
%patch1 -p1

%if %{with rogue}
install -d rogue
cd rogue
gzip -dc %{SOURCE10} | %{__sed} s/"^more "/"cat >LICENSE.rogue "/ >rogue.shar
echo yes| sh rogue.shar
cd ..
%patch2 -p1
%endif

%if %{with xatrix}
install -d xatrix
cd xatrix
gunzip -c %{SOURCE11} | %{__sed} s/"^more "/"cat >LICENSE.xatrix "/ >xatrix.shar
echo yes| sh xatrix.shar
cd ..
%patch3 -p1
%endif

%build
cat linux/Makefile | tr -d '\015' > Makefile.tmp
mv -f Makefile.tmp linux/Makefile

%{__make} build_release -C linux \
	CC="%{__cc}" \
	RELEASE_CFLAGS="-Dstricmp=strcasecmp %{rpmcflags} -ffast-math %{!?debug:-fomit-frame-pointer} -DPKGLIBDIR=\\\\\\\"%{_gamelibdir}\\\\\\\" -DPKGDATADIR=\\\\\\\"%{_gamedatadir}\\\\\\\"" \
	MESA_DIR=/usr

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_gamedatadir}/baseq2,%{_gamelibdir}/{baseq2,ctf}} \
	$RPM_BUILD_ROOT%{_gamehomedir}/.quake2/baseq2 \
	$RPM_BUILD_ROOT{/etc/sysconfig,/etc/rc.d/init.d} \
	$RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_desktopdir}}

cd linux/release%{qarch}-glibc

install quake2 $RPM_BUILD_ROOT%{_bindir}/quake2id
install ref_*.so $RPM_BUILD_ROOT%{_gamelibdir}
install game%{qarch}.so $RPM_BUILD_ROOT%{_gamelibdir}/baseq2
install ctf/game%{qarch}.so $RPM_BUILD_ROOT%{_gamelibdir}/ctf
%if %{with rogue}
install -D rogue/game%{qarch}.so $RPM_BUILD_ROOT%{_gamelibdir}/rogue/game%{qarch}.so
%endif
%if %{with xatrix}
install -D xatrix/game%{qarch}.so $RPM_BUILD_ROOT%{_gamelibdir}/xatrix/game%{qarch}.so
%endif

cat > $RPM_BUILD_ROOT%{_bindir}/quake2-glx <<EOF
#!/bin/sh
exec %{_bindir}/quake2id +set vid_ref glx +set gl_driver libGL.so.1 > /dev/null
EOF

cat > $RPM_BUILD_ROOT%{_bindir}/quake2-x11 <<EOF
#!/bin/sh
exec %{_bindir}/quake2id +set vid_ref softx > /dev/null
EOF

cat > $RPM_BUILD_ROOT%{_bindir}/quake2-svga <<EOF
#!/bin/sh
exec %{_bindir}/quake2id +set vid_ref soft > /dev/null
EOF

cat > $RPM_BUILD_ROOT%{_desktopdir}/quake2-glx.desktop <<EOF
[Desktop Entry]
Name=Quake II (GLX)
Comment=Quake2 for Linux
Comment[pl]=Quake2 dla Linuksa
Exec=quake2-glx
Icon=quake2.png
Terminal=false
Type=Application
Categories=Game;X-FPPGame;
Encoding=UTF-8
EOF

cat > $RPM_BUILD_ROOT%{_desktopdir}/quake2-x11.desktop <<EOF
[Desktop Entry]
Name=Quake II (X11)
Comment=Quake2 for Linux
Comment[pl]=Quake2 dla Linuksa
Exec=quake2-x11
Icon=quake2.png
Terminal=false
Type=Application
Categories=Game;X-FPPGame;
Encoding=UTF-8
EOF

echo "%{_gamelibdir}" > $RPM_BUILD_ROOT%{_sysconfdir}/quake2.conf

install %{SOURCE2} $RPM_BUILD_ROOT%{_gamehomedir}/.quake2/baseq2/server.cfg
install %{SOURCE6} $RPM_BUILD_ROOT%{_gamehomedir}/.screenrc
install %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d/q2ded
install %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE5} $RPM_BUILD_ROOT/etc/sysconfig/q2ded

%clean
rm -rf $RPM_BUILD_ROOT

%pre server
%groupadd -P %{name}-server -g 170 quake2
%useradd -P %{name}-server -u 170 -d %{_gamehomedir} -s /bin/sh -c "Quake 2" -g quake2 quake2

%post server
/sbin/chkconfig --add q2ded
%service q2ded restart "Quake2 server"

%preun server
if [ "$1" = "0" ]; then
	%service q2ded stop
	/sbin/chkconfig --del q2ded
fi

%postun server
if [ "$1" = "0" ]; then
	%userremove quake2
	%groupremove quake2
fi

%triggerpostun server -- quake2-server < 1:0.3-3.11
if [ -f %{_gamedatadir}/baseq2/server.cfg.rpmsave ]; then
	mv -f %{_gamehomedir}/.quake2/baseq2/server.cfg{,.rpmnew}
	mv -f %{_gamedatadir}/baseq2/server.cfg.rpmsave %{_gamehomedir}/.quake2/baseq2/server.cfg
fi

if [ -f /var/lock/subsys/quake2-server ]; then
	mv -f /var/lock/subsys/{quake2-server,q2ded}
	%service -q q2ded restart
fi

%files
%defattr(644,root,root,755)
%doc *_Changes.txt changes.txt joystick.txt readme.txt linux/README*
%{_pixmapsdir}/quake2.png

%files common
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/quake2id
%{_sysconfdir}/quake2.conf
%dir %{_gamelibdir}
%dir %{_gamelibdir}/baseq2
%attr(755,root,root) %{_gamelibdir}/baseq2/game%{qarch}.so
%dir %{_gamelibdir}/ctf
%attr(755,root,root) %{_gamelibdir}/ctf/game%{qarch}.so
%dir %{_gamedatadir}
%dir %{_gamedatadir}/baseq2

%files server
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/q2ded
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/q2ded
%dir %attr(770,root,quake2) %{_gamehomedir}
%config(noreplace) %attr(660,root,quake2) %verify(not md5 mtime size) %{_gamehomedir}/.screenrc
%dir %attr(770,root,quake2) %{_gamehomedir}/.quake2
%dir %attr(770,root,quake2) %{_gamehomedir}/.quake2/baseq2
%config(noreplace) %attr(660,root,quake2) %verify(not md5 mtime size) %{_gamehomedir}/.quake2/baseq2/server.cfg

%files glx
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/quake2-glx
%attr(755,root,root) %{_gamelibdir}/ref_glx.so
%{_desktopdir}/quake2-glx.desktop

%files svga
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/quake2-svga
%attr(755,root,root) %{_gamelibdir}/ref_soft.so

%files x11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/quake2-x11
%attr(755,root,root) %{_gamelibdir}/ref_softx.so
%{_desktopdir}/quake2-x11.desktop

%if %{with rogue}
%files rogue
%defattr(644,root,root,755)
%dir %{_gamelibdir}/rogue
%attr(755,root,root) %{_gamelibdir}/rogue/game%{qarch}.so
%endif

%if %{with xatrix}
%files xatrix
%defattr(644,root,root,755)
%dir %{_gamelibdir}/xatrix
%attr(755,root,root) %{_gamelibdir}/xatrix/game%{qarch}.so
%endif
