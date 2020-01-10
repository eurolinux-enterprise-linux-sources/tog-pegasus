#
#
#               OpenPegasus (Red Hat release) RPM .spec file
#
#  tog-pegasus.spec
#
#   Copyright (c) 2000 - 2006, 
#     The Open Group; Hewlett-Packard Development Company, L.P.;
#     IBM Corp.;  BMC Software; Tivoli Systems.
#     Licensed under the "Open Group Pegasus Open Source" license 
#     shipped with this software.
#
#  Upstream tog-pegasus.spec file modified for Red Hat build -
#  April 2006, Jason Vas Dias <jvdias@redhat.com>, Red Hat Inc.
#

%{?!LINUX_VERSION: 		%define LINUX_VERSION  %{?dist}}
#
%{?!PEGASUS_BUILD_TEST_RPM:   	%define PEGASUS_BUILD_TEST_RPM        0}
# do "rpmbuild --define 'PEGASUS_BUILD_TEST_RPM 1'" to build test RPM.
#
%{?!NOCLEAN:     		%define NOCLEAN 0}
# ^- 1: don't do %clean
%{?!NODEBUGINFO: 		%define NODEBUGINFO 0}
# ^- 1: don't generate debuginfo or strip binaries
%{?!PEGASUS_32BIT_PROVIDER_SUPPORT: %define PEGASUS_32BIT_PROVIDER_SUPPORT 0}
# ^- 1: build 32 bit providers for 64 bit CIMOM
%{?!EXTERNAL_SLP_REQUESTED: %define EXTERNAL_SLP_REQUESTED 1}
# ^- 1: include External SLP support
%if %{NODEBUGINFO}
%define debug_package   %{nil}
%endif
%define srcname    	pegasus
%define major_ver	2.12
%define pegasus_gid	65
%define pegasus_uid	66
%define cimsrvr_gid	134
%define cimsrvr_uid	134

Version: 		%{major_ver}.0
Release: 		6%{?dist}
Epoch:   		2
#
Summary:   		OpenPegasus WBEM Services for Linux
Name:      		tog-pegasus
Group:     		System Environment/Daemons
URL:       		http://www.openpegasus.org
#
License:   		MIT
#
BuildRoot: 		%{_tmppath}/%{name}-%{version}-%{release}-%{_target_cpu}-%(%{__id} -u -n)
#
Source:			http://www.openpegasus.org/uploads/40/18361/pegasus-%{version}.tar.gz
#  1: Description of security enhacements
Source1:        	README.RedHat.Security
#  2: Script for setting SSL certificates - used in init script when cimserver is started for the first time
Source2:		genOpenPegasusSSLCerts
#  3: Description of SSL settings
Source3:		README.RedHat.SSL
#
#  0: Still not fixed by http://cvs.rdg.opengroup.org/bugzilla/show_bug.cgi?id=5008
#     Changes to the init script to make it LSB compliant
Patch0:			pegasus-2.9.0-initscript.patch
#  1: http://cvs.rdg.opengroup.org/bugzilla/show_bug.cgi?id=5011
#     Removing insecure -rpath
Patch1:			pegasus-2.9.0-no-rpath.patch
#  2: Adding -fPIE
Patch2:			pegasus-2.7.0-PIE.patch
#  3: http://cvs.rdg.opengroup.org/bugzilla/show_bug.cgi?id=5016
#     Configuration variables
Patch3:			pegasus-2.9.0-redhat-config.patch
#  4: don't see how http://cvs.rdg.opengroup.org/bugzilla/show_bug.cgi?id=5099 fixed it
#     Changing provider dir to the directory we use
Patch4:			pegasus-2.9.0-cmpi-provider-lib.patch
#  5: http://cvs.rdg.opengroup.org/bugzilla/show_bug.cgi?id=5010
#     We distinguish between local and remote user and behave adequately (will be upstream once)
Patch5:			pegasus-2.9.0-local-or-remote-auth.patch
#  6: http://cvs.rdg.opengroup.org/bugzilla/show_bug.cgi?id=5012
#     Modifies pam rules to use access cofiguration file and local/remote differences
Patch6:			pegasus-2.5.1-pam-wbem.patch
#  7: http://cvs.rdg.opengroup.org/bugzilla/show_bug.cgi?id=5006
#     Modifies Makefile for the tests
Patch7:			pegasus-2.9.0-fix_tests.patch
#  9: Adds cimuser binary to admin commands
Patch9:			pegasus-2.6.0-cimuser.patch
# 12: Removes snmp tests, which we don't want to perform
Patch12:		pegasus-2.7.0-no_snmp_tests.patch
# 13: Changes to make package compile on sparc
Patch13:                pegasus-2.9.0-sparc.patch
# 16: Fixes "getpagesize" build error
Patch16:		pegasus-2.9.1-getpagesize.patch
# 17: Don't strip debug information
Patch17:		pegasus-2.10.0-dont-strip.patch
# 18: Change build options
Patch18:		pegasus-2.11.0-new-build-options.patch
# 19: Backported sslBackwardCompatibility option
Patch19:                pegasus-2.12.0-ssl-backwarkd-compatibility.patch
# 20: Service has to be enabled by administrator, not by default, bz#1277655
Patch20:                pegasus-2.12.0-service-off-by-default.patch
#
Conflicts: 		openwbem
Provides: 		tog-pegasus-cimserver
Provides:		cim-server
#
BuildRequires:      	bash, sed, grep, coreutils, procps, gcc, gcc-c++
BuildRequires:      	imake, libstdc++, make, pam-devel
BuildRequires:      	openssl-devel >= 0.9.8b, e2fsprogs
BuildRequires:		net-snmp-devel
%if %{PEGASUS_32BIT_PROVIDER_SUPPORT}
%if %{__isa_bits} == 64
BuildRequires: glibc-devel(%{__isa_name}-32)
BuildRequires: pam-devel(%{__isa_name}-32)
BuildRequires: openssl-devel(%{__isa_name}-32)
%endif
%endif
%if %{EXTERNAL_SLP_REQUESTED}
BuildRequires:		openslp-devel
Requires:		openslp
%endif
#
Requires:           	bash, sed, grep, coreutils, procps, openssl >= 0.9.8b, pam
Requires:          	chkconfig, sysvinit
Requires:           	e2fsprogs, bind-utils, net-tools
Requires(post):     	bash, sed, grep, coreutils, procps, openssl >= 0.9.8b, pam
Requires(post):    	chkconfig, sysvinit
Requires(post):     	e2fsprogs, bind-utils, net-tools
Requires(pre):      	bash, sed, grep, coreutils, procps, openssl >= 0.9.8b, pam
Requires(pre):     	chkconfig, sysvinit
Requires(pre):      	e2fsprogs, bind-utils, net-tools
Requires(postun):   	bash, sed, grep, coreutils, procps, openssl >= 0.9.8b, pam
Requires(postun):  	chkconfig, sysvinit
Requires(postun):   	e2fsprogs, bind-utils, net-tools
Requires:		net-snmp
Requires:		tog-pegasus-libs = %{epoch}:%{version}-%{release}

