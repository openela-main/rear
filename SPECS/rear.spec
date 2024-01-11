%define debug_package %{nil}

Summary:    Relax-and-Recover is a Linux disaster recovery and system migration tool
Name:       rear
Version:    2.6
Release:    10%{?dist}
License:    GPLv3
Group:      Applications/File
URL:        http://relax-and-recover.org/

Source0:    https://github.com/rear/rear/archive/%{version}.tar.gz#/rear-%{version}.tar.gz
Patch4:  rear-bz1492177-warning.patch
Patch29: rear-bz1832394.patch
Patch30: rear-sfdc02772301.patch
Patch31: rear-bz1945869.patch
Patch32: rear-bz1958247.patch
Patch33: rear-bz1930662.patch
Patch34: rear-asciidoc.patch
Patch35: rear-bz1983013.patch
Patch36: rear-bz1993296.patch
Patch37: rear-bz1747468.patch
Patch38: rear-bz2049091.patch
Patch39: rear-pr2675.patch
Patch40: rear-bz2048454.patch
Patch41: rear-bz2035939.patch
Patch42: rear-bz2083272.patch
Patch43: rear-bz2111049.patch
Patch44: rear-bz2104005.patch
Patch48: rear-bz2111059.patch
Patch49: pxe-rsync-output.patch
Patch50: rear-bz2119501.patch
Patch51: rear-bz2120736.patch
Patch52: rear-bz2091163.patch
Patch53: rear-bz2130945.patch
Patch54: rear-bz2131946.patch
Patch56: s390-no-clobber-disks.patch
Patch58: rear-device-shrinking-bz2223895.patch
Patch59: rear-usb-uefi-part-size-bz2228402.patch
Patch60: rear-luks-key-bz2228779.patch
Patch61: rear-uefi-usb-secureboot-bz2196445.patch
Patch62: rear-vg-command-not-found-bz2121476.patch

### Dependencies on all distributions
BuildRequires:   asciidoc
Requires:   binutils
Requires:   ethtool
Requires:   gzip
Requires:   iputils
Requires:   parted
Requires:   tar
Requires:   openssl
Requires:   gawk
Requires:   attr
Requires:   bc
Requires:   file
Requires:   dhcp-client

### If you require NFS, you may need the below packages
#Requires:  nfsclient portmap rpcbind

### We drop LSB requirements because it pulls in too many dependencies
### The OS is hardcoded in /etc/rear/os.conf instead
#Requires:  redhat-lsb

### Required for Bacula/MySQL support
#Requires:  bacula-mysql

### Required for OBDR
#Requires:  lsscsi sg3_utils

### Optional requirement
#Requires:  cfg2html

%ifarch x86_64 i686
Requires: syslinux
%endif
%ifarch x86_64 i686 aarch64
# We need mkfs.vfat for recreating EFI System Partition
Recommends: dosfstools
%endif
%ifarch ppc ppc64
Requires:   yaboot
%endif

%ifarch ppc ppc64 ppc64le
# Called by grub2-install (except on PowerNV)
Requires:   /usr/sbin/ofpathname
# Needed to make PowerVM LPARs bootable
Requires:   /usr/sbin/bootlist
%endif
%ifarch s390x
# Contain many utilities for working with DASDs
Requires:   s390utils-base
Requires:   s390utils-core
%endif

Requires:   crontabs
Requires:   iproute
# No ISO image support on s390x (may change when we add support for LPARs)
%ifnarch s390x
Requires:   xorriso
%endif

# mingetty is not available anymore with RHEL 7 (use agetty instead via systemd)
# Note that CentOS also has rhel defined so there is no need to use centos
%if 0%{?rhel} && 0%{?rhel} > 6
Requires:   util-linux
%else
Requires:   mingetty
Requires:   util-linux
%endif

### The rear-snapshot package is no more
#Obsoletes: rear-snapshot

