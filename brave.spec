%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}

Name: brave
Summary: A web browser that stops ads and trackers by default. 
Group: Applications/Internet
URL: https://www.brave.com/
Version: 1.25.68
Release: 7%{?dist}
License: MPLv2.0
Source0: https://github.com/brave/brave-browser/releases/download/v%{version}/brave-browser-%{version}-linux-amd64.zip
Source1: logo.png
Source2: brave
#-------------------------------------
BuildRequires:	gendesk
%if 0%{?fedora} >= 29
Requires:	python-unversioned-command
%endif
Recommends:	chromium-pepper-flash
ExclusiveArch: x86_64

%description
Brave browser for Desktop and Laptop computers running Windows, OSX, and Linux.

%prep

%setup -c brave-%{version}

%build

# create *.desktop file
gendesk -f -n \
          --pkgname="%{name}" \
          --pkgdesc="A web browser that stops ads and trackers by default" \
          --name="Brave" \
          --categories="Network;WebBrowser;"

%install

  install -d -m0755 %{buildroot}/%{_libdir}
  cp -a --reflink=auto %{_builddir}/brave-%{version} %{buildroot}/%{_libdir}/brave

  install -Dm0755 %{S:2} %{buildroot}/usr/bin/brave


  # desktop
  install -dm 755 $RPM_BUILD_ROOT/%{_datadir}/pixmaps/
  install -Dm644 %{S:1} $RPM_BUILD_ROOT/%{_datadir}/pixmaps/%{name}.png
  install -Dm644 "%{name}.desktop" "$RPM_BUILD_ROOT/%{_datadir}/applications/%{name}.desktop"

%files
%defattr(755, root, root)
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_libdir}/%{name}/


%changelog

* Thu Jun 03 2021 David Va <davidva AT tuta DOT io> 1.25.68-7
- Updated to 1.25.68

* Sat Mar 20 2021 David Va <davidva AT tuta DOT io> 1.23.45-7
- Updated to 1.23.45

* Wed Nov 18 2020 David Va <davidva AT tuta DOT io> 1.18.55-7
- Updated to 1.18.55

* Wed Sep 30 2020 David Va <davidva AT tuta DOT io> 1.16.47-7
- Updated to 1.16.47

* Mon Aug 31 2020 David Va <davidva AT tuta DOT io> 1.14.71-7
- Updated to 1.14.71

* Mon Jul 13 2020 David Va <davidva AT tuta DOT io> 1.12.85-7
- Updated to 1.12.85

* Mon Apr 20 2020 David Va <davidva AT tuta DOT io> 1.7.98-7
- Updated to 1.7.98

* Fri Mar 20 2020 David Va <davidva AT tuta DOT io> 1.5.114-7
- Updated to 1.5.114

* Thu Jan 16 2020 David Va <davidva AT tuta DOT io> 1.3.92-7
- Updated to 1.3.92

* Fri Dec 06 2019 David Va <davidva AT tuta DOT io> 1.2.21-7
- Updated to 1.2.21

* Tue Nov 26 2019 David Va <davidva AT tuta DOT io> 1.1.11-7
- Updated to 1.1.11

* Thu Nov 14 2019 David Va <davidva AT tuta DOT io> 1.0.0-7
- Updated to 1.0.0

* Tue Oct 29 2019 David Va <davidva AT tuta DOT io> 0.73.37-1
- Updated to 0.73.37

* Wed Sep 18 2019 David Va <davidva AT tuta DOT io> 0.72.32-1
- Updated to 0.72.32

* Wed Sep 11 2019 David Va <davidva AT tuta DOT io> 0.71.72-1
- Updated to 0.71.72

* Tue Sep 03 2019 David Va <davidva AT tuta DOT io> 0.71.63-1
- Updated to 0.71.63

* Thu Aug 29 2019 David Va <davidva AT tuta DOT io> 0.71.47-1
- Updated to 0.71.47

* Thu Aug 22 2019 David Va <davidva AT tuta DOT io> 0.71.25-1
- Updated to 0.71.25

* Thu Aug 15 2019 David Va <davidva AT tuta DOT io> 0.70.66-1
- Updated to 0.70.66

