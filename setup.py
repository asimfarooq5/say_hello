from setuptools import setup

setup(
    name='say_hello',
    version='0.0.1',
    packages=['say_hello'],
    entry_points={
        'console_scripts': [
            'hello = say_hello.say:hello',
        ]
    }
)

# if __name__ == '__main__':
#     setup()
