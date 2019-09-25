Name     : dolittle-edge
Version  : 1.1.0
Release  : 1
License  : MIT
Summary  : Dolittle Edge
URL      : https://github.com/dolittle-edge/dolittle-edge-clearlinux
Source0  : file://dolittle-configure-openvpn
Source1  : file://docker-logrotate.conf
Source2  : file://60-prompt-edge.sh

%description

%prep

%build

%install
install -D -m 755 %{SOURCE0} %{buildroot}/usr/bin/dolittle-configure-openvpn
install -D -m 644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/docker.service.d/90-dolittle-logrotate.conf
install -D -m 644 %{SOURCE2} %{buildroot}/usr/share/defaults/etc/profile.d/60-prompt-edge.conf

%post

%preun

%postun

%files
%defattr(-, root, root, -)

# bins
/usr/bin/dolittle-configure-openvpn

# conf
/usr/lib/systemd/system/docker.service.d/90-dolittle-logrotate.conf

# scripts
/usr/share/defaults/etc/profile.d/60-prompt-edge.conf

%changelog

