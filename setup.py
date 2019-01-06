from setuptools import setup, find_packages

requires = [
    "tornado>=5,<6"
]

setup(
    name='ApiClient',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/mgohashi/api-client-python',
    license='',
    author='Marcelo Ohashi',
    author_email='mohashi@gmail.com',
    description='API Client with some methods to demonstrate a REST API',
    install_requires=requires,
    include_package_data=True,
    entry_points='''
        [console_scripts]
        run-api-client=apiclient:main
    '''
)
