"""
IX-ThePlague CLI Entry Point

Enables command-line interaction for infectious disease queries,
printing concise answers directly to the terminal.
"""

import sys
from core.query_processor import IXThePlagueQueryProcessor

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py \"Your infectious disease question here\"")
        sys.exit(1)

    query = sys.argv[1]
    processor = IXThePlagueQueryProcessor()
    response = processor.process_query(query)

    print("\n🦠 IX-ThePlague Response 🦠")
    print(response)

if __name__ == "__main__":
    main()
