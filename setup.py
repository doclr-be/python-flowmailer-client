import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='doclr_flowmailer_client',
    version='0.0.1',
    author='Doclr',
    author_email='info@doclr.be',
    description='Flowmailer client for sending transactional emails',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/doclr-be/python-flowmailer-client',
    project_urls = {
        "Bug Tracker": "https://github.com/doclr-be/python-flowmailer-client/issues"
    },
    license='MIT',
    packages=['doclr_flowmailer_client'],
    install_requires=['requests'],
)
