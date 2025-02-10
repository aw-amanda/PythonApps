# Print all available widgets within the QtWidgets module of PyQt5:

from PyQt5 import QtWidgets

# Get all classes within the QtWidgets module:
widget_classes = [cls_name for cls_name in dir(QtWidgets) if isinstance(getattr(QtWidgets, cls_name), type)]

# Filter for classes that inherit from QtWidgets.QWidget:
widget_names = [cls_name for cls_name in widget_classes if issubclass(getattr(QtWidgets, cls_name), QtWidgets.QWidget)]

# Print the list of widget names: 
for name in widget_names:
    print(name)