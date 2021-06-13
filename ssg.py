import typer 
import Site from ssg.site

def main(self, source="contents", dest="dist"):
    config = {
        "source": source
        "dest": dest
    }
    
    site = Site(**config).build()

typer(main(site))