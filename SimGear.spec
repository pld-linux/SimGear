#
# TODO: - bring back static libraries
#
Summary:	A set of libraries to build 3d simulations, games etc
Summary(pl.UTF-8):	Zestaw bibliotek do budowania trójwymiarowych symulacji, gier itp
Name:		SimGear
Version:	2016.2.1
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	https://downloads.sourceforge.net/project/flightgear/release-2016.2/simgear-%{version}.tar.bz2
# Source0-md5:	7bd21e63ffb83109f530627c593d94cd
Patch0:		cmake.patch
URL:		http://wiki.flightgear.org/SimGear
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-devel
BuildRequires:	OpenGL-glut-devel
BuildRequires:	OpenSceneGraph-devel >= 3.2.0
BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:	freealut-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	subversion-devel
BuildRequires:	zlib-devel
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1
%define		filterout	-flto

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
%setup -q -n simgear-%{version}
%patch0 -p1

%build
install -d build
cd build
%cmake -DSIMGEAR_SHARED=ON -DSYSTEM_EXPAT=ON -DJPEG_FACTORY=ON ../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS Thanks
%attr(755,root,root) %{_libdir}/libSimGearCore.so.%{version}
%attr(755,root,root) %{_libdir}/libSimGearScene.so.%{version}

%files devel
%defattr(644,root,root,755)
%dir %{_libdir}/cmake/SimGear
%{_libdir}/cmake/SimGear/SimGearConfig.cmake
%{_libdir}/cmake/SimGear/SimGearConfigVersion.cmake
%{_libdir}/cmake/SimGear/SimGearTargets-pld.cmake
%{_libdir}/cmake/SimGear/SimGearTargets.cmake
%attr(755,root,root) %{_libdir}/libSimGearCore.so
%attr(755,root,root) %{_libdir}/libSimGearScene.so
%{_includedir}/simgear

#%#files static
#%#defattr(644,root,root,755)
#%#{_libdir}/lib*.a
