
Name: app-elasticsearch-plugin
Epoch: 1
Version: 1.0.0
Release: 1%{dist}
Summary: Elasticsearch Policies - Core
License: LGPLv3
Group: ClearOS/Libraries
Packager: eGloo
Vendor: WikiSuite
Source: app-elasticsearch-plugin-%{version}.tar.gz
Buildarch: noarch

%description
Elasticsearch Policies provide access control for the Elasticsearch app.

%package core
Summary: Elasticsearch Policies - Core
Requires: app-base-core
Requires: app-accounts-core

%description core
Elasticsearch Policies provide access control for the Elasticsearch app.

This package provides the core API and libraries.

%prep
%setup -q
%build

%install
mkdir -p -m 755 %{buildroot}/usr/clearos/apps/elasticsearch_plugin
cp -r * %{buildroot}/usr/clearos/apps/elasticsearch_plugin/

install -D -m 0644 packaging/elasticsearch.php %{buildroot}/var/clearos/accounts/plugins/elasticsearch.php

%post core
logger -p local6.notice -t installer 'app-elasticsearch-plugin-core - installing'

if [ $1 -eq 1 ]; then
    [ -x /usr/clearos/apps/elasticsearch_plugin/deploy/install ] && /usr/clearos/apps/elasticsearch_plugin/deploy/install
fi

[ -x /usr/clearos/apps/elasticsearch_plugin/deploy/upgrade ] && /usr/clearos/apps/elasticsearch_plugin/deploy/upgrade

exit 0

%preun core
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-elasticsearch-plugin-core - uninstalling'
    [ -x /usr/clearos/apps/elasticsearch_plugin/deploy/uninstall ] && /usr/clearos/apps/elasticsearch_plugin/deploy/uninstall
fi

exit 0

%files core
%defattr(-,root,root)
%exclude /usr/clearos/apps/elasticsearch_plugin/packaging
%exclude /usr/clearos/apps/elasticsearch_plugin/unify.json
%dir /usr/clearos/apps/elasticsearch_plugin
/usr/clearos/apps/elasticsearch_plugin/deploy
/usr/clearos/apps/elasticsearch_plugin/language
/var/clearos/accounts/plugins/elasticsearch.php
