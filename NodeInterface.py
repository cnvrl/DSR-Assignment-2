from abc import ABC, abstractmethod
from datetime import date

class NodeInterface(ABC):
    """
    A Python abstract base class that holds a number of methods to be implemented
    in the Node class.

    @version Dec 2024
    """

    @abstractmethod
    def get_id(self) -> int:
        """
        Get account id.

        :return: account id
        """
        pass

    @abstractmethod
    def get_name(self) -> str:
        """
        Get account name.

        :return: account name
        """
        pass

    @abstractmethod
    def get_suburb(self) -> str:
        """
        Get suburb.

        :return: suburb
        """
        pass

    @abstractmethod
    def get_date_ob(self) -> date:
        """
        Get date of birth.

        :return: date of birth
        """
        pass

    @abstractmethod
    def __str__(self) -> str:
        """
        A string representation of a Node object.

        :return: a string that contains info about a Node object.
        """
        pass

    @abstractmethod
    def __hash__(self) -> int:
        """
        overrides a hash code value for the object.  Students should not uses Python's built-in `hash` method for the
        object as it might depend on memory address or other internal details.

        :return: Custom hash code value for the Node object.
        """
        pass

    @abstractmethod
    def __eq__(self, other: object) -> bool:
        """
        Indicates whether another object is "equal to" this one or not.

        :param other: the reference object with which to compare.
        :return: True if this object is the same as the `other` argument; False otherwise.
        """
        pass

    @abstractmethod
    def __lt__(self, other: object) -> bool:
        """
        Define the less-than operator for Node objects based on their ID.
        
        :param other: Another Node object to compare to.
        :return: True if this Node's ID is less than the other's ID, False otherwise.
        """
        pass