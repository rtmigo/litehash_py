from pathlib import Path


from setuptools import setup, find_packages


def load_module_dict(filename: str) -> dict:
    import importlib.util as ilu
    filename = Path(__file__).parent / filename
    spec = ilu.spec_from_file_location('', filename)
    module = ilu.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.__dict__


name = "zflow"

readme = (Path(__file__).parent / 'README.md').read_text(encoding="utf-8")
readme = "# " + readme.partition("\n#")[-1]

setup(
    name=name,
    version="0.0.0",

    author="Artëm IG",
    author_email="ortemeo@gmail.com",
    url='https://github.com/rtmigo/zflow_py',

    packages=find_packages(exclude=['tests']),

    install_requires=[
        "rcd@ git+https://github.com/rtmigo/rcd_py",
        "rcd_str@ git+https://github.com/rtmigo/rcd_str_py",
        "pickledir"
    ],

    description="",

    long_description=readme,
    long_description_content_type='text/markdown',

    #license="MIT",

    keywords="".split(),

    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Typing :: Typed",
     ],
)
