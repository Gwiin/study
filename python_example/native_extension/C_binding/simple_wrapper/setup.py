from setuptools import Extension, setup
setup(
    name = "simple-hello",
    version = "0.1.0",
    packages=["simple_hello"],
    ext_modules=[
        Extension("simple_hello._hello_core", ["simple_hello/_hello_core.c"])
    ],
    package_data={"simple_hello":["*.pyi","py.typed"]},
    include_package_data=True,
    zip_safe=False
)