# Script generated with Bloom
pkgdesc="ROS - This package wraps the libphidgets to use it as a ros dependency"
url='http://ros.org/wiki/libphidgets'

pkgname='ros-kinetic-libphidgets'
pkgver='0.6.12_1'
pkgrel=1
arch=('any')
license=('LGPL'
)

makedepends=('libusb-compat'
'ros-kinetic-catkin'
)

depends=('libusb-compat'
)

conflicts=()
replaces=()

_dir=libphidgets
source=()
md5sums=()

prepare() {
    cp -R $startdir/libphidgets $srcdir/libphidgets
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

