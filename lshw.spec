#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : lshw
Version  : 1
Release  : 3
URL      : http://www.ezix.org/software/files/lshw-B.02.18.tar.gz
Source0  : http://www.ezix.org/software/files/lshw-B.02.18.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: lshw-bin
Requires: lshw-locales
Requires: lshw-data
Requires: lshw-doc
Patch1: 0001-Avoid-crash-in-scan-dmi-sysfs-when-running-as-non-root.patch

%description
lshw: HardWare LiSter for Linux
===============================
lshw is a small tool to provide detailed information on the hardware configuration of the machine. It can report exact memory configuration, firmware version, mainboard configuration, CPU version and speed, cache configuration, bus speed, etc. on DMI-capable x86 or EFI (IA-64) systems and on some ARM and PowerPC machines (PowerMac G4 is known to work).

%package bin
Summary: bin components for the lshw package.
Group: Binaries
Requires: lshw-data

%description bin
bin components for the lshw package.


%package data
Summary: data components for the lshw package.
Group: Data

%description data
data components for the lshw package.


%package doc
Summary: doc components for the lshw package.
Group: Documentation

%description doc
doc components for the lshw package.


%package locales
Summary: locales components for the lshw package.
Group: Default

%description locales
locales components for the lshw package.


%prep
%setup -q -n lshw-B.02.18
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507568169
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1507568169
rm -rf %{buildroot}
%make_install
%find_lang lshw

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lshw

%files data
%defattr(-,root,root,-)
/usr/share/lshw/manuf.txt
/usr/share/lshw/oui.txt
/usr/share/lshw/pci.ids
/usr/share/lshw/usb.ids

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files locales -f lshw.lang
%defattr(-,root,root,-)

