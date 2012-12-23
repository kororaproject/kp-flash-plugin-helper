Name:		flash-plugin-helper
Version:	0.2
Release:	1%{?dist}.1
Summary:	Adobe Flash plugin installer
License:	GPLv3+
Requires:	kororaa-extras >= 0.5-1 coreutils flash-plugin pulseaudio-libs alsa-plugins-pulseaudio libcurl

%description
Install this instead of flash-plugin from Adobe. This helper
installer will manage the process for you, including dependencies,
setting up all of the required plugin directories for Firefox and
Google Chrome, etc.

%install
mkdir -p %{buildroot}/opt/google/chrome/plugins
mkdir -p %{buildroot}/%{_libdir}/chromium-browser/plugins
ln -sf %{_libdir}/flash-plugin/libflashplayer.so %{buildroot}/opt/google/chrome/plugins/libflashplayer.so
ln -sf %{_libdir}/flash-plugin/libflashplayer.so %{buildroot}/%{_libdir}/chromium-browser/plugins/libflashplayer.so

%post

%files
/opt/google/chrome/plugins/libflashplayer.so
%{_libdir}/chromium-browser/plugins/libflashplayer.so

%changelog
* Wed Oct 05 2011 Chris Smart <chris@kororaa.org> 0.2-1
- Support for 64bit Flash.

* Wed Aug 31 2011 Chris Smart <chris@kororaa.org> 0.1-2
- Fixed the way links are created, else they are removed on upgrade.

* Mon Apr 25 2011 Chris Smart <chris@kororaa.org> 0.1-1
- Initial spec.

