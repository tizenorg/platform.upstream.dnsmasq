Name:       dnsmasq
Summary:    dnsmasq, DNS forwarder.
Version:    2.57
Release:    5
Group:      TO_BE/FILLED_IN
License:    TO BE FILLED IN
Source0:    %{name}-%{version}.tar.gz
Source1001: 	dnsmasq.manifest
BuildRequires: cmake
BuildRequires: pkgconfig(dbus-1)

%description
Dnsmasq is a lightweight, easy to configure DNS forwarder and DHCP server.

%prep
%setup -q
cp %{SOURCE1001} .

%build
cmake . -DCMAKE_INSTALL_PREFIX=%{_prefix}
make %{?jobs:-j%jobs}

%post
mkdir -p /opt/var/lib/misc

%install
rm -rf %{buildroot}
%make_install

%files
%manifest %{name}.manifest
%{_bindir}/dnsmasq

%changelog
* Fri Nov 02 2012 Seungyoun Ju <sy39.ju@samsung.com> 2.57-5
- Default manifest file is added

* Mon Apr 16 2012 Seungyoun Ju <sy39.ju@samsung.com> 2.57-4
- "/opt/var/lib/misc" directory for lease file is created explicitly
