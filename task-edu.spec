
%define name task-edu
%define version 1
%define release %mkrel 2

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
