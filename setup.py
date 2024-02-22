from setuptools import setup, find_packages

setup(
    name='gemini-copilot',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'google-generativeai',
        'python-dotenv',
    ],
    entry_points={
        'console_scripts': [
            'gemini-copilot=gemini_copilot:gemini_copilot',
        ],
    },
)