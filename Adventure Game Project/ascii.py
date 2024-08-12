class AsciiArt:
    def __init__(self, art: str, name: str = " rand"):
        """
        Initialize an AsciiArt object.

        :param art: The ASCII art as a string
        :param name: The name of the ASCII art (default: "Untitled")
        """
        self.art = art
        self.name = name

    def display(self):
     school = r"""
                \_/
              --(_)--  .
                / \   /_\
                      |Q|
                .-----' '-----.                                  __
               /____[SCHOOL]___\                                ()))
                | [] .-.-. [] |                                (((())
              ..|____|_|_|____|..................................)(... ldb
            
            
            """
        print(self.art)
     print(school)