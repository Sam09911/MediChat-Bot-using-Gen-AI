from setuptools import find_packages, setup

setup(
    name='Generative AI Project',
    version='0.0.0',
    author='Sameer',
    author_email='attarmohammadsameer@gmail.com',
    packages=find_packages(),
    install_requires=[
        "sentence-transformers==2.2.2",
        "langchain",
        "flask",
        "pypdf",
        "python-dotenv",
        "pinecone-client[grpc]",  # Corrected package name
        "langchain-pinecone",
        "langchain_community",
        "langchain_openai",
        "langchain_experimental",
    ],
)
