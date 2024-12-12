from cffi import FFI
import platform
import os

if platform.system() == 'Windows':
    os.environ["PATH"] += 'C:\\msys64\\mingw64\\bin;'

ffibuilder = FFI()

ffibuilder.cdef('void interpret_code(const char*, size_t, bool, double);')
ffibuilder.cdef('void init_bf(void);')
ffibuilder.cdef('void end_bf(void);')
ffibuilder.cdef('void set_frame_size(size_t s);')
ffibuilder.cdef('void init_display(void);')

ffibuilder.set_source("_brainfrick",
    """
        #include "brainfrick.h"
    """,
        sources=['brainfrick.c'], extra_compile_args=['-O2',  '-march=native', '-DNDEBUG', '-D__USE_ANSI_MINGW_STDIO=0 '], libraries=['ncursesw'] if platform.system() != 'Windows' else ['ucrtbase', 'winmm', 'PowrProf'])


if __name__ == "__main__":
    ffibuilder.compile(verbose=True)