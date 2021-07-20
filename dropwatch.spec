Summary:	Kernel dropped packet monitor
Summary(pl.UTF-8):	Monitor pakietów odrzuconych przez jądro
Name:		dropwatch
Version:	1.5.3
Release:	4
License:	GPL v2+
Group:		Applications/System
Source0:	https://github.com/nhorman/dropwatch/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	64527bb669393e45b9b21f0b91c574c0
Patch0:		%{name}-no_werror.patch
URL:		https://github.com/nhorman/dropwatch
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	binutils-devel
BuildRequires:	libnl-devel >= 3.2
BuildRequires:	libpcap-devel
BuildRequires:	libtool
BuildRequires:	linux-libc-headers
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dropwatch is an utility to interface to the kernel to monitor for
dropped network packets.

%description -l pl.UTF-8
dropwatch to narzędzie współpracujące z jądrem w celu monitorowania
odrzuconych pakietów sieciowych.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
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

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/dropwatch
%attr(755,root,root) %{_bindir}/dwdump
%{_mandir}/man1/dropwatch.1*
