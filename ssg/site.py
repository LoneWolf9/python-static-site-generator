from pathlib import Path

class Site:
    
    def __init__(self, source, dest):
        source = source.Path(source)
        dest = dest.Path(dest)
        
        self.source = source
        self.dest = dest
    
    def create_dir(self, path):
        directory = self.dest / path.relative_to(self.source)
        directory.mkdir(parents=True, exist_ok=True)
    
    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        
        for path in self.source.rglog("*"):
            if path.is_dir():
                create_dir(path)
        
        
            
        
        
        
            
    
    
        