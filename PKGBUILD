# Script generated with Bloom
pkgdesc="ROS - Wrapper for the concorde traveling salesman problem solver. The code was obtained from http://www.math.uwaterloo.ca/tsp/concorde/downloads/downloads.htm all rights of it go to the corresponding authors David Applegate, Robert Bixby, Vasek Chvatal and William Cook. The library doesn't give a specific license, but is provided free for academic research use, for further licensing options contact William Cook."
url='http://www.math.uwaterloo.ca/tsp/concorde/downloads/downloads.htm'

pkgname='ros-kinetic-libconcorde-tsp-solver'
pkgver='0.6.12_1'
pkgrel=1
arch=('any')
license=('free for academic research, for further licensing contact Wiliam Cook'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-libqsopt'
)

depends=('ros-kinetic-libqsopt'
)

conflicts=()
replaces=()

_dir=libconcorde_tsp_solver
source=()
md5sums=()

prepare() {
    cp -R $startdir/libconcorde_tsp_solver $srcdir/libconcorde_tsp_solver
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

