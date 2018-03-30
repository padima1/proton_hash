from distutils.core import setup, Extension

proton_hash_module = Extension('proton_hash',
                                 sources = ['protonmodule.c',
                                            'proton.c',
                                            'sha3/blake.c',
                                            'sha3/bmw.c',
                                            'sha3/groestl.c',
                                            'sha3/jh.c',
                                            'sha3/keccak.c',
                                            'sha3/skein.c',
                                            'sha3/cubehash.c',
                                            'sha3/echo.c',
                                            'sha3/luffa.c',
                                            'sha3/simd.c',
                                            'sha3/shavite.c'],
                               include_dirs=['.', './sha3', './sha3/ctaes'])

setup (name = 'proton_hash',
       version = '2.0.1',
       description = 'Binding for Proton proof of work hashing.',
       ext_modules = [proton_hash_module])
