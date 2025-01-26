from abc import ABC, abstractmethod

class Character(ABC):
    """This a Character Abstract class"""

    @abstractmethod
    def __init__(self, first_name, is_alive=True) -> None:
        """This is the initial function called for Character"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self) -> None:
        """This is to change from alive to dead"""
        self.is_alive = False   
    


    

class Stark(Character):
      """This is a Stark class"""
      def __init__(self, first_name, is_alive=True):
        """This is the initial function called for Stark"""
        super().__init__(first_name, is_alive)

      def __repr__(self):
        """This is rewriting the print output message"""
        return("This is the Stark Class created")

def main() -> None:
    try:
        print("creating Stark Object from class")
        print(Stark("tofara"))
        print("creating Character Object from class")
        character = Character("tofara")
        print("Character created")
    except Exception as e:
        print(f"Error occured {e}")


if __name__ == "__main__":
    main()