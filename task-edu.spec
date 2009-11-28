
%define name task-edu
%define version 0.1
%define release %mkrel 2

Summary: Task packages for games
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group:   Education
Url: http://wiki.mandriva.com/en/Docs/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Suggests: kdeedu4
Suggests: kdegames4
Suggests: semantik
Suggests: tuxpaint
Suggests: tuxpaint-stamps
Suggests: scribus
Suggests: celestia
Suggests: stellarium
Suggests: drgeo
Suggests: freemind
Suggests: gcompris
Suggests: gcompris-sounds-da gcompris-sounds-de gcompris-sounds-en gcompris-sounds-es gcompris-sounds-eu
Suggests: gcompris-sounds-fi gcompris-sounds-fr gcompris-sounds-hu gcompris-sounds-it
Suggests: gcompris-sounds-nl gcompris-sounds-pt gcompris-sounds-ru gcompris-sounds-sv

%description
This task package Suggests edu packages selected by Mandriva.

%files
