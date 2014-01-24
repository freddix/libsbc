Summary:	Bluetooth Subband Codec (SBC) library
Name:		libsbc
Version:	1.2
Release:	1
License:	GPL/LGPL
Group:		Libraries
Source0:	http://www.kernel.org/pub/linux/bluetooth/sbc-%{version}.tar.xz
# Source0-md5:	ec65c444ad4c32aa85702641045b19e9
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bluetooth Subband Codec (SBC) library.

%package devel
Summary:	Header files for SBC library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for SBC library.

%prep
%setup -qn sbc-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/sbc*
%attr(755,root,root) %ghost %{_libdir}/libsbc.so.1
%attr(755,root,root) %{_libdir}/libsbc.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsbc.so
%{_includedir}/sbc
%{_pkgconfigdir}/sbc.pc

