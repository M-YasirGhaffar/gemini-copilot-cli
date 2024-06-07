from setuptools import setup, find_packages

setup(
    name='gemini_copilot',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'gemini-copilot=gemini_copilot.__main__:main',
        ],
    },
    install_requires=[
        'google-generativeai',
        'prompt_toolkit',
        'markdown2',
        'python-dotenv',
        'requests'  # if needed
    ],
    python_requires='>=3.6',
    author='Yasir',
    author_email='yasirghaffar.nust@proton.me',
    description='A CLI tool to interact with Gemini AI.',
    long_description=open('README.md').read(),
    license='MIT',
    url='https://m-yasir-ghaffar.web.app',
)
