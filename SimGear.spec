# TODO: - Add missing BRs for xorg
#	- Consider getting back to static linking or set sonames for shared libraries
#	- fix linking libsgprops.so and probably others .so files
%define	_pre	pre1
Summary:	A set of libraries to build 3d simulations, games etc
Summary(pl.UTF-8):	Zestaw bibliotek do budowania trójwymiarowych symulacji, gier itp
Name:		SimGear
Version:	0.3.11
Release:	0.%{_pre}.1
License:	GPL v2+
Group:		Libraries
Source0:	ftp://ftp.simgear.org/pub/simgear/Source/%{name}-%{version}-%{_pre}.tar.gz
# Source0-md5:	9e7edc288dae1860a205321c9287c521
Patch0:		%{name}-shared.patch
Patch1:		%{name}-link.patch
URL:		http://www.simgear.org/
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-devel
BuildRequires:	OpenGL-glut-devel
#BuildRequires:	XFree86-devel
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	freealut-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	metakit-devel >= 2.4.3
BuildRequires:	plib-devel >= 1.8.4-3
BuildRequires:	tcl-devel
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
%setup -q -n %{name}-%{version}-%{_pre}
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-x \
	--with-tcl=/usr/lib
%{__make} -j 1

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
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc TODO
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/simgear

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
