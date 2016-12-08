Name:           ros-indigo-libpcan
Version:        0.6.10
Release:        0%{?dist}
Summary:        ROS libpcan package

Group:          Development/Libraries
License:        LGPL
URL:            http://p103112.typo3server.info/fileadmin/media/linux/index.htm
Source0:        %{name}-%{version}.tar.gz

Requires:       kernel-headers
Requires:       popt-devel
Requires:       ros-indigo-mk
Requires:       ros-indigo-roslib
Requires:       ros-indigo-rospack
BuildRequires:  kernel-headers
BuildRequires:  popt-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-mk
BuildRequires:  ros-indigo-roslib
BuildRequires:  ros-indigo-rospack

%description
This package wraps the libpcan to use it as a ros dependency

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu Dec 08 2016 Florian Weisshardt <fmw@ipa.fhg.de> - 0.6.10-0
- Autogenerated by Bloom

* Mon Oct 24 2016 Florian Weisshardt <fmw@ipa.fhg.de> - 0.6.9-0
- Autogenerated by Bloom

* Thu Oct 20 2016 Florian Weisshardt <fmw@ipa.fhg.de> - 0.6.7-0
- Autogenerated by Bloom

* Thu Oct 13 2016 Florian Weisshardt <fmw@ipa.fhg.de> - 0.6.6-0
- Autogenerated by Bloom

* Mon Oct 10 2016 Florian Weisshardt <fmw@ipa.fhg.de> - 0.6.5-0
- Autogenerated by Bloom

* Fri Apr 01 2016 Florian Weisshardt <fmw@ipa.fhg.de> - 0.6.4-0
- Autogenerated by Bloom

* Mon Aug 31 2015 Florian Weisshardt <fmw@ipa.fhg.de> - 0.6.3-0
- Autogenerated by Bloom

* Sat Aug 29 2015 Florian Weisshardt <fmw@ipa.fhg.de> - 0.6.2-1
- Autogenerated by Bloom

* Tue Aug 25 2015 Florian Weisshardt <fmw@ipa.fhg.de> - 0.6.2-0
- Autogenerated by Bloom

* Thu May 28 2015 Florian Weisshardt <fmw@ipa.fhg.de> - 0.6.1-0
- Autogenerated by Bloom

