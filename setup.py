import io
import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(here, "README.rst"), "rt", encoding="utf8") as f:
    readme = f.read()


setup(
    name="tutor-minio-tmp",
    version="0.0.5",
    url="https://docs.tutor.overhang.io/",
    license="AGPLv3",
    author="weijie",
    author_email="wejie00@foxmail.com",
    description="A Tutor plugin for object storage in MinIO",
    long_description=readme,
    packages=["tutorminiotmp"],
    include_package_data=True,
    python_requires=">=3.5",
    entry_points={"tutor.plugin.v0": ["minio = tutorminiotmp.plugin"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
