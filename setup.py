from distutils.core import setup
setup(
    name="Pudding",
    packages=["Pudding"],
    version='1.0',
    license='MIT',
    description='An easy and simple package to find semantic communities',
    author='Buër Jean-Maxime',
    author_email='jeanmaxime.buer.pro@gmail.com',
    url='https://github.com/BuerJeanMaxime/pudding',
    keywords=['NLP','graph theory','semantic','louvain','pyhton','easy'],
    install_requires=['spacy','network','community'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: NLP community detection',
        'License :: OSI Approved :: MIT License',  # Again, pick a license
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)