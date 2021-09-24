from setuptools import setup

setup(name='downloadpdf',
      version='1.0.7',
      description='Download PDF from URL',
      long_description='For more information visit code repository.',
      url='https://github.com/PythonCheatsheet/downloadpdf/',
      author='Anit Shrestha Manandhar',
      author_email='codeanit@gmail.com',
      maintainer='Anit Shrestha Manandhar',
      maintainer_email='codeanit@gmail.com',
      license='MIT',
      packages=['downloadpdf', 'main', 'util'],
      zip_safe=False,
      python_requires='>=3.6',
      install_requires=['beautifulsoup4==4.10.0'],
      platforms='ubuntu-latest',
      keywords='Download, PDF, Scrap')
