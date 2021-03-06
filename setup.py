import os
import sys
from distutils.core import setup

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'stoneEcommercePython'))

setup(
    name='stone_ecommerce_python',
    version='1.1.0',
    package_dir={
        'stoneEcommercePython': 'stoneEcommercePython',
        'data_contracts': 'stoneEcommercePython/data_contracts',
        'enum_types': 'stoneEcommercePython/enum_types',
        'stone_config': 'stoneEcommercePython/stone_config',
        'resource_clients': 'stoneEcommercePython/resource_clients',
        'transaction_report_file': 'stoneEcommercePython/transaction_report_file'
    },
    packages=[
        'stoneEcommercePython',
        'data_contracts',
        'enum_types',
        'stone_config',
        'resource_clients',
        'transaction_report_file'
    ],
    url='https://github.com/stone-pagamentos/stone-ecommerce-python',
    license='Apache',
    author='Stone Pagamentos',
    author_email='devcenter@stone.com.br',
    description='Sdk for integration with stone payment api',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.4'
    ],
    install_requires=[
        'requests>=2.0.0',
        'enum34>=1.0.0',
        'xmltodict>=0.9.2'
    ],
    keywords=[
        'stone',
        'rest',
        'sdk',
        'payments'
    ]
)
