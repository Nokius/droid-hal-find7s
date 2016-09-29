%define device find7s
%define vendor oppo

%define vendor_pretty OPPO
%define device_pretty Find7s

%define installable_zip 1

%define straggler_files \
/selinux_version\
/service_contexts\
%{nil}

%include rpm/dhd/droid-hal-device.inc
