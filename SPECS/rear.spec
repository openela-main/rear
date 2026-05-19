# this is purely a shell script, so no debug packages
%global debug_package %{nil}

Name: rear
Version: 2.6
Release: 28%{?dist}
Summary: Relax-and-Recover is a Linux disaster recovery and system migration tool
URL: http://relax-and-recover.org/
License: GPLv3

Source0: https://github.com/rear/rear/archive/%{version}.tar.gz#/rear-%{version}.tar.gz
# Add cronjob and systemd timer as documentation
Source1: rear.cron
Source2: rear.service
Source3: rear.timer
# Skip buildin modules, RHBZ#1831311
Patch0: 0001-skip-kernel-buildin-modules.patch
Patch4:  rear-bz1492177-warning.patch
Patch29: rear-bz1832394.patch
Patch30: rear-sfdc02772301.patch
Patch31: rear-bz1945869.patch
Patch32: rear-bz1958247.patch
Patch33: rear-bz1930662.patch
Patch34: rear-tmpdir.patch
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
Patch45: rear-bz2097437.patch
Patch46: rear-bz2096916.patch
Patch47: rear-bz2096900.patch
Patch48: rear-bz2111059.patch
Patch49: rsync-output.patch
Patch50: rear-bz2119501.patch
Patch51: rear-bz2120736.patch
Patch52: rear-bz2117937.patch
Patch53: rear-bz2091163.patch
Patch54: rear-bz2130945.patch
Patch55: rear-bz2131946.patch
Patch56: s390-no-clobber-disks.patch
Patch57: rear-bz2188593-nbu-systemd.patch
Patch58: rear-device-shrinking-bz2223895.patch
Patch59: rear-usb-uefi-part-size-bz2228402.patch
Patch60: rear-luks-key-bz2228779.patch
Patch61: rear-uefi-usb-secureboot-bz2196445.patch
Patch62: rear-vg-command-not-found-bz2121476.patch
Patch63: rear-remove-lvmdevices-bz2145014.patch
Patch64: rear-save-lvm-poolmetadatasize-RHEL-6984.patch
Patch65: rear-skip-useless-xfs-mount-options-RHEL-10478.patch

# make initrd accessible only by root
# https://github.com/rear/rear/commit/89b61793d80bc2cb2abe47a7d0549466fb087d16
Patch111: rear-CVE-2024-23301.patch

# Support saving and restoring hybrid BIOS/UEFI bootloader setup and clean up bootloader detection
# https://github.com/rear/rear/pull/3145
Patch113: rear-restore-hybrid-bootloader-RHEL-16864.patch

# Resolve libs for executable links in COPY_AS_IS
# https://github.com/rear/rear/commit/9f859c13f5ba285cd1d5983c9b595975c21888d3
Patch114: rear-resolve-libraries-for-symlinks-in-COPY_AS_IS-RHEL-15108.patch

# Skip invalid disk drives (zero sized, no media) when saving layout
# https://github.com/rear/rear/commit/808b15a677191aac62faadd1bc71885484091316
Patch115: rear-skip-invalid-drives-RHEL-22863.patch

# Fix useless warning that libsystemd-core requires additional libraries
# and ReaR recovery system needs additional libraries
# https://github.com/rear/rear/pull/3250
Patch116: rear-fix-libsystemd-ldd-warning.patch

# Fix IPv6 addresses in nfs:// and sshfs:// BACKUP/OUTPUT_URL
# https://github.com/rear/rear/pull/3242
Patch117: rear-fix-ipv6.patch

# Remove obsolete FAT16 options to avoid kernel warning
# https://github.com/rear/rear/pull/2576
Patch118: rear-no-fat-16.patch

# Install GRUB on multipath disks
# https://github.com/rear/rear/pull/3334
Patch119: rear-multipath-bios-grub.patch

# Improve docs of layout configuration in user guide
# https://github.com/rear/rear/pull/3125
Patch121: rear-improve-layout-guide.patch

# skip longhorn iscsi devices in disklayout.conf
# https://github.com/rear/rear/commit/d765abff976a8346ce6afa432c9a09d67ed63482
Patch122: rear-skip-longhorn-iscsi-RHEL-83551.patch

# fix PPC PReP Boot detection on GPT layouts
# https://github.com/rear/rear/commit/1ca518c2a0e675ace956ef71bc79d67e4990562b
Patch123: rear-detect-prep-boot-on-gpt-RHEL-82098.patch

