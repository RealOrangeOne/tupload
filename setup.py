from setuptools import setup

setup(
    name="upload",
    version="1.0.0",
    install_requires=[],
    include_package_data=True,
    entry_points="""
        [console_scripts]
        upload=upload.upload:cli
    """
)
