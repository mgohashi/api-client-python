from setuptools import setup, find_packages

requires = [
    "tornado"
]

setup(
    name='ApiClient',
    version='0.1',
    packages=find_packages(),
    url='',
    license='',
    author='Marcelo Ohashi',
    author_email='mohashi@gmail.com',
    description='API Client with some methods to demonstrate a REST API',
    install_reqs=requires,
    entry_points='''
        [console_scripts]
        run-api-client=apiclient:main
    '''
)
