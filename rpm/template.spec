Name:           ros-indigo-libdlib
Version:        0.6.6
Release:        0%{?dist}
Summary:        ROS libdlib package

Group:          Development/Libraries
License:        LGPL
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-mk
Requires:       ros-indigo-roslib
Requires:       ros-indigo-rospack
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-mk
BuildRequires:  ros-indigo-roslib
BuildRequires:  ros-indigo-rospack

%description
This package wraps the external c++ library dlib (http://dlib.net/) in a ROS
package, so other packages can use it. It downloads the source code of it and
then builds it, corresponding to the web page of it, using cmake. The build
library is a static library and will be copied to the created common/lib folder.
The necessary header files will be copied to the common/include folder. The
include folder needs to exist before building the package, because in the
CMakeLists you have to specify where the headers are and if the folder doesn't
exist, catkin won't be able to build the package. For further descriptions and
tutorials see the Makefile.tarball and http://dlib.net/ .

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
* Thu Oct 13 2016 Richard Bormann <richard.bormann@ipa.fraunhofer.de> - 0.6.6-0
- Autogenerated by Bloom

* Mon Oct 10 2016 Richard Bormann <richard.bormann@ipa.fraunhofer.de> - 0.6.5-0
- Autogenerated by Bloom

