class Stack:
	"""
	Stack Datta Structure
	"""
	def __init__(self) -> None:
		self.items = []

	def push(self, item:str) -> list:
		"""
		this method add items to the stack

		Parameters
		----------
		item : any
			item refers to any data type

		Returns
		-------
		list
			here list is a stack
		"""

		return self.items.append(item)

	def pop(self) -> list:
		"""
		This method will remove the top 
		element of the stack

		Returns
		-------
		list
			list would be the updated 
			stack list
		"""
		return self.items.pop()

	def peek(self)->any:
		"""
		This method will return the top
		value of the stack

		Returns
		-------
		any
			any python data type
		"""
		return self.items[len(self.items)-1]

	def is_empty(self) -> bool:
		"""
		This method will return True if the stack is empty
		and False if the stack is not empty

		Returns
		-------
		bool
			True or False
		"""

		return True if len(self.items)==0 else False


	def get_stack(self) -> list:
		"""
		to check the stack

		Returns
		-------
		list
			
		"""
		return self.items