# fix recovery of LUKS encrypted systems with multiple keyslots
# https://github.com/rear/rear/commit/e9ce93f096e505968cc728a7eb5a06e25dc8d88b
Patch124: rear-support-multi-keyslot-luks-RHEL-83776.patch

# support generation of ed25519 SSH host keys in the rescue image
# https://github.com/rear/rear/commit/62d9a744ff710de34035ce15bd1b1bf810b6934a
Patch125: rear-rescue-ed25519-hostkey-support-RHEL-83479.patch

# enhance the 300_map_disks.sh script to also print the disk sizes
# https://github.com/rear/rear/commit/43d62fdfcac50b35be4f99d45bac3b5340525a7a
Patch126: rear-print-disk-mapping-with-sizes-RHEL-83241.patch

# add initial support for arm/aarch64 machines with UEFI
# https://github.com/rear/rear/commit/9b28f14fad26ff00a6f90b13c3e4906d85f3ae3c
Patch127: rear-support-aarch64-uefi-RHEL-56045.patch

# copy an sshd helper to the rescue ramdisk, necessary on EL9.8
# https://github.com/rear/rear/commit/bcf6669fac64d194d18b2e5360df4181002856e8
Patch128: rear-sshd-RHEL-146037.patch

# fix support for PowerNV machines without PPC PReP partitions
# https://github.com/rear/rear/commit/79a3b50a0effcf4c1a43e9dfe1b8d0427ee0bf02
Patch129: rear-fix-powerNV-support-RHEL-134217.patch

# EL10-only
# Patch130:
# Patch131:

# add support for dbus broker
# https://github.com/rear/rear/commit/61d294b9635b3c71bd58409e810bccb705b1220c
Patch132: rear-dbus-broker-RHEL-31749.patch

# abort when sourcing fails due to a syntax error
# https://github.com/rear/rear/commit/c4a7729242455cdef69f5ac3982f8d76ccc183c3
Patch133: rear-abort-source-on-syntax-error-RHEL-104289.patch

# fix recreation of multi-disk volume groups in migration mode
# https://github.com/rear/rear/commit/acb19846599a5fc411fd8c288776e1af2d79c920
Patch134: rear-fix-VG-recreation-RHEL-23887.patch

# skip unsupported partition tables, e.g. sun
# https://github.com/rear/rear/commit/825478ee27f916553938afaf5164fec22cb32732
Patch135: rear-skip-unsupported-partition-tables-RHEL-78583.patch

# do not attempt to use the disk with backup for recovery
# https://github.com/rear/rear/commit/258e34a72374d512155054e2d6efa84f8f5cd974
# https://github.com/rear/rear/commit/7e5aea79e0fe1badf7c0820e854f8ca3ac32cef0
# https://github.com/rear/rear/commit/a5edba7551884e9201a21fc1ea33de7ca7e6cb07
Patch136: rear-do-not-use-backup-disk-for-recovery-RHEL-111612.patch

######################
# downstream patches #
######################

# additional fixes for NBU support
Patch206: rear-nbu-RHEL-17390-RHEL-17393.patch

# support "export TMPDIR" again, temporarily, with a warning.
Patch207: rear-support-export-TMPDIR.patch

# error out if any unsupported OUTPUT used on s390
Patch208: rear-error-output-s390x-RHEL-99362.patch

# rear contains only bash scripts plus documentation so that on first glance it could be "BuildArch: noarch"
# but actually it is not "noarch" because it only works on those architectures that are explicitly supported.
# Of course the rear bash scripts can be installed on any architecture just as any binaries can be installed on any architecture.
# But the meaning of architecture dependent packages should be on what architectures they will work.
# Therefore only those architectures that are actually supported are explicitly listed.
# This avoids that rear can be "just installed" on architectures that are actually not supported:
ExclusiveArch: %ix86 x86_64 ppc ppc64 ppc64le ia64 s390x %arm aarch64
# Furthermore for some architectures it requires architecture dependent packages (like syslinux for x86 and x86_64)
# so that rear must be architecture dependent because ifarch conditions never match in case of "BuildArch: noarch"
# see the GitHub issue https://github.com/rear/rear/issues/629
%ifarch %ix86 x86_64
Requires: syslinux-extlinux
%endif
# See https://github.com/rhboot/efi-rpm-macros/blob/main/README
%ifarch %{efi}
# We need mkfs.vfat for recreating EFI System Partition
Recommends: dosfstools
# Needed for ISO image creation
Recommends: grub2-efi-%{efi_arch}-modules
Recommends: grub2-tools-extra
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
# In the end this should tell the user that rear is known to work only on ix86 x86_64 ppc ppc64 ppc64le ia64
# and on ix86 x86_64 syslinux is explicitly required to make the bootable ISO image
# (in addition to the default installed bootloader grub2) while on ppc ppc64 the
# default installed bootloader yaboot is also useed to make the bootable ISO image.

