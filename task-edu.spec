
%define name task-edu
%define version 1
%define release 3

Summary: Task packages for games
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group:   Education
Url: http://wiki.mandriva.com/en/Docs
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Suggests: kdeedu4
Suggests: educazionik
Suggests: kdegames4
Suggests: semantik
Suggests: tuxpaint
Suggests: tuxpaint-stamps
Suggests: scribus
Suggests: celestia
Suggests: stellarium
Suggests: drgeo
Suggests: freemind
Suggests: gcompris gcompris-music

%description
This task package Suggests edu packages selected by Mandriva.

%files


%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 1-2mdv2011.0
+ Revision: 615111
- the mass rebuild of 2010.1 packages

* Mon Dec 21 2009 Angelo Naselli <anaselli@mandriva.org> 1-1mdv2010.1
+ Revision: 480630
- Fixed gcompris
  Added educazionik (for Italian people)

* Sat Nov 28 2009 Angelo Naselli <anaselli@mandriva.org> 0.1-2mdv2010.1
+ Revision: 470862
- added tuxpaint-stamps

* Thu Oct 01 2009 Angelo Naselli <anaselli@mandriva.org> 0.1-1mdv2010.0
+ Revision: 452146
- import task-edu

