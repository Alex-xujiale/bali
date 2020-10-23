from setuptools import find_packages, setup

INSTALL_REQUIREMENTS = [
    'fastapi[all]==0.61.1',
    'grpcio==1.32.0',
    'grpcio-tools==1.32.0',
    'django-mysql==3.2.0',
    'PyMySQL==0.10.1',
    'passlib[bcrypt]==1.7.2',
    'pillow==7.2.0',
    'python-jose[cryptography]==3.2.0',
    'Pillow==6.2.2',
    'redis==3.5.3',
    'SQLAlchemy==1.3.19',
    'sqla-wrapper==4.200628',
]

setup(
    name='bali',
    version='0.1.0',
    description='Simplify gRPC services and clients',
    url='https://github.com/JoshYuJump/bali',
    author='Josh.Yu',
    author_email='josh.yu_8@live.com',
    license='MIT',
    install_requires=INSTALL_REQUIREMENTS,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)