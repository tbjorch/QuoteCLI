from setuptools import setup

setup(
    name="Quote CLI",
    version="0.1",
    author="Tobias Bjorch",
    py_modules=["quote", "quote_scraper"],
    install_requires=["Click", "BeautifulSoup4", "requests"],
    entry_points="""
        [console_scripts]
        quote=quote:quote
    """,
)
