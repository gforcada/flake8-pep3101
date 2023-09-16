from setuptools import setup

short_description = 'Checks for old string formatting.'


def read_file(filename):
    with open(filename) as file_obj:
        file_contents = file_obj.read()
    return file_contents


long_description = f"""
{read_file('README.rst')}
{read_file('CHANGES.rst')}
"""


setup(
    name='flake8-pep3101',
    version='2.0.1.dev0',
    description=short_description,
    long_description=long_description,
    # Get more from https://pypi.org/classifiers/
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Framework :: Flake8',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development',
        'Topic :: Software Development :: Quality Assurance',
    ],
    python_requires='>=3.8',
    keywords='pep8 pycodestyle flake8 python string formatting',
    author='Gil Forcada',
    author_email='gil.gnome@gmail.com',
    url='https://github.com/gforcada/flake8-pep3101',
    license='GPL version 2',
    py_modules=['flake8_pep3101'],
    include_package_data=True,
    test_suite='run_tests',
    zip_safe=False,
    install_requires=['flake8'],
    extras_require={'test': ['pytest']},
    entry_points={'flake8.extension': ['S001 = flake8_pep3101:Flake8Pep3101']},
)
