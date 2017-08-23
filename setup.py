from setuptools import setup

setup(
    name="tupload",
    version="1.0.0",
    install_requires=[],
    include_package_data=True,
    entry_points="""
        [console_scripts]
        upload=tupload.upload:cli
        screenshot=tupload.screenshot:cli
    """
)