%description
Relax-and-Recover is the leading Open Source disaster recovery and system
migration solution. It comprises of a modular
frame-work and ready-to-go workflows for many common situations to produce
a bootable image and restore from backup using this image. As a benefit,
it allows to restore to different hardware and can therefore be used as
a migration tool as well.

Currently Relax-and-Recover supports various boot media (incl. ISO, PXE,
OBDR tape, USB or eSATA storage), a variety of network protocols (incl.
sftp, ftp, http, nfs, cifs) as well as a multitude of backup strategies
(incl.  IBM TSM, HP DataProtector, Symantec NetBackup, EMC NetWorker,
Bacula, Bareos, BORG, Duplicity, rsync).

Relax-and-Recover was designed to be easy to set up, requires no maintenance
and is there to assist when disaster strikes. Its setup-and-forget nature
removes any excuse for not having a disaster recovery solution implemented.

Professional services and support are available.

%pre
if [ $1 -gt 1 ] ; then
# during upgrade remove obsolete directories
%{__rm} -rf %{_datadir}/rear/output/NETFS
fi

%prep
%setup 
%patch4 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch56 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1

echo "30 1 * * * root test -f /var/lib/rear/layout/disklayout.conf && /usr/sbin/rear checklayout || /usr/sbin/rear mkrescue" >rear.cron

### Add a specific os.conf so we do not depend on LSB dependencies
%{?fedora:echo -e "OS_VENDOR=Fedora\nOS_VERSION=%{?fedora}" >etc/rear/os.conf}
%{?rhel:echo -e "OS_VENDOR=RedHatEnterpriseServer\nOS_VERSION=%{?rhel}" >etc/rear/os.conf}

%build
# asciidoc writes a timestamp to files it produces, based on the last
# modified date of the source file, but is sensible to the timezone.
# This makes the results differ according to the timezone of the build machine
# and spurious changes will be seen.
# Set the timezone to UTC as a workaround.
# https://wiki.debian.org/ReproducibleBuilds/TimestampsInDocumentationGeneratedByAsciidoc
TZ=UTC %{__make} -C doc

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0644 rear.cron %{buildroot}%{_sysconfdir}/cron.d/rear

