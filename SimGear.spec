#
# TODO: - Add missing BRs for xorg
#	- Consider getting back to static linking or set sonames for shared libraries
#	- Still some undefined references (ldd -r /usr/lib/libsgprops.so after install is good example)
#
Summary:	A set of libraries to build 3d simulations, games etc
Summary(pl.UTF-8):	Zestaw bibliotek do budowania trójwymiarowych symulacji, gier itp
Name:		SimGear
Version:	1.9.1
Release:	0.3
License:	GPL v2+
Group:		Libraries
Source0:	ftp://ftp.simgear.org/pub/simgear/Source/%{name}-%{version}.tar.gz
# Source0-md5:	edfdaa60518a06699a409d0eb9f1b157
Patch0:		%{name}-shared.patch
Patch1:		%{name}-link.patch
Patch2:		%{name}-cstdio.patch
Patch3:		%{name}-tgdb.patch
URL:		http://www.simgear.org/
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-devel
BuildRequires:	OpenGL-glut-devel
BuildRequires:	OpenSceneGraph-devel
#BuildRequires:	XFree86-devel
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	freealut-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	metakit-devel >= 2.4.3
BuildRequires:	plib-devel >= 1.8.4-3
BuildRequires:	zlib-devel
Requires:	OpenGL
Requires:	plib >= 1.8.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
SimGear is a set of open-source libraries designed to be used as
building blocks for quickly assembling 3d simulations, games, and
visualization applications.

The term "Simulation Kernel" is a bit presumptuous for us at this
point, but this is the direction we are heading with SimGear.

%description -l pl.UTF-8
SimGear to zestaw bibliotek zaprojektowanych do wykorzystania jako
klocki do szybkiego zestawiania trójwymiarowych symulacji, gier oraz
wizualnych aplikacji.

W tej chwili jest jeszcze trochę za wcześnie na używanie terminu
"Jądro Symulacji", ale to jest kierunek w którym zmierza SimGear.

%package devel
Summary:	Header files for SimGear
Summary(pl.UTF-8):	Pliki nagłówkowe dla SimGear
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenAL-devel
Requires:	OpenGL-devel
Requires:	plib-devel >= 1.8.0

%description devel
Header files neccessary to build SimGear applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe potrzebne do budowania aplikacji z SimGearem.

%package static
Summary:	Static SimGear libraries
Summary(pl.UTF-8):	Statyczne biblioteki SimGear
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static SimGear libraries.

%description static -l pl.UTF-8
Statyczne biblioteki SimGear.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-x
%{__make} -j 2

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS
%attr(755,root,root) %{_libdir}/libsgbucket.so.0.0.0
%attr(755,root,root) %ghost %{_libdir}/libsgbucket.so.0
%attr(755,root,root) %{_libdir}/libsgdebug.so.0.0.0
%attr(755,root,root) %ghost %{_libdir}/libsgdebug.so.0
%attr(755,root,root) %{_libdir}/libsgenvironment.so.0.0.0
%attr(755,root,root) %ghost %{_libdir}/libsgenvironment.so.0
%attr(755,root,root) %{_libdir}/libsgephem.so.0.0.0
%attr(755,root,root) %ghost %{_libdir}/libsgephem.so.0
%attr(755,root,root) %{_libdir}/libsgio.so.0.0.0
%attr(755,root,root) %ghost %{_libdir}/libsgio.so.0
%attr(755,root,root) %{_libdir}/libsgmagvar.so.0.0.0
%attr(755,root,root) %ghost %{_libdir}/libsgmagvar.so.0
%attr(755,root,root) %{_libdir}/libsgmaterial.so.0.0.0
%attr(755,root,root) %ghost %{_libdir}/libsgmaterial.so.0
%attr(755,root,root) %{_libdir}/libsgmath.so.0.0.0
%attr(755,root,root) %ghost %{_libdir}/libsgmath.so.0
%attr(755,root,root) %{_libdir}/libsgmisc.so.0.0.0
%attr(755,root,root) %ghost %{_libdir}/libsgmisc.so.0
%attr(755,root,root) %{_libdir}/libsgmodel.so.0.0.0
%attr(755,root,root) %ghost %{_libdir}/libsgmodel.so.0
%attr(755,root,root) %{_libdir}/libsgnasal.so.0.0.0
%attr(755,root,root) %ghost %{_libdir}/libsgnasal.so.0
%attr(755,root,root) %{_libdir}/libsgprops.so.0.0.0
%attr(755,root,root) %ghost %{_libdir}/libsgprops.so.0
%attr(755,root,root) %{_libdir}/libsgroute.so.0.0.0
%attr(755,root,root) %ghost %{_libdir}/libsgroute.so.0
%attr(755,root,root) %{_libdir}/libsgscreen.so.0.0.0
%attr(755,root,root) %ghost %{_libdir}/libsgscreen.so.0
%attr(755,root,root) %{_libdir}/libsgserial.so.0.0.0
%attr(755,root,root) %ghost %{_libdir}/libsgserial.so.0
%attr(755,root,root) %{_libdir}/libsgsky.so.0.0.0
%attr(755,root,root) %ghost %{_libdir}/libsgsky.so.0
%attr(755,root,root) %{_libdir}/libsgsound.so.0.0.0
%attr(755,root,root) %ghost %{_libdir}/libsgsound.so.0
%attr(755,root,root) %{_libdir}/libsgstructure.so.0.0.0
%attr(755,root,root) %ghost %{_libdir}/libsgstructure.so.0
%attr(755,root,root) %{_libdir}/libsgtgdb.so.0.0.0
%attr(755,root,root) %ghost %{_libdir}/libsgtgdb.so.0
%attr(755,root,root) %{_libdir}/libsgthreads.so.0.0.0
%attr(755,root,root) %ghost %{_libdir}/libsgthreads.so.0
%attr(755,root,root) %{_libdir}/libsgtiming.so.0.0.0
%attr(755,root,root) %ghost %{_libdir}/libsgtiming.so.0
%attr(755,root,root) %{_libdir}/libsgutil.so.0.0.0
%attr(755,root,root) %ghost %{_libdir}/libsgutil.so.0
%attr(755,root,root) %{_libdir}/libsgxml.so.0.0.0
%attr(755,root,root) %ghost %{_libdir}/libsgxml.so.0

