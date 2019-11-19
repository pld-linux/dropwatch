Summary:	Kernel dropped packet monitor
Summary(pl.UTF-8):	Monitor pakietów odrzuconych przez jądro
Name:		dropwatch
Version:	1.4
Release:	18
License:	GPL v2+
Group:		Applications/System
Source0:	https://fedorahosted.org/releases/d/r/dropwatch/%{name}-%{version}.tbz2
# Source0-md5:	5145753b3e9255bd9b190251ba4d3bbf
Patch0:		np-Werror.patch
# dead
#URL:		https://fedorahosted.org/dropwatch
# is it "main" fork?
URL:		https://github.com/garekkream/dropwatch
BuildRequires:	binutils-devel
BuildRequires:	libnl-devel >= 3.2
BuildRequires:	linux-libc-headers
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	sed >= 4.0
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

cd src
%{__sed} -i -e 's,gcc,$(CC),g' Makefile
%{__sed} -i -e '/^CFLAGS/ s/$/ $(EXTRA_CFLAGS)/' Makefile
%{__sed} -i -e '/^LDFLAGS/ s/$/ $(EXTRA_LDFLAGS)/' Makefile

%build
%{__make} -C src \
	CC="%{__cc}" \
	EXTRA_CFLAGS="%{rpmcflags}" \
	EXTRA_LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install -p src/dropwatch $RPM_BUILD_ROOT%{_bindir}
cp -p doc/dropwatch.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/dropwatch
%{_mandir}/man1/dropwatch.1*
