Name     : dolittle-edge
Version  : 1.0.2
Release  : 1
License  : MIT
Summary  : Dolittle Edge
URL      : https://github.com/dolittle-edge/dolittle-edge-clearlinux
Source0  : ./dolittle-configure-openvpn
Source1  : ./docker-logrotate.conf

%description

%prep

%build

%install
install -D -m 755 %{SOURCE0} %{buildroot}/usr/bin/dolittle-configure-openvpn
install -D -m 644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/docker.service.d/90-dolittle-logrotate.conf

%post

%preun

%postun

%files
%defattr(-, root, root, -)

# bins
/usr/bin/dolittle-configure-openvpn

# conf
/usr/lib/systemd/system/docker.service.d/90-dolittle-logrotate.conf

%changelog

