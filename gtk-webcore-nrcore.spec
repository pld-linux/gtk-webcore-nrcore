%define snap	125
Summary:	Port of WebCore HTML rendering engine to GTK+
Summary(pl.UTF-8):	Port silnika renderującego HTML WebCore do GTK+
Name:		gtk-webcore-nrcore
Version:	0.5.3
Release:	0.%{snap}.1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	%{name}-%{snap}.tar.bz2
# Source0-md5:	bef9ba8f8dd1036e72742ed09544f315
URL:		http://gtk-webcore.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.2.0
BuildRequires:	gtk+2-devel >= 2:2.2.0
BuildRequires:	gtk-webcore-jscore-libs-devel >= 0.5.3
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libxml2-devel >= 1:2.6.0
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libXt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gtk-webcore-nrcore is a port of the WebCore HTML rendering engine to
GTK+. WebCore is in turn a port of the KDE project's KHTML rendering
engine.

%description -l pl.UTF-8
gtk-webcore-nrcore to port silnika renderującego HTML WebCore do GTK+.
WebCore to z kolei port silnika renderującego KHTML z projektu KDE.

%package libs
Summary:	Shared library for gtk-webcore-nrcore
Summary(pl.UTF-8):	Biblioteka współdzielona gtk-webcore-nrcore
Group:		X11/Libraries
Requires:	glib2 >= 1:2.2.0
Requires:	gtk+2 >= 2:2.2.0
Requires:	gtk-webcore-jscore-libs >= 0.5.3
Requires:	libxml2 >= 1:2.6.0

%description libs
gtk-webcore-nrcore is a port of the WebCore HTML rendering engine to
GTK+. WebCore is in turn a port of the KDE project's KHTML rendering
engine.

%description libs -l pl.UTF-8
gtk-webcore-nrcore to port silnika renderującego HTML WebCore do GTK+.
WebCore to z kolei port silnika renderującego KHTML z projektu KDE.

%package libs-devel
Summary:	Development files for gtk-webcore-nrcore
Summary(pl.UTF-8):	Pliki programistyczne gtk-webcore-nrcore
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel >= 1:2.2.0
Requires:	gtk+2-devel >= 2:2.2.0
Requires:	gtk-webcore-jscore-libs-devel >= 0.5.3
Requires:	libxml2-devel >= 1:2.6.0
Requires:	xorg-lib-libXt-devel

%description libs-devel
Development files for gtk-webcore-nrcore.

%description libs-devel -l pl.UTF-8
Pliki programistyczne gtk-webcore-nrcore.

%package libs-static
Summary:	Static gtk-webcore-nrcore library
Summary(pl.UTF-8):	Statyczna biblioteka gtk-webcore-nrcore
Group:		X11/Development/Libraries
Requires:	%{name}-libs-devel = %{version}-%{release}

%description libs-static
Static gtk-webcore-nrcore library.

%description libs-static -l pl.UTF-8
Statyczna biblioteka gtk-webcore-nrcore.

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS-Gtk+WebCore ChangeLog-Gtk+WebCore LICENSE-APPLE LICENSE-Nokia README-Gtk+WebCore TODO-Gtk+WebCore
%{_datadir}/%{name}

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtk_webcore_nrcore.so.*.*.*

%files libs-devel
%defattr(644,root,root,755)
%doc HACKING-Gtk+WebCore
%attr(755,root,root) %{_libdir}/libgtk_webcore_nrcore.so
%{_libdir}/libgtk_webcore_nrcore.la
%{_includedir}/gtk-webcore/NRCore
%{_pkgconfigdir}/%{name}.pc

%files libs-static
%defattr(644,root,root,755)
%{_libdir}/libgtk_webcore_nrcore.a
