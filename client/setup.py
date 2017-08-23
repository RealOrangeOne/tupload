from setuptools import setup, find_packages

setup(
    name="upload",
    version="1.0.0",
    install_requires=[],
    include_package_data=True,
    entry_points="""
        [console_scripts]
        upload=upload:cli
    """
)