%files
%defattr(-, root, root, 0755)
%doc MAINTAINERS COPYING README.adoc doc/*.txt doc/user-guide/relax-and-recover-user-guide.html
%doc %{_mandir}/man8/rear.8*
%config(noreplace) %{_sysconfdir}/cron.d/rear
%config(noreplace) %{_sysconfdir}/rear/
%config(noreplace) %{_sysconfdir}/rear/cert/
%{_datadir}/rear/
%{_localstatedir}/lib/rear/
%{_sbindir}/rear

%changelog
* Tue Aug 22 2023 Pavel Cahyna <pcahyna@redhat.com> - 2.6-10
- Apply PR 3027 to ensure correct creation of the rescue environment
  when a file is shrinking while being read
- Backport PR 2774 to increase USB_UEFI_PART_SIZE to 1024 MiB
- Apply upstream patch for temp dir usage with LUKS to ensure
  that during recovery an encrypted disk can be unlocked using a keyfile
- Backport upstream PR 3031: Secure Boot support for OUTPUT=USB
- Correct a mistake done when backporting PR 2691

* Wed Feb 22 2023 Pavel Cahyna <pcahyna@redhat.com> - 2.6-9
- Backport PR2943 to fix s390x dasd formatting
- Require s390utils-{core,base} on s390x

* Sun Jan 15 2023 Pavel Cahyna <pcahyna@redhat.com> - 2.6-8
- Apply PR2903 to protect against colons in pvdisplay output
- Apply PR2873 to fix initrd regeneration on s390x
- Apply PR2431 to migrate XFS configuration files

* Wed Aug 24 2022 Pavel Cahyna <pcahyna@redhat.com> - 2.6-7
- Avoid stderr message about irrelevant broken links
- Changes for NetBackup (NBU) 9.x support

* Tue Aug  9 2022 Pavel Cahyna <pcahyna@redhat.com> - 2.6-6
- Restore usr/share/rear/output/PXE/default/820_copy_to_net.sh
  removed in 2.4-19 with rsync refactor.
  It is still needed to use a rsync OUTPUT_URL when OUTPUT=PXE and BACKUP=RSYNC

* Mon Aug  8 2022 Pavel Cahyna <pcahyna@redhat.com> - 2.6-5
- Apply PR2795 to detect changes in system files between backup
  and rescue image
- Apply PR2808 to exclude dev/watchdog* from recovery system
- Backport upstream PRs 2827 and 2839 to pass -y to lvcreate instead of one "y"
  on stdin
- Apply PR2811 to add the PRE/POST_RECOVERY_COMMANDS directives
- Recommend dosfstools on x86 and aarch64, needed for EFI System Partition

* Sun Feb 27 2022 Pavel Cahyna <pcahyna@redhat.com> - 2.6-4
- Apply PR2675 to fix leftover temp dir bug (introduced in backported PR2625)
- Apply PR2603 to ignore unused PV devices
- Apply upstream PR2750 to avoid exclusion of wanted multipath devices
- Remove unneeded xorriso dep on s390x (no ISO image support there)
- Apply upstream PR2736 to add the EXCLUDE_{IP_ADDRESSES,NETWORK_INTERFACES}
  options

* Mon Aug 30 2021 Pavel Cahyna <pcahyna@redhat.com> - 2.6-3
- Add patch for better handling of thin pools and other LV types not supported
  by vgcfgrestore
  Resolves: rhbz1747468

* Mon Aug 16 2021 Pavel Cahyna <pcahyna@redhat.com> - 2.6-2
- Fix multipath performance regression in 2.6, introduced by upstream PR #2299.
  Resolves: rhbz1993296

* Sat Aug  7 2021 Pavel Cahyna <pcahyna@redhat.com> - 2.6-1
- Rebase to upstream release 2.6 and drop unneded patches.
  Add S/390 support.
  Resolves: rhbz1983003, rhbz1988493, rhbz1868421
- Add missing dependencies on dhcp-client (see #1926451), file
- Patch documents to be compatible with asciidoc,
  we don't have asciidoctor
- On POWER add bootlist & ofpathname to the list of required programs
  conditionally (bootlist only if running under PowerVM, ofpathname
  always except on PowerNV) - upstream PR2665, add them to package
  dependencies
  Resolves: rhbz1983013

* Tue May 11 2021 Pavel Cahyna <pcahyna@redhat.com> - 2.4-19
- Backport PR2608:
  Fix setting boot path in case of UEFI partition (ESP) on MD RAID
  Resolves: rhbz1945869
- Backport PR2625
  Prevents accidental backup removal in case of errors
  Resolves: rhbz1958247
- Fix rsync error and option handling
  Fixes metadata storage when rsync user is not root
  Resolves: rhbz1930662

* Mon Jan 11 2021 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.4-18
- Fix typo in default.conf
  Resolves: #1882060
- Modify the cron command to avoid an e-mail with error message after
  ReaR is installed but not properly configured when the cron command
  is triggered for the first time
  Resolves: #1729499
- Backport upstream code related to LUKS2 support
  Resolves: #1832394
- Changes for NetBackup (NBU) support, upstream PR2544
  Resolves: #1898080

* Mon Aug 10 2020 Pavel Cahyna <pcahyna@redhat.com> - 2.4-17
- Update the Rubrik patch to include complete PR2445
  Resolves: rhbz1867696

* Thu Jun 04 2020 Václav Doležal <vdolezal@redhat.com> - 2.4-16
- Apply upstream PR2373: Skip Longhorn Engine replica devices
  Resolves: rhbz1843809

* Mon Jun 01 2020 Václav Doležal <vdolezal@redhat.com> - 2.4-15
- Apply upstream PR2346: Have '-iso-level 3' option also for ppc64le
  Resolves: rhbz1729502

* Mon Jun 01 2020 Václav Doležal <vdolezal@redhat.com> - 2.4-14
- Backport remaining Rubrik related patches.
  Related: rhbz1743303

* Thu May 21 2020 Václav Doležal <vdolezal@redhat.com> - 2.4-13
- Backport upstream PR #2249 to add support for Rubrik backup method.
  Resolves: rhbz1743303

* Mon Dec 16 2019 Pavel Cahyna <pcahyna@redhat.com> - 2.4-12
- Backport upstream PR #2293 to use grub-mkstandalone instead of
  grub-mkimage for UEFI (ISO image and GRUB_RESCUE image generation).
  Avoids hardcoded module lists or paths and so is more robust.
  Fixes an issue where the generated ISO image had no GRUB2 modules and
  was therefore unbootable. The backport does not add new config settings.
  Resolves: rhbz1737042

* Mon Nov 18 2019 Pavel Cahyna <pcahyna@redhat.com> - 2.4-11
- Apply upstream PR2122: add additional NBU library path to fix support for
  NetBackup 8.
  Resolves: rhbz1747393
- Apply upstream PR2021: Be safe against empty docker_root_dir (issue 1989)
  Resolves: rhbz1729493, where ReaR can not create a backup in rescue mode,
  because it thinks that the Docker daemon is running and hits the problem
  with empty docker_root_dir.
- Apply upstream PR2223 and commit 36cf20e to avoid an empty string in the
  list of users to clone, which can lead to bash overflow with lots of users
  and groups per user and to wrong passwd/group files in the rescue system.
  Resolves: rhbz1729495
- Backport of Upstream fix for issue 2035: /run is not mounted in the rescue
  chroot, which causes LVM to hang, especially if rebuilding initramfs.
  Resolves: rhbz1757488
- Backport upstream PR 2218: avoid keeping build dir on errors
  by default when used noninteractively
  Resolves: rhbz1729501
- Apply upstream PR2173 - Cannot restore using Bacula method
  due to "bconsole" not showing its prompt
  Resolves: rhbz1726992
- Backport fix for upstream issue 2187 (disklayout.conf file contains
  duplicate lines, breaking recovery in migration mode or when
  thin pools are used). PR2194, 2196.
  Resolves: rhbz1732308

* Tue Jun  4 2019 Pavel Cahyna <pcahyna@redhat.com> - 2.4-10
- Apply upstream patch PR1993
  Automatically exclude $BUILD_DIR from the backup
  Resolves: rhbz1677733

* Mon Jun  3 2019 Pavel Cahyna <pcahyna@redhat.com> - 2.4-9
- Update fix for bz#1657725. Previous fix was not correct, bootlist was still
  invoked only with one partition argument due to incorrect array expansion.
  See upstream PR2096, 2097, 2098.

* Tue May 28 2019 Pavel Cahyna <pcahyna@redhat.com> - 2.4-8
- Apply upstream PR2065 (record permanent MAC address for team members)
  Resolves: rhbz1685178

* Tue May 28 2019 Pavel Cahyna <pcahyna@redhat.com> - 2.4-7
- Apply upstream PR2034 (multipath optimizations for lots of devices)

* Mon Jan 14 2019 Pavel Cahyna <pcahyna@redhat.com> - 2.4-6
- Require xorriso instead of genisoimage, it is now the preferred method
  and supports files over 4GB in size.
- Apply upstream PR2004 (support for custom network interface naming)
- Backport upstream PR2001 (UEFI support broken on Fedora 29 and RHEL 8)

* Thu Dec 13 2018 Pavel Cahyna <pcahyna@redhat.com> - 2.4-4
- Backport fixes for upstream bugs 1974 and 1975
- Backport fix for upstream bug 1913 (backup succeeds in case of tar error)
- Backport fix for upstream bug 1926 (support for LACP bonding and teaming)
- Apply upstream PR1954 (record permanent MAC address for bond members)

* Thu Aug 09 2018 Pavel Cahyna <pcahyna@redhat.com> - 2.4-3
- Merge some spec changes from Fedora.
- Apply upstream patch PR1887
  LPAR/PPC64 bootlist is incorrectly set when having multiple 'prep' partitions
- Apply upstream patch PR1885
  Partition information recorded is unexpected when disk has 4K block size

* Wed Jul 18 2018 Pavel Cahyna <pcahyna@redhat.com> - 2.4-2
- Build and install the HTML user guide. #1418459

* Wed Jun 27 2018 Pavel Cahyna <pcahyna@redhat.com> - 2.4-1
- Rebase to version 2.4, drop patches integrated upstream
  Resolves #1534646 #1484051 #1498828 #1571266 #1496518

* Wed Feb 14 2018 Pavel Cahyna <pcahyna@redhat.com> - 2.00-6
- Ensure that NetBackup is started automatically upon recovery (PR#1544)
  Also do not kill daemons spawned by sysinit.service at the service's end
  (PR#1610, applies to NetBackup and also to dhclient)
  Resolves #1506231
- Print a warning if grub2-mkimage is about to fail and suggest what to do.
  bz#1492177
- Update the patch for #1388653 to the one actually merged upstream (PR1418)

* Fri Jan 12 2018 Pavel Cahyna <pcahyna@redhat.com> - 2.00-5
- cd to the correct directory before md5sum to fix BACKUP_INTEGRITY_CHECK.
  Upstream PR#1685, bz1532676

* Mon Oct 23 2017 Pavel Cahyna <pcahyna@redhat.com> - 2.00-4
- Retry get_disk_size to fix upstream #1370, bz1388653

* Wed Sep 13 2017 Pavel Cahyna <pcahyna@redhat.com> - 2.00-3
- Fix rear mkrescue on systems w/o UEFI. Upstream PR#1481 issue#1478
- Resolves: #1479002

* Wed May 17 2017 Jakub Mazanek <jmazanek@redhat.com> - 2.00-2
- Excluding Archs s390 and s390x
- Related #1355667

* Mon Feb 20 2017 Jakub Mazanek <jmazanek@redhat.com> - 2.00-1
- Rebase to version 2.00 
- Resolves #1355667

* Tue Jul 19 2016 Petr Hracek <phracek@redhat.com> - 1.17.2-6
- Replace experimental grep -P with grep -E
Resolves: #1290205

* Wed Mar 23 2016 Petr Hracek <phracek@redhat.com> - 1.17.2-5
- Remove backuped patched files
Related: #1283930

* Wed Mar 23 2016 Petr Hracek <phracek@redhat.com> - 1.17.2-4
- Rear recovery over teaming interface will not work
Resolves: #1283930

* Tue Mar 08 2016 Petr Hracek <phracek@redhat.com> - 1.17.2-3
- Replace experimental grep -P with grep -E
Resolves: #1290205

* Tue Feb 23 2016 Petr Hracek <phracek@redhat.com> - 1.17.2-2
- rear does not require syslinux
- changing to arch package so that syslinux is installed
- Resolves: #1283927

* Mon Sep 14 2015 Petr Hracek <phracek@redhat.com> - 1.17.2-1
- New upstream release 1.17.2
Related: #1059196

* Wed May 13 2015 Petr Hracek <phracek@redhat.com> 1.17.0-2
- Fix Source tag
Related: #1059196

* Mon May 04 2015 Petr Hracek <phracek@redhat.com> 1.17.0-1
- Initial package for RHEL 7
Resolves: #1059196

* Fri Oct 17 2014 Gratien D'haese <gratien.dhaese@gmail.com>
- added the suse_version lines to identify the corresponding OS_VERSION

* Fri Jun 20 2014 Gratien D'haese <gratien.dhaese@gmail.com>
- add %%pre section

* Thu Apr 11 2013 Gratien D'haese <gratien.dhaese@gmail.com>
- changes Source

* Thu Jun 03 2010 Dag Wieers <dag@wieers.com>
- Initial package. (using DAR)
