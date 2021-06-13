import shutil

from typing import List

from pathlib import Path

class Parser:
    
    extensions = [].List[str]
    
    def valid_extension(self, extension):
        return extensions[extension]
    
    def parse(self, path, source, dest):
        self.path = Path(path)
        self.source = Path(source)
        self.dest = Path(dest)
        
        raise NotImplementedError
    
    def read(self, path):
        with open(path, 'r') as file:
            return self.read(file)
    
    def write(self, path, dest, content, ext=".html"):
        full_path = self.dest / path.with_suffix(ext).name
        with open(full_path, 'w') as file:
            self.content.write(file)
    
    def copy(self, path, source, dest):
        path.copy2(self.dest / path.relative_to(self.source))
    
    
    class ResourceParser(Parser):
        
        extensions = [".jpg", ".png", ".gif", ".css", ".html"]
        
        def parse(self, path, source, dest):
            Parser.copy(path, source, dest)
        
           
            
        
        
        
    
    