BuildRequires: efi-srpm-macros
BuildRequires: git-core
# Required for HTML user guide
BuildRequires: make
BuildRequires: asciidoctor

### Mandatory dependencies:
Requires: binutils
Requires: ethtool
Requires: gzip
Requires: iputils
Requires: parted
Requires: tar
Requires: openssl
Requires: gawk
Requires: attr
Requires: bc
Requires: iproute
# No ISO image support on s390x (may change when we add support for LPARs)
%ifnarch s390x
Requires:   xorriso
%endif
Requires: file
Requires: dhcp-client
%if 0%{?rhel}
Requires: util-linux
%endif

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
(incl.  IBM TSM, MircroFocus Data Protector, Symantec NetBackup, EMC NetWorker,
Bacula, Bareos, BORG, Duplicity, rsync).

Relax-and-Recover was designed to be easy to set up, requires no maintenance
and is there to assist when disaster strikes. Its setup-and-forget nature
removes any excuse for not having a disaster recovery solution implemented.

Professional services and support are available.

#-- PREP, BUILD & INSTALL -----------------------------------------------------#
%prep
%autosetup -p1 -S git

### Add a specific os.conf so we do not depend on LSB dependencies
%{?fedora:echo -e "OS_VENDOR=Fedora\nOS_VERSION=%{?fedora}" >etc/rear/os.conf}
%{?rhel:echo -e "OS_VENDOR=RedHatEnterpriseServer\nOS_VERSION=%{?rhel}" >etc/rear/os.conf}

# Change /lib to /usr/lib for COPY_AS_IS
sed -E -e "s:([\"' ])/lib:\1/usr/lib:g" \
    -i usr/share/rear/prep/GNU/Linux/*include*.sh

# Same for Linux.conf
sed -e 's:/lib/:/usr/lib/:g' \
    -e 's:/lib\*/:/usr/lib\*/:g' \
    -e 's:/usr/usr/lib:/usr/lib:g' \
    -i 'usr/share/rear/conf/GNU/Linux.conf'

%build
# build HTML user guide
# asciidoc writes a timestamp to files it produces, based on the last
# modified date of the source file, but is sensitive to the timezone.
# This makes the results differ according to the timezone of the build machine
# and spurious changes will be seen.
# Set the timezone to UTC as a workaround.
# https://wiki.debian.org/ReproducibleBuilds/TimestampsInDocumentationGeneratedByAsciidoc
TZ=UTC make doc

%install
%{make_install}
install -p -d %{buildroot}%{_docdir}/%{name}/
install -m 0644 %{SOURCE1} %{buildroot}%{_docdir}/%{name}/
install -m 0644 %{SOURCE2} %{buildroot}%{_docdir}/%{name}/
install -m 0644 %{SOURCE3} %{buildroot}%{_docdir}/%{name}/

