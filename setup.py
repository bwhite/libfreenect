#!/usr/bin/env python
from distutils.core import setup
from distutils.extension import Extension

ext_modules = [Extension("freenect", ["freenect.c", 'src/tilt.c', 'src/core.c',
                                      'src/cameras.c', 'src/usb_libusb10.c',
                                      'wrappers/c_sync/libfreenect_sync.c'],
                         libraries=['usb-1.0'],
                         runtime_library_dirs=['/usr/local/lib', '/usr/local/lib64', '/usr/lib/'],
                         extra_compile_args=['-fPIC', '-I', '../../include/',
                                             '-I', '/usr/include/libusb-1.0/',
                                             '-I', '/usr/local/include/libusb-1.0',

                                             '-I', '/Library/Python/2.6/site-packages/numpy-1.5.1-py2.6-macosx-10.6-universal.egg/numpy/core/include',
                                             '-I', '/usr/local/include',
                                             '-I', '../c_sync/',
                                             '-I', 'wrappers/c_sync/',
                                             '-I', 'include/'])]
setup(
  name = 'freenect',
  version='0.0.1',
  ext_modules = ext_modules
)
