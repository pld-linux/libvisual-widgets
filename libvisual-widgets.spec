Summary:	Libvisual widgets
Summary(pl.UTF-8):   Widgety dla libvisual
Name:		libvisual-widgets
Version:	0.2.0
%define	bver	20041130
Release:	0.%{bver}.1
License:	GPL
Group:		Libraries
Source0:	%{name}-%{bver}.tar.bz2
# Source0-md5:	9838d54400375ebe6ea1b5a7887dc574
URL:		http://libvisual.sourceforge.net/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.14
BuildRoot:	%{tmpdir}/%{name}-%{bver}-root-%(id -u -n)

%description
libvisual-widgets is a package that contains standard user interface
widgets that are to be used together with libvisual itself.

%description -l pl.UTF-8
libvisual-widgets to pakiet zawierający standardowe widgety interfejsu
użytkownika, które mogą być używane również przez libvisual.

%package devel
Summary:	Header files for libvisual-widgets library
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki libvisual-widgets
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libvisual-widgets library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki-widgets libvisual.

%package static
Summary:	Static libvisual-widgets library
Summary(pl.UTF-8):   Statyczna biblioteka libvisual-widgets
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libvisual-widgets library.

%description static -l pl.UTF-8
Statyczna biblioteka libvisual-widgets.

%prep
%setup -q -n %{name}-%{bver}

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--enable-static
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/lvw
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
