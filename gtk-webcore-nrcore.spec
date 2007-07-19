%define snap	125
Summary:	Port of WebCore HTML rendering engine to GTK+
Name:		gtk-webcore-nrcore
Version:	0.5.3
Release:	0.%{snap}.1
Source0:	%{name}-%{snap}.tar.bz2
# Source0-md5:	bef9ba8f8dd1036e72742ed09544f315
License:	LGPL
Group:		X11/Libraries
URL:		http://gtk-webcore.sourceforge.net/
BuildRequires:	glib2-devel
BuildRequires:	gtk+2-devel
BuildRequires:	gtk-webcore-jscore-libs-devel
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gtk-webcore-nrcore is a port of the WebCore HTML rendering engine to
GTK+. WebCore is in turn a port of the KDE project's KHTML rendering
engine.

%package libs
Summary:	Shared library for gtk-webcore-nrcore
Group:		X11/Libraries

%description libs
gtk-webcore-nrcore is a port of the WebCore HTML rendering engine to
GTK+. WebCore is in turn a port of the KDE project's KHTML rendering
engine.

%package libs-devel
Summary:	Development library for gtk-webcore-nrcore
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description libs-devel
gtk-webcore-nrcore is a port of the WebCore HTML rendering engine to
GTK+. WebCore is in turn a port of the KDE project's KHTML rendering
engine.

%prep
%setup -q -n %{name}

%build
./autogen.sh
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post libs	-p /sbin/ldconfig
%postun libs	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS-Gtk+WebCore ChangeLog-Gtk+WebCore LICENSE-APPLE LICENSE-Nokia README-Gtk+WebCore TODO-Gtk+WebCore
%{_datadir}/%{name}

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %_libdir/lib*.so.*

%files libs-devel
%defattr(644,root,root,755)
%doc HACKING-Gtk+WebCore
%{_libdir}/lib*.so
%{_libdir}/lib*.a
%{_includedir}/gtk-webcore/NRCore
%{_pkgconfigdir}/%{name}.pc
