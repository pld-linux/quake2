Summary:	Quake2 for linux
Summary(pl):	Quake2 dla Linuksa
Summary(pt_BR):	Quake2 para Linux
Name:		quake2
Version:	3.20
Release:	1
License:	distributable
Group:		Applications/Games
Source0:	ftp://3darchives.in-span.net/pub/idgames/idstuff/quake2/unix/%{name}-%{version}-glibc-i386-unknown-linux2.0.tar.gz
Source1:	%{name}-scripts.tgz
Source2:	%{name}.sysconfig
Source3:	%{name}.conf
Source4:	%{name}-server.conf
Source5:	%{name}-server
URL:		http://www.idsoftware.com
Requires:	%{name}-renderer
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gamedir	/usr/share/games

%description
Quake2 for linux!

%description -l pl
Quake2 dla Linuksa!

%description -l pt_BR
Quake2 para Linux!

# -------------------- BEGIN SVGALIB subpackage -------------------------------
%package svgalib
Summary:	Quake2 for SVGAlib
Summary(pl):	Biblioteki Quake2 dla SVGAlib
Group:		Applications/Games
Requires:	%{name} = %{version}
Requires:	svgalib >= 1.2.13
Provides:	%{name}-renderer

%description svgalib
Quake2 libraries for SVGAlib play

%description svgalib -l pl
# -------------------- END SVGALIB subpackage -------------------------------
Biblioteki Quake2 do grania na SVGAlib


# -------------------- BEGIN software-X11  subpackage -------------------------------
%package software-X11
Summary:	Quake2 X11 software renderer libs
Summary(pl):	Biblioteka Quake2 - programowe renderowanie
Group:		Applications/Games
Requires:	%{name} = %{version}
Requires:	XFree86
Provides:	%{name}-renderer

%description software-X11
Play Quake2 using software X11 renderer

%description software-X11 -l pl
# -------------------- END software-X11 subpackage -------------------------------
Zagraj w Quake2 przy urzyciu programowego renderowania w X11



# -------------------- BEGIN Mesa3D subpackage -------------------------------
%package Mesa3D
Summary:	Quake2 X11 Mesa renderer libs
Summary(pl):	Biblioteka Mesa dla Quake2
Group:		Applications/Games
Requires:	%{name} = %{version}
Requires:	XFree86
Provides:	%{name}-renderer

%description Mesa3D
Play Quake2 using Mesa3D software acceleration

%description Mesa3D -l pl
# -------------------- END Mesa3D subpackage -------------------------------
Zagraj w Quake2 przy urzyciu programowego renderowania Mesa3D



# -------------------- BEGIN 3DFX subpackage -------------------------------
%package 3DFX
Summary:	Quake2 3DFX libs
Summary(pl):	Biblioteki 3DFX dla Quake2
Group:		Applications/Games
Requires:	%{name} = %{version}
Requires:	XFree86
Provides:	%{name}-renderer

%description 3DFX
Play Quake2 using 3DFX acceleration

%description 3DFX -l pl
# -------------------- END Mesa3D subpackage -------------------------------
Zagraj w Quake2 z akceleracj± 3DFX



# -------------------- BEGIN GLX subpackage -------------------------------
%package GLX
Summary:	OpenGL Quake2
Summary(pl):	Quake2 OpenGL
Group:		Applications/Games
Requires:	%{name} = %{version}
Requires:	OpenGL
Provides:	%{name}-renderer

%description GLX
Play Quake2 using hardware OpenGL acceleration

%description GLX -l pl
# -------------------- END Mesa3D subpackage -------------------------------
Zagraj w Quake2 ze sprzêtow± akceleracj± OpenGL



# -------------------- BEGIN SERVER subpackage -------------------------------
%package server
Summary:	Quake2 server
Summary(pl):	Serwer Quake2
Summary(pt_BR):	Servidor Quake2
Group:		Applications/Games
Requires:	%{name} = %{version}

%description server
Quake2 server

%description server -l pt_BR
Servidor Quake2

%description server -l pl
# -------------------- END SERVER subpackage -------------------------------
Serwer Quake2 dla Linuksa

