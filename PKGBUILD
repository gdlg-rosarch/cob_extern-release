# Script generated with Bloom
pkgdesc="ROS - Wrapper for the Qsopt linear programming solver. The code was obtained from http://www.math.uwaterloo.ca/~bico/qsopt/index.html, all rights on Qsopt go to the authors David Applegate, William Cook, Sanjeeb Dash, and Monika Mevenkamp. The library doesn't explicitly provide a license, but allows the free use for research or educational purposes. For further questions on licensing, contact the previous listed authors."
url='http://www.math.uwaterloo.ca/~bico/qsopt/index.html'

pkgname='ros-kinetic-libqsopt'
pkgver='0.6.12_1'
pkgrel=1
arch=('any')
license=('free for research or education purpose, all rights maintained by David Applegate, William Cook, Sanjeeb Dash, and Monika Mevenkamp'
)

makedepends=('dpkg'
'ros-kinetic-catkin'
)

depends=('dpkg'
)

conflicts=()
replaces=()

_dir=libqsopt
source=()
md5sums=()

prepare() {
    cp -R $startdir/libqsopt $srcdir/libqsopt
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

