from setuptools import setup, find_packages

setup(
    name="tupload",
    version="1.0.0",
    install_requires=[],
    include_package_data=True,
    zip_safe=False,
    packages=find_packages(exclude=[]),
    entry_points="""
        [console_scripts]
        tupload=tupload.upload:cli
        upload=tupload.upload:cli
        screenshot=tupload.screenshot:cli
        redist=tupload.redistribute:cli
    """
)