%description
OpenPegasus WBEM Services for Linux enables management solutions that deliver
increased control of enterprise resources. WBEM is a platform and resource
independent DMTF standard that defines a common information model and
communication protocol for monitoring and controlling resources from diverse
sources.

%package devel
Summary: 		The OpenPegasus Software Development Kit
Group: 			Systems Management/Base
Requires:               tog-pegasus >= %{version}-%{release}
Obsoletes: 		tog-pegasus-sdk
Requires:		make, gcc, gcc-c++
Requires(preun): 	make

%description devel
The OpenPegasus WBEM Services for Linux SDK is the developer's kit for the
OpenPegasus WBEM Services for Linux release. It provides Linux C++ developers
with the WBEM files required to build WBEM Clients and Providers. It also
supports C provider developers via the CMPI interface.

%package libs
Summary:		The OpenPegasus Libraries
Group:			Systems Management/Base
Requires(pre):		/usr/sbin/useradd
Requires(pre):		/usr/sbin/groupadd

%description libs
The OpenPegasus libraries.

%if %{PEGASUS_BUILD_TEST_RPM}
%package test
Summary: 		The OpenPegasus Tests
Group: 			Systems Management/Base
Requires:               tog-pegasus >= %{version}-%{release}, make

%description test
The OpenPegasus WBEM tests for the OpenPegasus %{version} Linux rpm.
%endif

%if %{PEGASUS_32BIT_PROVIDER_SUPPORT}

%ifarch x86_64
%global PEGASUS_HARDWARE_PLATFORM_FOR_32BIT LINUX_IX86_GNU
%global PEGASUS_EXTRA_CXX_FLAGS_32BIT  "-O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=4 -march=i386 -mtune=generic -fasynchronous-unwind-tables -Wno-unused -m32"
%global PEGASUS_EXTRA_LINK_FLAGS_32BIT "-O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=4 -march=i386 -mtune=generic -fasynchronous-unwind-tables -m32"
%else
%ifarch ppc64 pseries
%global PEGASUS_HARDWARE_PLATFORM_FOR_32BIT LINUX_PPC_GNU
%global PEGASUS_EXTRA_CXX_FLAGS_32BIT  "-O2 -g -fmessage-length=0 -D_FORTIFY_SOURCE=2 -m32 -Wno-unused"
%global PEGASUS_EXTRA_LINK_FLAGS_32BIT "-O2 -g -m64 -fmessage-length=0 -D_FORTIFY_SOURCE=2 -m32"
%else
%ifarch s390x zseries
%global PEGASUS_HARDWARE_PLATFORM_FOR_32BIT LINUX_ZSERIES_GNU
%global PEGASUS_EXTRA_CXX_FLAGS_32BIT  "-O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=4 -m31 -Wno-unused"
%global PEGASUS_EXTRA_LINK_FLAGS_32BIT "-O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=4 -m31"
%endif
%endif
%endif

%endif

