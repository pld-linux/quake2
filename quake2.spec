
Summary:	Quake2 for linux
Summary(pl):	Quake2 dla Linuksa
Summary(pt_BR):	Quake2 para Linux
Name:		quake2
Version:	20031005
Release:	1
License:	GPL (for code only)
Group:		Applications/Games
Source0:	http://www.kernel.pl/~mmazur/misc/%{name}-%{version}.tar.bz2
# Source0-md5:	f8ff2cb2dbfa6c70c245e73f94cf2017
#Source1:	multiplay pack (need to check licence)
Source2:	%{name}-server.conf
Source3:	%{name}-server
Source4:	%{name}.png
Patch0:		%{name}-stupid_nvidia_bug.patch
URL:		http://www.idsoftware.com/games/quake/quake2/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libltdl-devel
BuildRequires:	libtool
BuildRequires:	svgalib-devel
BuildRequires:	unzip
Requires:	%{name}-renderer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gamelibdir	%{_libdir}/games/%{name}
%define		_gamedatadir	%{_datadir}/games/%{name}

%description
Quake2 for linux!

%description -l pl
Quake2 dla Linuksa!

%description -l pt_BR
Quake2 para Linux!

%package static
Summary:	Quake2 - static libs
Summary(pl):	Quake2 - biblioteki statyczne
Group:		Applications/Games
Requires:	%{name} = %{version}

%description static
Quake2 - static libs

%description static -l pl
Quake2 - biblioteki statyczne

%package server
Summary:	Quake2 server
Summary(pl):	Serwer Quake2
Summary(pt_BR):	Servidor Quake2
Group:		Applications/Games
PreReq:		rc-scripts
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name} = %{version}

%description server
Quake2 server.

%description server -l pl
Serwer Quake2 dla Linuksa.

%description server -l pt_BR
Servidor Quake2.

%package 3dfx
Summary:	Quake2 3DFX libs
Summary(pl):	Biblioteki 3DFX dla Quake2
Group:		Applications/Games
Requires:	%{name} = %{version}
Provides:	%{name}-renderer
Obsoletes:	%{name}-3DFX

%description 3dfx
Play Quake2 using 3DFX acceleration.

%description 3dfx -l pl
Zagraj w Quake2 z akceleracj± 3DFX.

%package glx
Summary:	OpenGL Quake2
Summary(pl):	Quake2 OpenGL
Group:		Applications/Games
Requires:	%{name} = %{version}
Requires:	OpenGL
Provides:	%{name}-renderer
Obsoletes:	%{name}-GLX

%description glx
Play Quake2 using hardware OpenGL acceleration.

%description glx -l pl
Zagraj w Quake2 ze sprzêtow± akceleracj± OpenGL.

%package sdl
Summary:	Quake2 for SDL
Summary(pl):	Biblioteki Quake2 dla SDL
Group:		Applications/Games
Requires:	%{name} = %{version}
Provides:	%{name}-renderer

%description sdl
Quake2 libraries for SDL play.

%description sdl -l pl
Biblioteki Quake2 do grania na SDL.

%package sgl
Summary:	Quake2 for SDL with GL
Summary(pl):	Biblioteki Quake2 dla SDL z obs³ug± GL
Group:		Applications/Games
Requires:	%{name} = %{version}
Provides:	%{name}-renderer

%description sgl
Quake2 libraries for SDL with GL play.

%description sgl -l pl
Biblioteki Quake2 do grania na SDL z obs³ug± GL.

%package svga
Summary:	Quake2 for SVGAlib
Summary(pl):	Biblioteki Quake2 dla SVGAlib
Group:		Applications/Games
Requires:	%{name} = %{version}
Provides:	%{name}-renderer
Obsoletes:	%{name}-svgalib

%description svga
Quake2 libraries for SVGAlib play.

%description svga -l pl
Biblioteki Quake2 do grania na SVGAlib.

%package x11
Summary:	Quake2 X11 software renderer libs
Summary(pl):	Biblioteka Quake2 - programowe renderowanie
Group:		Applications/Games
Requires:	%{name} = %{version}
Provides:	%{name}-renderer
Obsoletes:	%{name}-software-X11
Obsoletes:	%{name}-X11

%description x11
Play Quake2 using software X11 renderer.

