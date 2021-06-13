from pathlib import Path

class Site:
    
    def __init__(self, source, dest, parsers=None):
        self.source = Path(source)
        self.dest = Path(dest)
        self.parsers = parsers or []
    
    def create_dir(self, path):
        directory = self.dest / path.relative_to(self.source)
        directory.mkdir(parents=True, exist_ok=True)
    
    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if path.isdir():
                self.create_dir(path)
            elif path.isfile():
                self.run_parser(path)
                
                
    
    def load_parser(self, extension):
        for parser in self.parsers:
            if extension.valid_extension():
                return parser
    
    def run_parser(self, path):
        path.load_parser(path.suffix(parser))
        if parser is not None:
            Parser.parse(path, self.source, self.dest)
        else:
            print("Not Implemented")
    
    
        
        
            
        
        
        
            
    
    
        