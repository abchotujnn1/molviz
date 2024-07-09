from setuptools import setup, find_packages

setup(
    name="molviz",
    version="0.0.1",

    packages=find_packages('src'),
    package_dir={'': 'src',},
    install_requires=["numpy", "pandas"],
    entry_points={'console_scripts':['molviz=molviz.main:main_function',]}
)
