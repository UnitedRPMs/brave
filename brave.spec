%{?nodejs_find_provides_and_requires}
%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}

%global branch 0.67.x

# Put here new versions of yarn
#https://github.com/yarnpkg/yarn/releases
%global y_ver 1.6.0

Name: brave
Summary: A web browser that stops ads and trackers by default. 
Group: Applications/Internet
URL: https://www.brave.com/
Version: 0.67.72
Release: 1%{?dist}
License: MPLv2.0
Source0: https://github.com/brave/brave-browser/archive/%{branch}.zip#/%{name}-browser-%{branch}.tar.gz
Source1: brave-snapshot
Source2: brave
#-------------------------------------
BuildRequires: git 
BuildRequires: ninja-build
BuildRequires: python2-devel
BuildRequires: libgnome-keyring-devel 
BuildRequires: xorg-x11-server-Xvfb
BuildRequires: nss-devel
BuildRequires: alsa-lib-devel
BuildRequires: gtk3-devel
BuildRequires: gendesk
BuildRequires: wget
BuildRequires: gcc-c++
%if 0%{?fedora} >= 29
BuildRequires:	python-unversioned-command
%endif
Provides: %{name}-browser = %{version}-%{release}
ExclusiveArch: x86_64

%description
Brave browser for Desktop and Laptop computers running Windows, OSX, and Linux.

%prep

%{S:1} -c %{branch}
%setup -T -D -n %{name}-browser-%{branch}

%build

# get yarn
wget -c https://github.com/yarnpkg/yarn/releases/download/v%{y_ver}/yarn-v%{y_ver}.tar.gz
tar xmzvf yarn-v1.6.0.tar.gz -C ~

# activate yarn
echo "export PATH=$PATH:~/yarn-v%{y_ver}/bin/:~/yarn-v%{y_ver}/lib/" >> ~/.bashrc

# get nvm

git clone git://github.com/creationix/nvm.git ~/nvm

# activate nvm

echo "source ~/nvm/nvm.sh" >> ~/.bashrc

source ~/.bashrc
nvm install 8
nvm use 8

# Begin the build
XCFLAGS="-g -O2 -fstack-protector-strong -Wformat -Werror=format-security -D_FORTIFY_SOURCE=2" XLDFLAGS="-Wl,-z,relro"

~/yarn-v%{y_ver}/bin/yarn install
#npm install home-path buffer-to-vinyl stream-combiner2 to-absolute-glob 
#npm install
#npm run init --python=python2.7 --target_os=linux --target_arch=x64
#npm run init --python=python2.7

# We need said a npm/yarn the path of binaries already installed... 
export PATH=$PATH:/usr/bin/:$PWD/node_modules/.bin/

# Now the installation
CHANNEL=dev ~/yarn-v%{y_ver}/bin/yarn run init 
#CHANNEL=dev npm run build-package

# create *.desktop file
gendesk -f -n \
          --pkgname="%{name}" \
          --pkgdesc="A web browser that stops ads and trackers by default" \
          --name="Brave" \
          --categories="Network;WebBrowser;"

%install

  install -d -m0755 %{buildroot}/%{_libdir}
  cp -a --reflink=auto brave-linux-x64 %{buildroot}/%{_libdir}/brave

  install -Dm0755 %{S:2} %{buildroot}/usr/bin/brave


  # desktop
  install -dm 755 $RPM_BUILD_ROOT/%{_datadir}/pixmaps/
  install -Dm644 res/dev/app.png $RPM_BUILD_ROOT/%{_datadir}/pixmaps/%{name}.png
  install -Dm644 "%{name}.desktop" "$RPM_BUILD_ROOT/%{_datadir}/applications/%{name}.desktop"

%files
%defattr(755, root, root)
%license LICENSE.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_libdir}/%{name}/


%changelog

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