%description x11 -l pl
Zagraj w Quake2 przy u¿yciu programowego renderowania w X11.

%prep
%setup -q -n %{name}
%patch0

cat Makefile.am |sed -e 's/libltdl//'>Makefile.am.tmp
mv -f Makefile.am.tmp Makefile.am

cat configure.in |sed -e 's/AC_LIBLTDL_CONVENIENCE/AC_LIBLTDL_INSTALLABLE/' \
>configure.in.tmp
mv -f configure.in.tmp configure.in

%build
%{__aclocal}
%{__autoheader}
%{__libtoolize} --ltdl --automake
%{__automake}
%{__autoconf}

%configure \
	--enable-ltdl-install=no \
	--libdir=%{_libdir}/games \
	--datadir=%{_datadir}/games \
	--enable-sdlsound \
	--with-opengl=/usr/X11R6

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_gamedatadir}/baseq2,/etc/rc.d/init.d} \
	$RPM_BUILD_ROOT{%{_pixmapsdir},%{_applnkdir}/Games}

#$RPM_BUILD_ROOT%{_gamedir}/baseq2/players/{crakhor,cyborg,female,male}

#for i in crakhor cyborg female male ; do
#        install baseq2/players/$i/* $RPM_BUILD_ROOT%{_gamedir}/baseq2/players/$i
#done
#install baseq2/pak2.pak        $RPM_BUILD_ROOT%{_gamedir}/quake2/baseq2

install %{SOURCE2} $RPM_BUILD_ROOT%{_gamedatadir}/baseq2/server.cfg
install %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d
install %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}

echo "[Desktop Entry]\nName=Quake II\nExec=%{name}\nIcon=%{name}.png \
\nTerminal=0\nType=Application\n" > $RPM_BUILD_ROOT%{_applnkdir}/Games/%{name}.desktop

rm -rf docs/{CVS,ctf/CVS}

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
%doc AUTHORS COPYING HACKING README TODO docs/*
%attr(755,root,root) %{_bindir}/quake2
%dir %{_gamelibdir}
%dir %{_gamelibdir}/baseq2
%dir %{_gamelibdir}/ctf
%attr(755,root,root) %{_gamelibdir}/baseq2/game.so
%{_gamelibdir}/baseq2/game.la
%attr(755,root,root) %{_gamelibdir}/ctf/game.so
%{_gamelibdir}/ctf/game.la
#%%{_gamedir}/baseq2/pak2.pak
#%%{_gamedir}/baseq2/players
%dir %{_gamedatadir}
%dir %{_gamedatadir}/baseq2
%{_pixmapsdir}/quake2.png
%{_applnkdir}/Games/quake2.desktop

%files static
%defattr(644,root,root,755)
%{_gamelibdir}/baseq2/game.a
%{_gamelibdir}/ctf/game.a
%{_gamelibdir}/ref_glx.a
%{_gamelibdir}/ref_sdlgl.a
%{_gamelibdir}/ref_soft.a
%{_gamelibdir}/ref_softsdl.a
%{_gamelibdir}/ref_softx.a
%{_gamelibdir}/ref_tdfx.a

%files server
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/quake2-server
%config(noreplace) %verify(not size mtime md5) %{_gamedatadir}/baseq2/server.cfg

%files 3dfx
%defattr(644,root,root,755)
%attr(755,root,root) %{_gamelibdir}/ref_tdfx.so
%{_gamelibdir}/ref_tdfx.la

%files glx
%defattr(644,root,root,755)
%attr(755,root,root) %{_gamelibdir}/ref_glx.so
%{_gamelibdir}/ref_glx.la

%files sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{_gamelibdir}/ref_softsdl.so
%{_gamelibdir}/ref_softsdl.la

%files sgl
%defattr(644,root,root,755)
%attr(755,root,root) %{_gamelibdir}/ref_sdlgl.so
%{_gamelibdir}/ref_sdlgl.la

%files svga
%defattr(644,root,root,755)
%attr(755,root,root) %{_gamelibdir}/ref_soft.so
%{_gamelibdir}/ref_soft.la

%files x11
%defattr(644,root,root,755)
%attr(755,root,root) %{_gamelibdir}/ref_softx.so
%{_gamelibdir}/ref_softx.la
