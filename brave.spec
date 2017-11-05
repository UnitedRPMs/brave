%{?nodejs_find_provides_and_requires}
%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}

%global commit0 7d07299a5d462d3c9ae32cfbfbe7296cc57c89b9
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

Name: brave
Summary: A web browser that stops ads and trackers by default. 
Group: Applications/Internet
URL: https://www.brave.com/
Version: 0.19.80
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
Provides: %{name}-browser = %{version}-%{release}
ExclusiveArch: x86_64

%description
Brave browser for Desktop and Laptop computers running Windows, OSX, and Linux.

%prep

%{S:1} -c %{commit0}
%setup -T -D -n %{name}-%{shortcommit0}

%build

# get nvm

git clone git://github.com/creationix/nvm.git ~/nvm

# activate nvm

echo "source ~/nvm/nvm.sh" >> ~/.bashrc

source ~/.bashrc
nvm install 7
nvm use 7

XCFLAGS="-g -O2 -fstack-protector-strong -Wformat -Werror=format-security -D_FORTIFY_SOURCE=2" XLDFLAGS="-Wl,-z,relro"

npm cache clean
npm config set registry http://registry.npmjs.org/
npm install

# We need said a npm the path of binaries already installed... 
export PATH=$PATH:/usr/bin/:$PWD/node_modules/.bin/

# Now the installation
CHANNEL=dev npm run build-package

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
cp -rf Brave-linux-x64/* $RPM_BUILD_ROOT%{_libdir}/%{name}/

cp -f %{S:2} %{buildroot}/%{_bindir}/
chmod a+x %{buildroot}/%{_bindir}/%{name}
chmod a+x %{buildroot}/%{_libdir}/%{name}/%{name}

  # desktop
  install -Dm0644 res/app.png "$RPM_BUILD_ROOT/%{_datadir}/pixmaps/%{name}.png"
  install -Dm644 "%{name}.desktop" "$RPM_BUILD_ROOT/%{_datadir}/applications/%{name}.desktop"

%files
%defattr(755, root, root)
%license LICENSE.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_libdir}/%{name}/


%changelog

* Sun Nov 05 2017 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.19.80-1
- Updated 0.19.80

* Tue Oct 31 2017 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.19.70-1
- Updated 0.19.70

* Wed May 18 2016 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.10.3-1
- Updated 0.10.3

* Wed May 18 2016 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.9.6-1
- initial build
