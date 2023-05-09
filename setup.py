from setuptools import setup

setup(
    name='maksim-custom-serializer',
    version='0.1.0',
    packages=[
        "lab3.serializer.src"
    ],
    entry_points={
        'console_scripts': [
            "custom-serialize = lab3.serializer.custom:main"
        ]
    },
    url="maksiksay@gmail.com",
    license='MIT',
    author='maksiksay',
    author_email='maksiksay@gmail.com',
    description='Python JSON and XML serializer',
)
