import Path from pathlib

class Site():
    
    def __init__(self, source, dest):
        source = source.Path()
        dest = dest.Path()
        
        self.source = source
        self.dest = dest
    
    def create_dir(self, path):
        directory = path.relative_to('{self.dest} / {self.source}')
        directory.mkdir(parents=True, exist_ok=True)
    
    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        
        for path in self.source.rglob("*"):
            if path == "directory":
                create_dir(path)
        
        
            
        
        
        
            
    
    
        