from setuptools import find_packages, setup

setup(
    name='bagles',
    version='1.0',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['bagles=bagles.main:main']
    }
)
