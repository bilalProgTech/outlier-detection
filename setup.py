from setuptools import setup

with open("README.md","r") as fh:
    long_description = fh.read()

setup(
      name='outlier_detection',
      version='1.0.4',
      description='Detect outliers from pandas dataframe using various statistical tools',
      py_modules=["outlier_detection"],
      package_dir={'':'outlier_detection'},
      long_description = long_description,
      long_description_content_type="text/markdown",
      install_requires=[
          'seaborn==0.11.1',
          'matplotlib==3.2.2'
      ]
)