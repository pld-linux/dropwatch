Summary:	Kernel dropped packet monitor
Name:		dropwatch
Version:	1.4
Release:	1
Source0:	https://fedorahosted.org/releases/d/r/dropwatch/%{name}-%{version}.tbz2
# Source0-md5:	5145753b3e9255bd9b190251ba4d3bbf
License:	GPLv2+
Group:		Applications/System
URL:		http://fedorahosted.org/dropwatch
BuildRequires:	binutils-devel
BuildRequires:	libnl-devel
BuildRequires:	linux-libc-headers
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dropwatch is an utility to interface to the kernel to monitor for
dropped network packets.

%prep
%setup -q

%build
cd src
export CFLAGS=$RPM_OPT_FLAGS
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install src/dropwatch $RPM_BUILD_ROOT%{_bindir}
install doc/dropwatch.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
