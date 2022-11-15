from datetime import datetime
from pubsub import pub
import traceback


def log_func(func):
	"""
	Log decorator, logs function, values and docstrings

	:param func: Function to be decorated
	:return: Wrapper-function
	"""

	def wrapper(self, *args, **kwargs):
		message = datetime.now().strftime("%d/%m/%Y %H:%M:%S")  # Add date and time information
		message += f" - {func.__name__}({args}, {kwargs}):{func.__doc__}"  # Log-data for function call
		pub.sendMessage("DIN MOR", message=message)  # Send the message with pubsub

		return func(self, *args, **kwargs)

	return wrapper


def log_error(func):
	""" Log error and relevant info """

	def wrapper(self, *args, **kwargs):
		try:
			return func(self, *args, **kwargs)
		except:
			message = datetime.now().strftime("%d/%m/%Y %H:%M:%S")  # Add date and time information
			message += f" - Error in {func.__name__}({args}, {kwargs}):\n{traceback.format_exc()}"
			pub.sendMessage("DIN MOR", message=message)

	return wrapper
