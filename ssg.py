import typer 
from ssg.site import Site

def main(source="contents", dest="dist"):
    config = {
        "source": source,
        "dest": dest
    }
    
    Site(**config).build()

typer(main)