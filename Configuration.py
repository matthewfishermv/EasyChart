

class Configuration(object):

	def __init__(self):
		self.properties = {}

	def set_property(self, property, value):
		"""Sets property to value.

		Assumes property name references a valid property.
		Assumes every property has a unique property name.

		Subclasses can override this method to handle special cases.
		Subclass definitions must return Configuration.set_property() on success.

		Returns:
			True if property has been changed.
			False if no change was made or an error was encountered.
		"""

		if property in self.properties and value != self.properties[property]:
			self.properties[property] = value

			return True

		return False

	def get_properties(self): return self.properties
	def get_property(self, property_name): return self.properties[property_name]