from setuptools import find_packages, setup

setup(
    name='mcqgenerator',
    packages=find_packages(),
    version='0.1.0',
    author='saurabh sharma',
    author_email='saurabh.sharma.phe20@itbhu.ac.in',
    install_requires=['openai','langchain','streamlit','python-dotenv','PyPDF2']
)