Summary:	a set of libraries to build 3d simulations, games etc.
Summary(pl):	zestaw bibliotek do budowania tr�jwymiarowych symulacji, gier itp.
Name:		SimGear
Version:	0.0.14
Release:	3
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	����������
Group(uk):	��̦�����
Source0:	ftp://ftp.simgear.org/pub/simgear/Source/%{name}-%{version}.tar.gz
Patch0:		%{name}-shared.patch
URL:		http://www.simgear.org
Requires:	OpenGL
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel
BuildRequires:	libstdc++-devel
BuildRequires:	glut-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRequires:	plib >= 1.2.0
BuildRequires:	zlib-devel
BuildRequires:	tcl-devel
BuildRequires:	metakit-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define _noautoreqdep libGL.so.1 libGLU.so.1

%description
SimGear is a set of open-source libraries designed to be used as
building blocks for quickly assembling 3d simulations, games, and
visualization applications.

The term "Simulation Kernel" is a bit presumptuous for us at this
point, but this is the direction we are heading with SimGear.

%description -l pl
SimGear to zestaw bibliotek zaprojektowanych do wykorzystania jako
klocki do szybkiego zestawiania tr�jwymiarowych symulacji, gier...

W tej chwili jest jeszcze troch� za wcze�nie na u�ywanie terminu
"J�dro Symulacji", ale to jest kierunek w kt�rym zmierza SimGear.

%package devel
Summary:	header files for SimGear
Summary(pl):	pliki nag��wkowe dla SimGear
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files neccessary to build SimGear applications.

%description devel -l pl
Pliki nag��wkowe potrzebne do budowania aplikacji z SimGearem.

%package static
Summary:	static SimGear libraries
Summary(pl):	statyczne biblioteki SimGear
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static SimGear libraries.

%description static -l pl
Statyczne biblioteki SimGear.

%prep
%setup -q
%patch0 -p1

%build
rm missing
libtoolize --force --copy
aclocal
autoconf
automake -a -c
%configure \
	--with-x \
	--with-tcl=/usr/lib
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc simgear/metakit/doc/*.html
%doc simgear/metakit/doc/api
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
