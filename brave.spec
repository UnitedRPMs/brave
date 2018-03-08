%{?nodejs_find_provides_and_requires}
%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}

%global commit0 580be782bc37ed8580dd22f79e1d2d355fddfb89
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

# Put here new versions of yarn
#https://github.com/yarnpkg/yarn/releases
%global y_ver 1.3.2

Name: brave
Summary: A web browser that stops ads and trackers by default. 
Group: Applications/Internet
URL: https://www.brave.com/
Version: 0.21.18
Release: 1%{?gver}%{?dist}
License: MPLv2.0
Source0: https://github.com/brave/browser-laptop/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
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
Provides: %{name}-browser = %{version}-%{release}
ExclusiveArch: x86_64

%description
Brave browser for Desktop and Laptop computers running Windows, OSX, and Linux.

%prep

%{S:1} -c %{commit0}
%setup -T -D -n %{name}-%{shortcommit0}

%build

# get yarn
wget -c https://github.com/yarnpkg/yarn/releases/download/v%{y_ver}/yarn-v%{y_ver}.tar.gz
tar xmzvf yarn-v1.3.2.tar.gz -C ~

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

# We need said a npm/yarn the path of binaries already installed... 
export PATH=$PATH:/usr/bin/:$PWD/node_modules/.bin/

# Now the installation
CHANNEL=dev ~/yarn-v%{y_ver}/bin/yarn run build-package

# create *.desktop file
gendesk -f -n \
          --pkgname="%{name}" \
          --pkgdesc="A web browser that stops ads and trackers by default" \
          --name="Brave" \
          --categories="Network;WebBrowser;"

%install

# Make destiny directories
install -dm 755 %{buildroot}/%{_libdir}/%{name} \
%{buildroot}/%{_bindir}

# Move to correct path
cp -rf brave-linux-x64/* $RPM_BUILD_ROOT%{_libdir}/%{name}/

cp -f %{S:2} %{buildroot}/%{_bindir}/
chmod a+x %{buildroot}/%{_bindir}/%{name}
chmod a+x %{buildroot}/%{_libdir}/%{name}/%{name}

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