%files devel
%defattr(644,root,root,755)
%doc TODO
%attr(755,root,root) %{_libdir}/libsgbucket.so
%attr(755,root,root) %{_libdir}/libsgdebug.so
%attr(755,root,root) %{_libdir}/libsgenvironment.so
%attr(755,root,root) %{_libdir}/libsgephem.so
%attr(755,root,root) %{_libdir}/libsgio.so
%attr(755,root,root) %{_libdir}/libsgmagvar.so
%attr(755,root,root) %{_libdir}/libsgmaterial.so
%attr(755,root,root) %{_libdir}/libsgmath.so
%attr(755,root,root) %{_libdir}/libsgmisc.so
%attr(755,root,root) %{_libdir}/libsgmodel.so
%attr(755,root,root) %{_libdir}/libsgnasal.so
%attr(755,root,root) %{_libdir}/libsgprops.so
%attr(755,root,root) %{_libdir}/libsgroute.so
%attr(755,root,root) %{_libdir}/libsgscreen.so
%attr(755,root,root) %{_libdir}/libsgserial.so
%attr(755,root,root) %{_libdir}/libsgsky.so
%attr(755,root,root) %{_libdir}/libsgsound.so
%attr(755,root,root) %{_libdir}/libsgstructure.so
%attr(755,root,root) %{_libdir}/libsgtgdb.so
%attr(755,root,root) %{_libdir}/libsgthreads.so
%attr(755,root,root) %{_libdir}/libsgtiming.so
%attr(755,root,root) %{_libdir}/libsgutil.so
%attr(755,root,root) %{_libdir}/libsgxml.so
%{_libdir}/libsgbucket.la
%{_libdir}/libsgdebug.la
%{_libdir}/libsgenvironment.la
%{_libdir}/libsgephem.la
%{_libdir}/libsgio.la
%{_libdir}/libsgmagvar.la
%{_libdir}/libsgmaterial.la
%{_libdir}/libsgmath.la
%{_libdir}/libsgmisc.la
%{_libdir}/libsgmodel.la
%{_libdir}/libsgnasal.la
%{_libdir}/libsgprops.la
%{_libdir}/libsgroute.la
%{_libdir}/libsgscreen.la
%{_libdir}/libsgserial.la
%{_libdir}/libsgsky.la
%{_libdir}/libsgsound.la
%{_libdir}/libsgstructure.la
%{_libdir}/libsgtgdb.la
%{_libdir}/libsgthreads.la
%{_libdir}/libsgtiming.la
%{_libdir}/libsgutil.la
%{_libdir}/libsgxml.la
%{_includedir}/simgear

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
