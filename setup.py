from setuptools import setup, find_packages

setup(
    name='gemini_copilot',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'click',
        'google-generativeai',
        'python-dotenv'
    ],
    entry_points={
        'console_scripts': [
            'gemini-copilot = gemini_copilot:gemini_copilot',
        ]
    }
)
