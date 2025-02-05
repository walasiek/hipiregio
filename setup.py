from distutils.core import setup
import hipisejm


setup(
    name='hipiregio',
    version=hipiregio.__version__,
    author='Marcin Walas',
    author_email='kontakt@marcinwalas.pl',
    packages=[
        'hipiregio',
        'hipiregio.utils',
    ],
    scripts=[
        # 'bin/hipiregio-{script_name}.py'
    ],
    url='https://pypi.org/project/hipiregio/',
    license='LICENSE',
    description='Regionalisms, dialects and languages of Poland',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "pytest",
    ],
)