#-- FILES ---------------------------------------------------------------------#
%files
%doc MAINTAINERS COPYING README.adoc doc/*.txt doc/user-guide/*.html
%doc %{_mandir}/man8/rear.8*
%doc %{_docdir}/%{name}/rear.*
%config(noreplace) %{_sysconfdir}/rear/
%{_datadir}/rear/
%{_sharedstatedir}/rear/
%{_sbindir}/rear

#-- CHANGELOG -----------------------------------------------------------------#
%changelog
* Thu Jan 29 2026 Lukáš Zaoral <lzaoral@redhat.com> - 2.6-28
- use git to apply downstream patches
- copy an sshd helper to the rescue ramdisk (RHEL-146037)
- fix support for PowerNV machines without PPC PReP partitions (RHEL-134217)
- add support for dbus broker (RHEL-31749)
- abort when sourcing fails due to a syntax error (RHEL-104289)
- fix recreation of multi-disk volume groups in migration mode (RHEL-23887)
- skip unsupported partition tables (RHEL-78583)
- do not attempt to use the disk with backup for recovery (RHEL-111612)

* Thu Aug 14 2025 Pavel Cahyna <pcahyna@redhat.com> - 2.6-27
- add dependency on grub2-tools-extra and GRUB EFI modules on EFI machines
- add dependency on syslinux-extlinux on x86
- add initial support for aarch64 machines with UEFI
- enhance the 300_map_disks.sh script to also print the disk sizes
- support generation of ed25519 SSH host keys in the rescue image
- create sshd home directory in the rescue image on systems upgraded from EL8
- fix recovery of LUKS encrypted systems with multiple keyslots
- fix PPC PReP Boot detection on GPT layouts
- skip longhorn iscsi devices in disklayout.conf
- error out if any unsupported OUTPUT used on s390x

* Tue Feb 11 2025 Pavel Cahyna <pcahyna@redhat.com> - 2.6-26
- Install GRUB on multipath disks, PR 3334
- Improve docs of layout configuration in user guide, PR 3125

* Sat Jul 20 2024 Pavel Cahyna <pcahyna@redhat.com> - 2.6-25
- Backport PR 3250 to fix useless warning that libsystemd-core requires
  additional libraries and ReaR recovery system needs additional libraries
- Backport PR 3242 to fix IPv6 address in nfs:// and sshfs:// BACKUP/OUTPUT_URL
- Backport PR 2576 to remove obsolete FAT16 options to avoid kernel warning

* Sat Feb 24 2024 Pavel Cahyna <pcahyna@redhat.com> - 2.6-24
- Support "export TMPDIR" in user configuration again, print a warning
  when this is used - revert commit f464eae2, adapt PR 3163, add commit
  b422845f.
  Will be supported only until the update to 2.7

* Fri Feb  9 2024 Pavel Cahyna <pcahyna@redhat.com> - 2.6-23
- Resolve libs for executable links in COPY_AS_IS, PR 3073
- Skip invalid disk drives when saving layout PR 3047

* Thu Feb  8 2024 Pavel Cahyna <pcahyna@redhat.com> - 2.6-22
- Do not delete NetBackup logs in case of errors and save
  /usr/openv/netbackup/logs to the restored system after a successful recovery
- Add /usr/openv/var to COPY_AS_IS_NBU, fixes an issue seen
  with NetBackup 10.2.0.1

* Thu Feb  8 2024 Pavel Cahyna <pcahyna@redhat.com> - 2.6-21
- Support saving and restoring hybrid BIOS/UEFI bootloader, PRs 3145 3136
- make initrd accessible only by root (CVE-2024-23301), PR 3123

* Fri Dec  1 2023 Pavel Cahyna <pcahyna@redhat.com> - 2.6-20
- Backport PR 3061 to save LVM pool metadata volume size in disk layout
  and restore it
- Backport PR 3058 to skip useless xfs mount options when mounting
  during recovery, prevents mount errors like "logbuf size must be greater
  than or equal to log stripe size"

* Fri Aug 25 2023 Pavel Cahyna <pcahyna@redhat.com> - 2.6-19
- Add patch to force removal of lvmdevices, prevents LVM problems after
  restoring to different disks/cloning. Upstream PR 3043

* Tue Aug 22 2023 Pavel Cahyna <pcahyna@redhat.com> - 2.6-18
- Add patch to start rsyslog and include NBU systemd units
- Apply PR 3027 to ensure correct creation of the rescue environment
  when a file is shrinking while being read
- Backport PR 2774 to increase USB_UEFI_PART_SIZE to 1024 MiB
- Apply upstream patch for temp dir usage with LUKS to ensure
  that during recovery an encrypted disk can be unlocked using a keyfile
- Backport upstream PR 3031: Secure Boot support for OUTPUT=USB
- Correct a mistake done when backporting PR 2691

* Wed Feb 22 2023 Pavel Cahyna <pcahyna@redhat.com> - 2.6-17
- Backport PR2943 to fix s390x dasd formatting
- Require s390utils-{core,base} on s390x

* Sun Jan 15 2023 Pavel Cahyna <pcahyna@redhat.com> - 2.6-16
- Apply PR2903 to protect against colons in pvdisplay output
- Apply PR2873 to fix initrd regeneration on s390x
- Apply PR2431 to migrate XFS configuration files

* Thu Aug 25 2022 Pavel Cahyna <pcahyna@redhat.com> - 2.6-15
- Exclude /etc/lvm/devices from the rescue system to work around a segfault
  in lvm pvcreate

* Wed Aug 24 2022 Pavel Cahyna <pcahyna@redhat.com> - 2.6-14
- Avoid stderr message about irrelevant broken links
- Changes for NetBackup (NBU) 9.x support

* Tue Aug  9 2022 Pavel Cahyna <pcahyna@redhat.com> - 2.6-13
- Backport PR2831 - rsync URL refactoring
  fixes rsync OUTPUT_URL when different from BACKUP_URL

* Mon Aug  8 2022 Pavel Cahyna <pcahyna@redhat.com> - 2.6-12
- Apply PR2795 to detect changes in system files between backup
  and rescue image
- Apply PR2808 to exclude dev/watchdog* from recovery system
- Backport upstream PRs 2827 and 2839 to pass -y to lvcreate instead of one "y"
  on stdin
- Apply PR2811 to add the PRE/POST_RECOVERY_COMMANDS directives
- Recommend dosfstools on x86_64, needed for EFI System Partition
- Backport PR2825 to replace defunct mkinitrd with dracut
- Apply PR2580 to load the nvram module in the rescue environment in order
  to be able to set the boot order on ppc64le LPARs
- Backport PR2822 to include the true vi executable in rescue ramdisk

* Sun Feb 27 2022 Pavel Cahyna <pcahyna@redhat.com> - 2.6-11
- Apply PR2675 to fix leftover temp dir bug (introduced in backported PR2625)
- Apply PR2603 to ignore unused PV devices
- Apply upstream PR2750 to avoid exclusion of wanted multipath devices
- Remove unneeded xorriso dep on s390x (no ISO image support there)
- Apply upstream PR2736 to add the EXCLUDE_{IP_ADDRESSES,NETWORK_INTERFACES}
  options
- Add patch for better handling of thin pools and other LV types not supported
  by vgcfgrestore

* Mon Aug 16 2021 Pavel Cahyna <pcahyna@redhat.com> - 2.6-10
- Sync spec changes and downstream patches from RHEL 8 rear-2.6-2
  - Fix multipath performance regression in 2.6, introduced by upstream PR #2299.
    Resolves: rhbz1993296
  - On POWER add bootlist & ofpathname to the list of required programs
    conditionally (bootlist only if running under PowerVM, ofpathname
    always except on PowerNV) - upstream PR2665, add them to package
    dependencies
    Resolves: rhbz1983013
  - Backport PR2608:
    Fix setting boot path in case of UEFI partition (ESP) on MD RAID
    Resolves: rhbz1945869
  - Backport PR2625
    Prevents accidental backup removal in case of errors
    Resolves: rhbz1958247
  - Fix rsync error and option handling
    Resolves: rhbz1930662

* Wed Aug 11 2021 Pavel Cahyna <pcahyna@redhat.com> - 2.6-9
- Put TMPDIR on /var/tmp by default, otherwise it may lack space
  RHBZ #1988420, upstream PR2664

* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 2.6-8
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Wed Jun 30 2021 Pavel Cahyna <pcahyna@redhat.com> - 2.6-7
- Sync spec changes and downstream patches from RHEL 8
  - Require xorriso instead of genisoimage
  - Add S/390 support and forgotten dependency on the file utility
  - Backport upstream code related to LUKS2 support
  - Modify the cron command to avoid an e-mail with error message after
    ReaR is installed but not properly configured when the cron command
    is triggered for the first time
  - Changes for NetBackup (NBU) support, upstream PR2544
- Add dependency on dhcp-client, RHBZ #1926451

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 2.6-6
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Fri Feb 26 2021 Christopher Engelhard <ce@lcts.de> - 2.6-5
- Change /lib to /usr/lib in scripts to fix RHBZ #1931112

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 23 2020 Christopher Engelhard <ce@lcts.de> - 2.6-3
- Stop auto-creating a cronjob, but ship example cronjob/
  systemd timer units in docdir instead (upstream issue #1829)
- Build & ship HTML user guide
- Remove %pre scriptlet, as it was introduced only to fix a
  specific upgrade issue with v1.15 in 2014

* Tue Sep 22 2020 Christopher Engelhard <ce@lcts.de> - 2.6-2
- Backport upstream PR#2469 to fix RHBZ #1831311

* Tue Sep 22 2020 Christopher Engelhard <ce@lcts.de> - 2.6-1
- Update to 2.6
- Streamline & clean up spec file

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 30 2015 Johannes Meixner <jsmeix@suse.de>
- For a changelog see the rear-release-notes.txt file.