# -------------------- END packages definitions ----------------------------
# **************************************************************************




%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_gamedir}/quake2/baseq2/players/{crakhor,cyborg,female,male} \
	$RPM_BUILD_ROOT{%{_bindir},/etc/rc.d/init.d,/etc/sysconfig}

for i in crakhor cyborg female male ; do
        install baseq2/players/$i/* $RPM_BUILD_ROOT%{_gamedir}/quake2/baseq2/players/$i
done

install baseq2/gamei386.so	$RPM_BUILD_ROOT%{_gamedir}/quake2/baseq2/gamei386.so
install baseq2/pak2.pak		$RPM_BUILD_ROOT%{_gamedir}/quake2/baseq2
install quake2			$RPM_BUILD_ROOT%{_bindir}/quake2id
install lib3dfxgl.so		$RPM_BUILD_ROOT%{_gamedir}/quake2
install libMesaGL.so.2.6	$RPM_BUILD_ROOT%{_gamedir}/quake2

for i in gl glx soft softx ; do
        install ref_$i.so $RPM_BUILD_ROOT%{_gamedir}/quake2
done

#install %{SOURCE1}	$RPM_BUILD_ROOT%{_bindir}/quake2
install %{SOURCE2}	$RPM_BUILD_ROOT/etc/sysconfig/quake2
install %{SOURCE3}	$RPM_BUILD_ROOT%{_sysconfdir}
install %{SOURCE4}	$RPM_BUILD_ROOT%{_gamedir}/quake2/baseq2/server.cfg
install %{SOURCE5}	$RPM_BUILD_ROOT/etc/rc.d/init.d/quake2-server

gzip -9nf README readme.txt

cd $RPM_BUILD_ROOT%{_bindir}/ ; tar zxfv %{SOURCE1}

%clean
rm -rf $RPM_BUILD_ROOT

# ------------------------------------------------------------------------------------ 	#
# 	Now the things done on destination machine					#

%post svgalib
echo "Now run /usr/bin/quake2-svgalib "

%post software-X11
echo "Now run /usr/bin/quake2-software-X11 "

%post 3DFX
echo "Now run /usr/bin/quake2-3DFX "

%post Mesa3D
ln -s %{_gamedir}/quake2/libMesaGL.so.2.6 %{_gamedir}/quake2/libMesaGL.so.2
echo "Now run /usr/bin/quake2-Mesa3D "

%post GLX
echo "Now run /usr/bin/quake2-GLX "

%post server
/sbin/chkconfig --add quake2-server
echo "Run \"/etc/rc.d/init.d/quake2-server start\" to start Quake2 server." >&2

%preun server
if [ "$1" = "0" ]; then
    /etc/rc.d/init.d/quake2-server stop >&2
    /sbin/chkconfig --del quake2-server
fi


# -----------------------------------------------------------------------------------	#
#	Now the files in packages
%files
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/quake2
%attr(755,root,root)%{_bindir}/quake2id
%dir %{_gamedir}/quake2
%dir %{_gamedir}/quake2/baseq2
%attr(755,root,root) %{_gamedir}/quake2/baseq2/*so*
%{_gamedir}/quake2/baseq2/pak2.pak
%{_gamedir}/quake2/baseq2/players
%config /etc/sysconfig/quake2
%config %{_sysconfdir}/quake2.conf
%doc *.gz

%files server
%defattr(644,root,root,755)
%attr(755,games,games) 	/etc/rc.d/init.d/quake2-server
%config %{_gamedir}/quake2/baseq2/server.cfg

%files svgalib
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/quake2-svgalib
%{_gamedir}/quake2/ref_soft.so

%files software-X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/quake2-software-X11
%{_gamedir}/quake2/ref_softx.so

%files Mesa3D
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/quake2-Mesa3D
%{_gamedir}/quake2/libMesaGL.so.2.6
%{_gamedir}/quake2/ref_gl.so

%files 3DFX
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/quake2-3DFX
%{_gamedir}/quake2/lib3dfxgl.so
%{_gamedir}/quake2/ref_gl.so

%files GLX
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/quake2-GLX
%{_gamedir}/quake2/ref_glx.so