* Tue Aug 13 2019 David Va <davidva AT tuta DOT io> 0.70.57-1
- Updated to 0.70.57

* Wed Aug 07 2019 David Va <davidva AT tuta DOT io> 0.69.100-1
- Updated to 0.69.100

* Thu Jul 18 2019 David Va <davidva AT tuta DOT io> 0.69.77-1
- Updated to 0.69.77

* Thu Jul 11 2019 David Va <davidva AT tuta DOT io> 0.69.51-1
- Updated to 0.69.51

* Fri Jul 05 2019 David Va <davidva AT tuta DOT io> 0.69.33-1
- Updated to 0.69.33

* Sun Jun 30 2019 David Va <davidva AT tuta DOT io> 0.69.17-1
- Updated to 0.69.17

* Tue Jun 25 2019 David Va <davidva AT tuta DOT io> 0.68.78-1
- Updated to 0.68.78

* Sat Jun 15 2019 David Va <davidva AT tuta DOT io> 0.68.50-1
- Updated to 0.68.50

* Sat Jun 01 2019 David Va <davidva AT tuta DOT io> 0.67.72-1
- Updated to 0.67.72

* Tue Dec 11 2018 David Va <davidva AT tuta DOT io> 0.25.203-1
- Updated to 0.25.203

* Wed Oct 10 2018 David Va <davidva AT tuta DOT io> 0.25.2-1
- Updated to 0.25.2

* Thu Sep 20 2018 David Va <davidva AT tuta DOT io> 0.24.0-1
- Updated to 0.24.0

* Wed Sep 12 2018 David Va <davidva AT tuta DOT io> 0.23.107-1
- Updated to 0.23.107

* Sat Aug 11 2018 David Va <davidva AT tuta DOT io> 0.23.79-1
- Updated to 0.23.79

* Wed Aug 01 2018 David Va <davidva AT tuta DOT io> 0.23.73-1
- Updated to 0.23.73

* Sat Jul 21 2018 David Va <davidjeremias82 AT gmail DOT com> - 0.23.39-1
- Updated to 0.23.39

* Sun Jul 08 2018 David Va <davidjeremias82 AT gmail DOT com> - 0.23.31-1
- Updated to 0.23.31

* Mon Jul 02 2018 David Va <davidjeremias82 AT gmail DOT com> - 0.23.19-1
- Updated to 0.23.19

* Fri Jun 15 2018 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.22.810-1
- Updated to 0.22.810

* Wed Jun 06 2018 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.22.727-1
- Updated to 0.22.727

* Sun May 06 2018 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.22.669-1
- Updated to 0.22.669
- Again to npm

* Thu Apr 12 2018 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.22.13-1
- Updated to 0.22.13

* Wed Mar 07 2018 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.21.18-1
- Updated to 0.21.18

* Fri Feb 16 2018 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.20.42-1
- Updated to 0.20.42

* Mon Feb 05 2018 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.20.31-1
- Updated to 0.20.31

* Sat Feb 03 2018 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.20.30-1
- Updsted to 0.20.30

* Tue Jan 30 2018 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.19.147-1
- Updated to 0.19.147

* Tue Jan 23 2018 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.19.143-1
- Updated to 0.19.143

* Tue Jan 16 2018 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.19.136-1
- Updated to 0.19.136

* Thu Dec 28 2017 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.19.123-1
- Updated to 0.19.123

* Mon Dec 18 2017 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.19.116-1
- Updated to 0.19.116

* Sat Dec 02 2017 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.19.105-1
- Updated to 0.19.105

* Thu Nov 16 2017 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.19.95-1
- Updated to 0.19.95
- Changed to yarn

* Mon Nov 13 2017 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.19.89-1
- Updated 0.19.89

* Sat Nov 11 2017 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.19.88-1
- Updated 0.19.88

* Sun Nov 05 2017 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.19.80-1
- Updated 0.19.80

* Tue Oct 31 2017 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.19.70-1
- Updated 0.19.70

* Wed May 18 2016 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.10.3-1
- Updated 0.10.3

* Wed May 18 2016 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.9.6-1
- initial build
