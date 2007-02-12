%define	rel	rc1
Summary:	Advanced shutdown utility
Summary(pl.UTF-8):	Zaawansowane narzędzie do restartowania
Name:		gshutdown
Version:	0.2
Release:	0.%{rel}.1
License:	GPL v2
Group:		Applications/System
Source0:	http://gshutdown.tuxfamily.org/release/gshutdown-0.2rc1.tar.gz
# Source0-md5:	f3b3c3eb86a4f18765bc30134a8a1464
Patch0:         %{name}-locale_names.patch
URL:		http://gshutdown.tuxfamily.org/
BuildRequires:	gtk+2-devel
BuildRequires:	libglade2-devel
BuildRequires:	libnotify-devel
Requires:	libglade2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GShutdown is an advanced shutdown utility which allows you to schedule
the shutdown, the restart of your computer of the logout.

%prep
%setup -q -n %{name}-%{version}%{rel}
%patch0 -p1

rm -f po/no.*

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%find_lang gshutdown --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post

%preun

%postun

%files -f gshutdown.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/gshutdown.png
%{_mandir}/man1/*
