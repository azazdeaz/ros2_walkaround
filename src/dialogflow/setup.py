from setuptools import setup

package_name = 'dialogflow'

setup(
    name='dialogflow',
    version='0.0.0',
    packages=['dialogflow'],
    py_modules=[],
    install_requires=['setuptools'],
    author='András Polgár',
    author_email='azazdeaz@gmail.com',
    maintainer='András Polgár',
    maintainer_email='azazdeaz@gmail.com',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='Package containing examples of how to use the rclpy API.',
    license='Apache License, Version 2.0',
    test_suite='test',
    data_files      = [
       ('share/' + package_name, ['package.xml'])
    ],
    zip_safe=True,
    entry_points={
        'console_scripts': [
            'listen = dialogflow.listen:main',
            'talk = dialogflow.talk:main',
        ],
    },
)
