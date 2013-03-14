
%define plugin	eggtimer
%define name	vdr-plugin-%plugin
%define version	0.9.5
%define rel	14

Summary:	VDR plugin: Eggtimer
Name:		%name
Version:	%version
Release:	%rel
Group:		Video
License:	GPL
URL:		http://vaasa.wi-bw.tfh-wildau.de/~pjuszack/digicam/index_en.html
Source:		http://194.95.44.38/~pjuszack/digicam/download/vdr-%plugin-%version.tar.bz2
Patch0:		vdr-eggtimer-0.9.4-fix-menu.h.patch
Patch1:		eggtimer-0.9.5-i18n-1.6.patch
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
%vdr_plugin_install

install -D -m644 eggtimer.conf %{buildroot}%{vdr_plugin_cfgdir}/eggtimer.conf

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY eggtimer.conf.*
%config(noreplace) %{vdr_plugin_cfgdir}/eggtimer.conf




%changelog
* Thu Jul 30 2009 Anssi Hannula <anssi@mandriva.org> 0.9.5-12mdv2011.0
+ Revision: 404566
- rebuild due to BS building the previous release against wrong VDR on i586

* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.9.5-11mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Sat Mar 21 2009 Anssi Hannula <anssi@mandriva.org> 0.9.5-10mdv2009.1
+ Revision: 359703
- rediff i18n patch
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.9.5-9mdv2009.0
+ Revision: 197923
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.9.5-8mdv2009.0
+ Revision: 197658
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt to gettext i18n of VDR 1.6 (semi-automatic patch)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.9.5-7mdv2008.1
+ Revision: 145082
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.9.5-6mdv2008.1
+ Revision: 103088
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.9.5-5mdv2008.0
+ Revision: 49994
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.9.5-4mdv2008.0
+ Revision: 42080
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.9.5-3mdv2008.0
+ Revision: 22746
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.9.5-2mdv2007.0
+ Revision: 90915
- rebuild for new vdr

* Fri Nov 03 2006 Anssi Hannula <anssi@mandriva.org> 0.9.5-1mdv2007.1
+ Revision: 76350
- 0.9.5

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.9.4-8mdv2007.1
+ Revision: 73987
- rebuild for new vdr
- Import vdr-plugin-eggtimer

* Sun Sep 10 2006 Anssi Hannula <anssi@mandriva.org> 0.9.4-7mdv2007.0
- patch0: fix includes

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.9.4-6mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.9.4-5mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.9.4-4mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.9.4-3mdv2007.0
- rebuild for new vdr

* Tue Jul 11 2006 Anssi Hannula <anssi@mandriva.org> 0.9.4-2mdv2007.0
- fix URL

* Tue Jul 11 2006 Anssi Hannula <anssi@mandriva.org> 0.9.4-1mdv2007.0
- initial Mandriva release

