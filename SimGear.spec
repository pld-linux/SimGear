Summary:	A set of libraries to build 3d simulations, games etc
Summary(pl):	Zestaw bibliotek do budowania trójwymiarowych symulacji, gier itp
Name:		SimGear
Version:	0.3.8
Release:	1
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.simgear.org/pub/simgear/Source/%{name}-%{version}.tar.gz
# Source0-md5:	d535880954b8d9393f55cc51ee045c60
Patch0:		%{name}-shared.patch
Patch1:		%{name}-libs.patch
URL:		http://www.simgear.org/
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	glut-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	metakit-devel >= 2.4.3
BuildRequires:	plib-devel >= 1.8.4
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

%description -l pl
SimGear to zestaw bibliotek zaprojektowanych do wykorzystania jako
klocki do szybkiego zestawiania trójwymiarowych symulacji, gier...

W tej chwili jest jeszcze trochê za wcze¶nie na u¿ywanie terminu
"J±dro Symulacji", ale to jest kierunek w którym zmierza SimGear.

%package devel
Summary:	Header files for SimGear
Summary(pl):	Pliki nag³ówkowe dla SimGear
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenAL-devel
Requires:	OpenGL-devel-base
Requires:	plib-devel >= 1.8.0

%description devel
Header files neccessary to build SimGear applications.

%description devel -l pl
Pliki nag³ówkowe potrzebne do budowania aplikacji z SimGearem.

%package static
Summary:	Static SimGear libraries
Summary(pl):	Statyczne biblioteki SimGear
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static SimGear libraries.

%description static -l pl
Statyczne biblioteki SimGear.

%prep
%setup -q
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
%{__make}

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
