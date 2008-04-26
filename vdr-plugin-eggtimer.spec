
%define plugin	eggtimer
%define name	vdr-plugin-%plugin
%define version	0.9.5
%define rel	8

Summary:	VDR plugin: Eggtimer
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://vaasa.wi-bw.tfh-wildau.de/~pjuszack/digicam/index_en.html
Source:		http://194.95.44.38/~pjuszack/digicam/download/vdr-%plugin-%version.tar.bz2
Patch0:		vdr-eggtimer-0.9.4-fix-menu.h.patch
Patch1:		eggtimer-0.9.5-i18n-1.6.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
This is a plugin for the Video Disc Recorder (VDR). It can be used
to be reminded to certain things you will maybe forget when watching
TV. You can also let it switch to a channel or execute a command
from VDRs commands.conf at a certain point of time.

Examples: tea is ready, switch to a channel, shutdown VDR after
recording ...

%prep
%setup -q -n %plugin-%version
%patch0 -p1 -b .includes
%patch1 -p1
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

install -D -m644 eggtimer.conf %{buildroot}%{_vdr_plugin_cfgdir}/eggtimer.conf

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY eggtimer.conf.*
%config(noreplace) %{_vdr_plugin_cfgdir}/eggtimer.conf


