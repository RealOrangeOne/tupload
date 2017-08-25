# Maintainer: Jake Howard <git+aur@theorangeone.net>
pkgname=tupload
pkgver=1.0.0
pkgrel=1
pkgdesc="Capture screenshots and upload them using rsync"
arch=('any')
url="https://github.com/RealOrangeOne/tupload"
license=('unknown')
depends=('python-setuptools' 'rsync' 'gnome-screenshot')
makedepends=('python-pip')
source=("$pkgname-$pkgver.tar.gz::https://github.com/RealOrangeOne/tupload/archive/master.tar.gz")
sha512sums=('SKIP')

package() {
  cd tupload-master
  python setup.py install --root="$pkgdir/" --optimize=1
}
