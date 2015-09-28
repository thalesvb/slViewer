from os.path import sys
import platform

from cx_Freeze import setup, Executable
import cx_Freeze

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(
    build_exe='../build/exe.{0}-{1}-{2}'.format(cx_Freeze.sys.platform,
                                                platform.machine(),
                                                platform.python_version()),
    compressed=True,
    optimize=2,
    include_msvcr=False,
    packages=[],
    excludes=[],
)


base = 'Win32GUI' if sys.platform == 'win32' else None

executables = [
    Executable('Main.py', base=base, targetName='slViewer')
]

setup(name='slViewer',
      version='0.0.1',
      description='SAPLink file viewer written with wxPython Phoenix.',
      options=dict(build_exe=buildOptions),
      executables=executables,
      )