%prep
%setup -q -n %{srcname}
# upstream tarball has wrong structure - pegasus/pegasus/
cp -pR pegasus/* .
rm -rf pegasus/
%patch1 -p1 -b .no-rpath
%patch2 -p1 -b .PIE
%patch3 -p1 -b .redhat-config
%patch4 -p1 -b .cmpi-provider-lib
%patch6 -p1 -b .pam-wbem
%patch7 -p1 -b .fix-tests
%patch9 -p1 -b .cimuser
%patch12 -p1 -b .no_snmp_tests
%patch5 -p1 -b .local-or-remote-auth
%patch13 -p1 -b .sparc
%patch0 -p1 -b .initscript
%patch16 -p1 -b .getpagesize
%patch17 -p1 -b .dont-strip
%patch18 -p1 -b .new-build-options
%patch19 -p1 -b .ssl-backwarkd-compatibility
%patch20 -p1 -b .service-off-by-default
find . -name 'CVS' -exec /bin/rm -rf '{}' ';' >/dev/null 2>&1 ||:;

%build
rm -rf ${RPM_BUILD_ROOT} || :;
cp -fp %SOURCE1 doc
cp -fp %SOURCE2 rpm
cp -fp %SOURCE3 doc

export RPM_ARCH_LIB=%{_lib}
export RPM_ARCH=%{_target_cpu}
export RPM_BUILD_DIR=`pwd`
export RPM_ARCH=`uname -i`
export RPM_OPT_FLAGS=`rpm -q rpm --qf '%{OPTFLAGS}'`
%ifarch ia64
  export PEGASUS_PLATFORM=LINUX_IA64_GNU
%else
  %ifarch x86_64
    export PEGASUS_PLATFORM=LINUX_X86_64_GNU
  %else
    %ifarch ppc
      export PEGASUS_PLATFORM=LINUX_PPC_GNU
    %else
      %ifarch ppc64
        export PEGASUS_PLATFORM=LINUX_PPC64_GNU
      %else
        %ifarch s390
          export PEGASUS_PLATFORM=LINUX_ZSERIES_GNU
        %else
          %ifarch s390x
            export PEGASUS_PLATFORM=LINUX_ZSERIES64_GNU
          %else
            %ifarch sparcv9
              export PEGASUS_PLATFORM=LINUX_SPARCV9_GNU
            %else
              %ifarch sparc64
                export PEGASUS_PLATFORM=LINUX_SPARC64_GNU
              %else
                export PEGASUS_PLATFORM=LINUX_IX86_GNU
              %endif
            %endif
          %endif
        %endif
      %endif
    %endif
  %endif
%endif
export PEGASUS_ROOT=${RPM_BUILD_DIR}
export PEGASUS_HOME=${PEGASUS_ROOT}/build
export PEGASUS_ARCH_LIB=${RPM_ARCH_LIB}
export PEGASUS_ENVVAR_FILE=${PEGASUS_ROOT}/env_var_Linux.status
export PEGASUS_EXTRA_C_FLAGS="${RPM_OPT_FLAGS} -g -fPIC -Wall -Wno-unused -fno-strict-aliasing"
export PEGASUS_EXTRA_CXX_FLAGS=${PEGASUS_EXTRA_C_FLAGS}
export PEGASUS_EXTRA_PROGRAM_LINK_FLAGS="-pie -Wl,-z,relro,-z,now,-z,nodlopen,-z,noexecstack"
export OPENSSL_HOME=/usr
export OPENSSL_BIN=/usr/bin
export SYS_INCLUDES=-I/usr/kerberos/include
export LD_LIBRARY_PATH=${PEGASUS_HOME}/lib
export PATH=${PEGASUS_HOME}/bin:${PATH}

%if %{PEGASUS_32BIT_PROVIDER_SUPPORT}
sed -i 's/#PEGASUS_PLATFORM_FOR_32BIT_PROVIDER_SUPPORT=.*$/PEGASUS_PLATFORM_FOR_32BIT_PROVIDER_SUPPORT=%PEGASUS_HARDWARE_PLATFORM_FOR_32BIT/' $PEGASUS_ENVVAR_FILE
%endif

make %{?_smp_mflags} -f ${PEGASUS_ROOT}/Makefile.Release create_ProductVersionFile
make %{?_smp_mflags} -f ${PEGASUS_ROOT}/Makefile.Release create_CommonProductDirectoriesInclude
make %{?_smp_mflags} -f ${PEGASUS_ROOT}/Makefile.Release create_ConfigProductDirectoriesInclude
make %{?_smp_mflags} -f ${PEGASUS_ROOT}/Makefile.Release depend
make %{?_smp_mflags} -f ${PEGASUS_ROOT}/Makefile.Release all
make %{?_smp_mflags} -f ${PEGASUS_ROOT}/Makefile.Release repository
%if %{PEGASUS_BUILD_TEST_RPM}
    make %{?_smp_mflags} -f ${PEGASUS_ROOT}/Makefile.ReleaseTest -s create_repository
%endif

%if %{PEGASUS_32BIT_PROVIDER_SUPPORT}
export PEGASUS_PLATFORM_FOR_32BIT_PROVIDER_SUPPORT=%PEGASUS_HARDWARE_PLATFORM_FOR_32BIT
export PEGASUS_EXTRA_C_FLAGS=%PEGASUS_EXTRA_CXX_FLAGS_32BIT
export PEGASUS_EXTRA_CXX_FLAGS="$PEGASUS_EXTRA_C_FLAGS"
export PEGASUS_EXTRA_LINK_FLAGS=%PEGASUS_EXTRA_LINK_FLAGS_32BIT
make %{?_smp_mflags} -f $PEGASUS_ROOT/Makefile.cimprovagt32 all
%endif

%install
export RPM_ARCH_LIB=%{_lib}
export RPM_ARCH=%{_target_cpu}
export BSX=%{bsx}
export RPM_BUILD_DIR=`pwd`
export RPM_ARCH=`uname -i`
export RPM_OPT_FLAGS=`rpm -q rpm --qf '%{OPTFLAGS}'`
%ifarch ia64
  export PEGASUS_PLATFORM=LINUX_IA64_GNU
%else
  %ifarch x86_64
    export PEGASUS_PLATFORM=LINUX_X86_64_GNU
  %else
    %ifarch ppc
      export PEGASUS_PLATFORM=LINUX_PPC_GNU
    %else
      %ifarch ppc64
        export PEGASUS_PLATFORM=LINUX_PPC64_GNU
      %else
        %ifarch s390
          export PEGASUS_PLATFORM=LINUX_ZSERIES_GNU
        %else
          %ifarch s390x
            export PEGASUS_PLATFORM=LINUX_ZSERIES64_GNU
          %else
            %ifarch sparcv9
              export PEGASUS_PLATFORM=LINUX_SPARCV9_GNU
            %else
              %ifarch sparc64
                export PEGASUS_PLATFORM=LINUX_SPARC64_GNU
              %else
                export PEGASUS_PLATFORM=LINUX_IX86_GNU
              %endif
            %endif
          %endif
        %endif
      %endif
    %endif
  %endif
%endif
export PEGASUS_ROOT=${RPM_BUILD_DIR}
export PEGASUS_HOME=${PEGASUS_ROOT}/build
export PEGASUS_ARCH_LIB=${RPM_ARCH_LIB}
export PEGASUS_ENVVAR_FILE=${PEGASUS_ROOT}/env_var_Linux.status
export PEGASUS_EXTRA_C_FLAGS="${RPM_OPT_FLAGS} -Wno-unused"
export PEGASUS_EXTRA_CXX_FLAGS=${PEGASUS_EXTRA_C_FLAGS}
export PEGASUS_EXTRA_PROGRAM_LINK_FLAGS="-pie -Wl,-z,relro,-z,now,-z,nodlopen,-z,noexecstack"
export OPENSSL_HOME=/usr
export OPENSSL_BIN=/usr/bin
export SYS_INCLUDES=-I/usr/kerberos/include
export LD_LIBRARY_PATH=${PEGASUS_HOME}/lib
export PATH=${PEGASUS_HOME}/bin:${PATH}

export PEGASUS_STAGING_DIR=$RPM_BUILD_ROOT
%if %{PEGASUS_BUILD_TEST_RPM}
make -f $PEGASUS_ROOT/Makefile.Release stage \
    PEGASUS_STAGING_DIR=$PEGASUS_STAGING_DIR \
    PEGASUS_BUILD_TEST_RPM=%{PEGASUS_BUILD_TEST_RPM}
%else
make -f $PEGASUS_ROOT/Makefile.Release stage \
    PEGASUS_STAGING_DIR=$PEGASUS_STAGING_DIR
%endif

%if %{PEGASUS_32BIT_PROVIDER_SUPPORT}
export PEGASUS_PLATFORM_FOR_32BIT_PROVIDER_SUPPORT=%PEGASUS_HARDWARE_PLATFORM_FOR_32BIT
export LD_LIBRARY_PATH=$PEGASUS_HOME/lib32
make -f $PEGASUS_ROOT/Makefile.cimprovagt32 stage \
    PEGASUS_STAGING_DIR=$PEGASUS_STAGING_DIR
%endif

# move files to right directories
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d/
#mv $RPM_BUILD_ROOT/etc/init.d/tog-pegasus $RPM_BUILD_ROOT/etc/rc.d/init.d/tog-pegasus
rm -f $RPM_BUILD_ROOT/etc/init.d/tog-pegasus
cp rpm/tog-pegasus.rc $RPM_BUILD_ROOT/etc/rc.d/init.d/tog-pegasus
mkdir -p $RPM_BUILD_ROOT/%{_docdir}/%{name}-%{version}
mv $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{major_ver}/* $RPM_BUILD_ROOT/%{_docdir}/%{name}-%{version}
rm -rf $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{major_ver}
# create symlink for libcmpiCppImpl
pushd $RPM_BUILD_ROOT/usr/%{_lib}
ln -s libcmpiCppImpl.so.1 libcmpiCppImpl.so
popd

%if %{NODEBUGINFO}
    /usr/lib/rpm/brp-compress;
    exit 0;
%endif

:;


%files
%defattr(600,cimsrvr,cimsrvr,700)
%verify(not md5 size mtime mode group) /var/lib/Pegasus/repository
%defattr(644,root,pegasus,755)
/usr/share/Pegasus/mof
%defattr(600,root,pegasus,755)
%dir /usr/share/doc/%{name}-%{version}
%dir /usr/share/Pegasus
%dir /usr/share/Pegasus/scripts
%dir /var/lib/Pegasus
%dir /var/lib/Pegasus/cache
%dir /var/lib/Pegasus/log
%dir /var/lib/Pegasus/cache/localauth
%dir %attr(755,root,pegasus) /etc/Pegasus
%dir %attr(755,cimsrvr,cimsrvr) /var/run/tog-pegasus
#%dir %attr(1755,cimsrvr,cimsrvr) /var/run/tog-pegasus/socket
%dir %attr(1777,root,pegasus) /var/lib/Pegasus/cache/trace
%config(noreplace) %attr(755,root,pegasus) /etc/rc.d/init.d/tog-pegasus
%config(noreplace) %attr(644,root,root) /etc/Pegasus/cimserver_planned.conf
%config(noreplace) /etc/Pegasus/access.conf
%config(noreplace) /etc/pam.d/wbem
%ghost %config(noreplace) /etc/Pegasus/ssl.cnf
%ghost %config(noreplace) /etc/Pegasus/client.pem
%ghost %config(noreplace) /etc/Pegasus/server.pem
%ghost %config(noreplace) /etc/Pegasus/file.pem
%ghost %verify(not md5 size mtime) /var/lib/Pegasus/log/install.log
%attr(755,root,pegasus) /usr/sbin/*
%attr(755,root,pegasus) /usr/bin/*
%attr(750,root,pegasus) /usr/share/Pegasus/scripts/*
%attr(644,root,pegasus) /usr/share/man/man1/*
%attr(644,root,pegasus) /usr/share/man/man8/*
%doc doc/license.txt doc/Admin_Guide_Release.pdf doc/PegasusSSLGuidelines.htm doc/SecurityGuidelinesForDevelopers.html doc/README.RedHat.Security src/Clients/repupgrade/doc/repupgrade.html doc/README.RedHat.SSL

%files devel
%defattr(0644,root,pegasus,0755)
/usr/include/Pegasus
/usr/share/Pegasus/samples
/usr/share/Pegasus/html

%if %{PEGASUS_BUILD_TEST_RPM}
%files test -f ghost_arch_test
%defattr(0644,root,pegasus,0755)
%dir /usr/share/Pegasus/test
/usr/share/Pegasus/test/Makefile%{bsx}
/usr/share/Pegasus/test/mak
%verify(not md5 size mtime) /var/lib/Pegasus/testrepository
%defattr(0750,root,pegasus,0755)
/usr/share/Pegasus/test/bin
/usr/share/Pegasus/test/lib
%endif

%files libs
%defattr(600,root,pegasus,755)
%dir %{_libdir}/Pegasus
%dir %{_libdir}/Pegasus/providers
%dir %{_libdir}/Pegasus/providerManagers
%attr(755,root,pegasus) %{_libdir}/*.so.1
%attr(755,root,pegasus) %{_libdir}/Pegasus/providerManagers/*.so.1
%if %{PEGASUS_32BIT_PROVIDER_SUPPORT}
%dir /usr/lib/Pegasus
%dir /usr/lib/Pegasus/providers
%dir /usr/lib/Pegasus/providerManagers
%attr(755,root,pegasus) /usr/lib/*.so.1
%attr(755,root,pegasus) /usr/lib/Pegasus/providerManagers/*.so.1
/usr/lib/libpegclient.so
/usr/lib/libpegcommon.so
/usr/lib/libpegprovider.so
/usr/lib/libDefaultProviderManager.so
/usr/lib/Pegasus/providerManagers/libCMPIProviderManager.so
%endif
%{_libdir}/*.so
%{_libdir}/Pegasus/providers/*.so*
%{_libdir}/Pegasus/providerManagers/libCMPIProviderManager.so
%if %{EXTERNAL_SLP_REQUESTED}
#%{_libdir}/libpegslp_client.so
%{_libdir}/Pegasus/providers/libSLPProvider.so
%endif
%if !%{NODEBUGINFO}
%exclude /usr/lib/debug
%endif

%clean
%if !%{NOCLEAN}
[ "${RPM_BUILD_ROOT}" != "/" ] && rm -rf $RPM_BUILD_ROOT;
[ "${RPM_BUILD_DIR}" != "/" ] && rm -rf ${RPM_BUILD_DIR}/%{srcname};
%endif

%pre
if [ $1 -gt 1 ]; then
   if [ -d /var/lib/Pegasus/repository ]; then
	if [ -d /var/lib/Pegasus/prev_repository ]; then
	   mv /var/lib/Pegasus/prev_repository /var/lib/Pegasus/prev_repository_`date '+%Y-%m-%d-%s.%N'`.rpmsave;
	fi;
	mv /var/lib/Pegasus/repository /var/lib/Pegasus/prev_repository;
   fi
fi
:;

%post
ldconfig;
chkconfig --add tog-pegasus;
if [ $1 -ge 1 ]; then	
   echo `date` >>  /var/lib/Pegasus/log/install.log 2>&1 || :;
   if [ $1 -gt 1 ]; then
      if [ -d /var/lib/Pegasus/prev_repository ]; then
      #  The user's old repository was moved to /var/lib/Pegasus/prev_repository, which 
      #  now must be upgraded to the new repository in /var/lib/Pegasus/repository:
	 /usr/sbin/repupgrade 2>> /var/lib/Pegasus/log/install.log || :;
         mv /var/lib/Pegasus/prev_repository /var/lib/Pegasus/prev_repository_`date '+%Y-%m-%d-%s.%N'`.rpmsave;
         chown -R cimsrvr /var/lib/Pegasus/repository
         chgrp -R cimsrvr /var/lib/Pegasus/repository
      fi;
      /sbin/service tog-pegasus condrestart >/dev/null 2>&1 || :;
   fi;
fi
:;

%preun
if [ $1 -eq 0 ]; then
   /sbin/service tog-pegasus stop >/dev/null 2>&1 || :;
   /sbin/chkconfig --del tog-pegasus >/dev/null 2>&1 || :;
fi
:;

%postun -p /sbin/ldconfig

%preun devel
if [ $1 -eq 0 ] ; then
   make --directory /usr/share/Pegasus/samples -s clean >/dev/null 2>&1 || :;
fi
:;

%pre libs
if [ $1 -eq 1 ]; then
#  first install: create the 'pegasus' user and group:
   /usr/sbin/groupadd -g %{pegasus_gid} -f -r pegasus >/dev/null 2>&1 || :;
   /usr/sbin/useradd -u %{pegasus_uid} -r -N -M -g pegasus -s /sbin/nologin -d /var/lib/Pegasus \
     -c "tog-pegasus OpenPegasus WBEM/CIM services" pegasus >/dev/null 2>&1 || :;
fi
# Privilege Separation is enabled - create the 'cimsrvr' user and
# 'cimsrvr' group which are used as the context of the cimservermain process
if [ $1 -gt 0 ]; then
   /usr/sbin/groupadd -g %{cimsrvr_gid} -f -r cimsrvr >/dev/null 2>&1 || :;
   /usr/sbin/useradd -u %{cimsrvr_uid} -r -N -M -g cimsrvr -s /sbin/nologin -d /var/lib/Pegasus \
     -c "tog-pegasus OpenPegasus WBEM/CIM services" cimsrvr >/dev/null 2>&1 || :;
fi
:;

%post libs
if [ $1 -eq 1 ]; then
   # Create Symbolic Links for SDK Libraries
   #
   ln -sf libpegclient.so.1 /usr/%{_lib}/libpegclient.so
   ln -sf libpegcommon.so.1 /usr/%{_lib}/libpegcommon.so
   ln -sf libpegprovider.so.1 /usr/%{_lib}/libpegprovider.so
   ln -sf libDefaultProviderManager.so.1 /usr/%{_lib}/libDefaultProviderManager.so
   ln -sf libCIMxmlIndicationHandler.so.1 /usr/%{_lib}/libCIMxmlIndicationHandler.so
   ln -sf libsnmpIndicationHandler.so.1 /usr/%{_lib}/libsnmpIndicationHandler.so

   # Create Symbolic Links for Packaged Provider Libraries
   #
   ln -sf libComputerSystemProvider.so.1 /usr/%{_lib}/Pegasus/providers/libComputerSystemProvider.so
   ln -sf libOSProvider.so.1 /usr/%{_lib}/Pegasus/providers/libOSProvider.so
   ln -sf libProcessProvider.so.1 /usr/%{_lib}/Pegasus/providers/libProcessProvider.so

   # Create Symbolic Links for Packaged Provider Managers
   #
   ln -sf libCMPIProviderManager.so.1 /usr/%{_lib}/Pegasus/providerManagers/libCMPIProviderManager.so

   # Create Symbolic Links for SLP library and SLP Provider
   #
%if %{EXTERNAL_SLP_REQUESTED}
  ln -sf libpegslp_client.so.1 /usr/%{_lib}/libpegslp_client.so
  ln -sf libSLPProvider.so.1 /usr/%{_lib}/Pegasus/providers/libSLPProvider.so
%endif

   # Change ownership of Symbolic Links to the 'pegasus' group
   #
   /bin/chgrp -h pegasus /usr/%{_lib}/libpegclient.so
   /bin/chgrp -h pegasus /usr/%{_lib}/libpegcommon.so 
   /bin/chgrp -h pegasus /usr/%{_lib}/libpegprovider.so
   /bin/chgrp -h pegasus /usr/%{_lib}/libDefaultProviderManager.so
   /bin/chgrp -h pegasus /usr/%{_lib}/libCIMxmlIndicationHandler.so
   /bin/chgrp -h pegasus /usr/%{_lib}/libsnmpIndicationHandler.so
   /bin/chgrp -h pegasus /usr/%{_lib}/Pegasus/providers/libComputerSystemProvider.so
   /bin/chgrp -h pegasus /usr/%{_lib}/Pegasus/providers/libOSProvider.so
   /bin/chgrp -h pegasus /usr/%{_lib}/Pegasus/providers/libProcessProvider.so
   /bin/chgrp -h pegasus /usr/%{_lib}/Pegasus/providerManagers/libCMPIProviderManager.so
%if %{EXTERNAL_SLP_REQUESTED}
   /bin/chgrp -h pegasus /usr/%{_lib}/libpegslp_client.so
   /bin/chgrp -h pegasus /usr/%{_lib}/Pegasus/providers/libSLPProvider.so
%endif
fi
:;

%changelog
* Tue Oct 11 2016 Vitezslav Crhonek <vcrhonek@redhat.com> - 2:2.12.0-6
- Turn the service off by default
  Resolves: #1277655

* Mon Apr 11 2016 Vitezslav Crhonek <vcrhonek@redhat.com> - 2:2.12.0-5
- Add missing useradd/groupadd dependency to tog-pegasus-libs
  Resolves: #1313794

* Thu Nov 05 2015 Vitezslav Crhonek <vcrhonek@redhat.com> - 2:2.12.0-4
- Backported and slightly modified sslBackwardCompatibility option for disabling
  unsafe SSLv3 protocol
  Resolves: #1238329

* Mon Jun 10 2013 Vitezslav Crhonek <vcrhonek@redhat.com> - 2:2.12.0-3
- Disable privilege separation
  Resolves: #957233

* Mon Oct 29 2012 Vitezslav Crhonek <vcrhonek@redhat.com> - 2:2.12.0-2
- Fix local-or-remote-auth patch to work with IPv6 and with enabled
  privilege separation
  Resolves: #869664

* Tue Oct 09 2012 Vitezslav Crhonek <vcrhonek@redhat.com> - 2:2.12.0-1
- Update to upstream version 2.12.0
  Resolves: #825471, #739118, #716474
- Change post created symlinks group owner to 'pegasus'
  Resolves: #759064
- Fix invocation of useradd without specifying a UID
  Resolves: #800319
- Fix initscript is not world readable
  Resolves: #824297

* Tue Mar 06 2012 Vitezslav Crhonek <vcrhonek@redhat.com> - 2:2.11.0-3
- Backport upstream patch which enables the embedded instanaces to have
  correct empty string values
  Resolves: #796191
- Add "cim-server" to provides
  Resolves: #799040

* Tue Jul 26 2011 Vitezslav Crhonek <vcrhonek@redhat.com> - 2:2.11.0-2
- Add -libs requirement with explicit version to the main package
- Build with -fno-strict-aliasing
- Use correct init script
- Add OpenSLP support
  Resolves: #712525

* Mon Jul 25 2011 Vitezslav Crhonek <vcrhonek@redhat.com> - 2:2.11.0-1
- Update to upstream version 2.11.0
  Resolves: #633577
- Improve package to comply multilib policy
  Resolves: #607722
- Don't strip debug information
  Resolves: #693389
- Change build options
  Resolves: #694513

* Thu Jul 15 2010 Vitezslav Crhonek <vcrhonek@redhat.com> - 2:2.9.1-5
- Add cimsub to the pegasus_arch_alternatives script

* Thu Jun 17 2010 Vitezslav Crhonek <vcrhonek@redhat.com> - 2:2.9.1-4
- Mark files in /var/lib/Pegasus as noverify in spec file

* Tue May 25 2010 Vitezslav Crhonek <vcrhonek@redhat.com> - 2:2.9.1-3
- Fix memory leak

* Thu Apr 22 2010 Vitezslav Crhonek <vcrhonek@redhat.com> - 2:2.9.1-2
- Fix initscript permissions

* Thu Jan 14 2010 Vitezslav Crhonek <vcrhonek@redhat.com> - 2:2.9.1-1
- Update to upstream version 2.9.1
- Add patch/source descriptions to the spec file

* Wed Nov 25 2009 Dennis Gregorovic <dgregor@redhat.com> - 2:2.9.0-8.1
- Rebuilt for RHEL 6

* Mon Nov  2 2009 Vitezlsav Crhonek <vcrhonek@redhat.com> - 2:2.9.0-8
- Fix wrong multilib flag for ix86 arch

* Wed Sep 23 2009 Vitezslav Crhonek <vcrhonek@redhat.com> - 2:2.9.0-7
- Fix initscript
  Resolves: #523370

* Wed Sep 16 2009 Tomas Mraz <tmraz@redhat.com> - 2:2.9.0-6
- Use password-auth common PAM configuration instead of system-auth

* Wed Aug 25 2009 Tomas Mraz <tmraz@redhat.com> - 2:2.9.0-5
- rebuilt with new openssl

* Wed Aug 19 2009 Vitezslav Crhonek <vcrhonek@redhat.com> - 2:2.9.0-4
- Fix Source (but I'm afraid it's not very persistent and it will
  not work again after some time)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:2.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 21 2009 Vitezslav Crhonek <vcrhonek@redhat.com> - 2:2.9.0-2
- Fix Group

* Mon Jun 16 2009 Vitezslav Crhonek <vcrhonek@redhat.com> - 2:2.9.0-1
- Update to upstream version 2.9.0
- Remove redhat-lsb requires
- Add README.RedHat.SSL

* Thu Apr 16 2009 Vitezslav Crhonek <vcrhonek@redhat.com> - 2:2.7.2-8
- Replace useradd '-n' option by '-N' ('-n' is obsolete)
  Resolves: #495729

* Tue Mar  3 2009 Vitezslav Crhonek <vcrhonek@redhat.com> - 2:2.7.2-7
- Add noreplace to config files

* Sat Feb 28 2009 Caolán McNamara <caolanm@redhat.com> - 2:2.7.2-6
- fix elif

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:2.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 02 2009 Dennis Gilmore < dennis@ausil.us> - 2:2.7.2-4
- apply sparc fixes

* Sun Jan 18 2009 Tomas Mraz <tmraz@redhat.com> - 2:2.7.2-3
- rebuild with new openssl

* Tue Nov 11 2008 Vitezslav Crhonek <vcrhonek@redhat.com> - 2:2.7.2-2
- Fix local or remote auth patch to work correctly with new code base
  Related: #459217

* Thu Nov  6 2008 Vitezslav Crhonek <vcrhonek@redhat.com> - 2:2.7.2-1
- Update to upstream version 2.7.2
  (remove patches added in 2.7.1-1 - they're upstream now)
- Enable out-of-process providers
  Resolves: #455109

* Mon Sep  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2:2.7.1-2
- fix license tag

* Tue Jul 15 2008 Vitezslav Crhonek <vcrhonek@redhat.com> - 2:2.7.1-1
- Update to upstream version 2.7.1
- Fix setElementAt() doesn't copy value of CMPI_char parameter
  Resolves: #454589
- Fix CMPI MI factories that return errors are unsupported
  Resolves: #454590
- Fix HTTP 401 responses lack Content-Length headers
  Resolves: #454591

* Tue Jul  1 2008 Vitezslav Crhonek <vcrhonek@redhat.com> - 2:2.7.0-9
- Add SNMP indication handler to package
  Resolves: #452930

* Tue Jun  3 2008 Vitezslav Crhonek <vcrhonek@redhat.com> - 2:2.7.0-8
- Add cimsub to package
  Resolves: #447823

* Thu May 15 2008 Vitezslav Crhonek <vcrhonek@redhat.com> - 2:2.7.0-7
- Rebuild

* Mon Feb 11 2008 Vitezslav Crhonek <vcrhonek@redhat.com> - 2:2.7.0-6
- Rebuild

* Mon Jan 21 2008 Vitezslav Crhonek <vcrhonek@redhat.com> - 2:2.7.0-5
- No snmp tests in Test RPM

* Thu Jan 10 2008 Vitezslav Crhonek <vcrhonek@redhat.com> - 2:2.7.0-4
- Fix Test RPM

* Wed Dec  5 2007 Vitezslav Crhonek <vcrhonek@redhat.com> - 2:2.7.0-3
- Rebuild

* Fri Nov 23 2007 Vitezslav Crhonek <vcrhonek@redhat.com> - 2:2.7.0-2
- Fix OpenPegasus SRPM fails to build Test RPM 
  Resolves: #391961

* Mon Nov 19 2007 Vitezslav Crhonek <vcrhonek@redhat.com> - 2:2.7.0-1
- Update to upstream version 2.7.0
- Unhide some cmpi classes, package cmpi C++ headers
- Fix multiarch conflicts
  Resolves: #343311
- Add libcmpiCppImpl.so (symlink to libcmpiCppImpl.so.1)
  Resolves: #366871

* Tue Oct  9 2007 Vitezslav Crhonek <vcrhonek@redhat.com> - 2:2.6.1-2
- Fix files permissions
  Resolves: #200906

* Thu Aug 30 2007 Vitezslav Crhonek <vcrhonek@redhat.com> - 2:2.6.1-1
- Update to 2.6.1
- Fix wrong init script (#245339)

* Wed Mar 28 2007 Vitezslav Crhonek <vcrhonek@redhat.com> - 2:2.6.0-2
- Update changelog
- Build with Open Pegasus' Makefiles, istall with Red Hats (Mark Hamzy)

* Mon Feb 26 2007 Mark Hamzy <hamzy@us.ibm.com> - 2:2.6.0-1
- Upgrade to upstream version 2.6.0

* Mon Dec  4 2006 Nalin Dahyabhai <nalin@redhat.com> - 2:2.5.2-3
- change requires: tog-pegasus to prereq: tog-pegasus so that the pegasus
  user and group will exist when we go to lay down files for tog-pegasus-devel
  (#218305)
- prereq the current version of openssl so that the right versions of
  libssl and libcrypto will be available in %%post (possible for #208949)

* Fri Aug 18 2006 Jesse Keating <jkeating@redhat.com> - 2:2.5.2-2
- rebuilt with latest binutils to pick up 64K -z commonpagesize on ppc*
  (#203001)

* Thu Jul 27 2006 Jason Vas Dias <jvdias@redhat.com> - 2:2.5.2-1.fc6
- Upgrade to upstream version 2.5.2
- fix bug 198185
- fix bug 200246

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2:2.5.1-10.FC6.1
- rebuild

* Fri Jul 07 2006 Jason Vas Dias <jvdias@redhat.com> - 2:2.4.1-10
- More upstream 2.5.2_APPROVED bug fixes:
  o 4629: Pegasus freezes when it is unable to send out completely, the results of a request
  o 5073: Class Names on Reference, ReferenceNames, Assoc, AssocNames returned lower case
  o 5090: cimserver crash on a request after attempting to unload idle CMPI providers
  o 5180: OperationAggregate deleted in _enqueueResponse while member mutex held

* Fri Jun 09 2006 Jason Vas Dias <jvdias@redhat.com> - 2:2.5.1-8
- Fix bug 192754: remove multilib conflicts
- More upstream 2.5.2_APPROVED bug fixes:
  o 5119: memory leak in CMPI implementation
  o 5115: fix SetConfig_EnvVar comments

* Wed May 31 2006 Jason Vas Dias <jvdias@redhat.com> - 2:2.5.1-6
- Apply upstream patches for latest 2.5.2_APPROVED bugs:
  o 5046: cimprovider timeout needs to be increased
  o 5047: cimmof timeout needs to be increased
  o 5048: Invalid Pointer in CIMOperationRequestEncoder code
  o 5049: Unnecessary dependency on experimental headers
  o 5051: Improved handling of OOP indication provide module failures
  o 5053: reserveCapacity method may cause size overflow
  o 5059: XMLWriter does not escape '>' in strings
  o 5072: Potential race condition with OOP response chunks
  o 5083: CIMRequestMessage buildResponse() should be const
- Fix bug 193121: restore world read access to libraries   

* Tue May 02 2006 Jason Vas Dias <jvdias@redhat.com> - 2:2.5.1-4
- fix bug 190432: %%exclude /usr/lib/debug from RPM
- fix upstream OpenPegasus '2.5.2_APPROVED' bugs, applying upstream patches:
  o 4955 : Bogus Description property for OperatingSystem provider
  o 4956 : reserveCapacity method may cause size overflow on invalid input
  o 4968 : CMPI provider up-calls cause failure with out-of-process
  o 4978 : snmpDeliverTrap_netsnmp::_createSession function is not thread safe
  o 4983 : Memory leak in OOP indication generation
  o 4984 : Forked process hangs in system call
  o 4986 : Adding automated test for snmpIndication Handler
  (  http://cvs.opengroup.org/bugzilla/show_bug.cgi?id=? )
- apply upstream update to 'pegasus-2.5.1-warnings.patch' 

* Mon Apr 17 2006 Jason Vas Dias <jvdias@redhat.com> - 2:2.5.1-3
- Fix repupgrade (make it use correct paths)

* Fri Apr 14 2006 Jason Vas Dias <jvdias@redhat.com> - 2:2.5.1-2
- Apply patches for the two '2.5.2_APPROVED' upstream bugzillas 
  4934(4943) and 4945 :
  (http://cvs.opengroup.org/bugzilla/buglist.cgi?bug_id=4943%%2C4945)
- Fix the PATH_MAX and MAXHOSTNAMELEN issues (again)

* Thu Apr 06 2006 Jason Vas Dias <jvdias@redhat.com> - 2:2.5.1-1
- Upgrade to version 2.5.1 (including new upstream .spec file).

* Tue Mar  7 2006 Bill Nottingham <notting@redhat.com> - 2:2.5-9
- use an assigned uid/gid, do not loop over user ids looking for a free one

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2:2.5-6.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jason Vas Dias <jvdias@redhat.com> - 2:2.5-6
- restore SSLv23_method SSL support now that bug 173399 is fixed
- rebuild for new gcc, glibc, glibc-kernheaders
- PAMBasicAuthenticatorUnix.cpp includes no longer include syslog.h: add
- /usr/bin/install now decides to fail if chown fails - set $INSTALL_USER, $INSTALL_GROUP

* Thu Dec 15 2005 Jason Vas Dias <jvdias@redhat.com> - 2:2.5-5
- fix bug 175434 : deal with pegasus uid/gid already existing
  on first install

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com> - 2:2.5-4.1
- rebuilt

* Wed Nov 16 2005 Jason Vas Dias <jvdias@redhat.com> - 2:2.5-4
- fix bug 173401: SSL support broken by openssl-0.9.7g -> 0.9.8a upgrade 

* Wed Nov 09 2005 Jason Vas Dias <jvdias@redhat.com> - 2:2.5-3
- Rebuild for new openssl dependencies
- Enable CMPI support for sblim-cmpi-base with ENABLE_CQL=true

* Mon Oct 31 2005 Jason Vas Dias <jvdias@redhat.com> - 2:2.5-2
- Add /usr/lib/cmpi alternate providerLibDir for sblim-cmpi-base Fedora Extras pkg
- Fix bug 171124: use numeric ids for pegasus user/group
- guidelines: do not remove pegasus user/group in %%postun.

* Fri Oct 14 2005 Tomas Mraz <tmraz@redhat.com>
- use include instead of pam_stack in pam config

* Fri Sep 30 2005 Jason Vas Dias <jvdias@redhat.com> - 2:2.5-1
- Implemented new 'make install' target.
- Re-wrote tog-pegasus.spec file from scratch.
- Ported BZ 167986 authentication code and BZ 167164 + BZ 167165 fixes from RHEL-4

* Wed Sep 28 2005 Jason Vas Dias <jvdias@redhat.com> - 2:2.5-0
- Initial build.
