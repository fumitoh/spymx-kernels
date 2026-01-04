# GitHub Copilot Instructions for spymx-kernels

This repository provides custom IPython kernels for the Spyder plugin for modelx. The kernels extend Spyder's functionality to work with modelx models.

## Project Structure

- `spymx_kernels/console/kernel.py` - Main kernel implementation (for spyder-kernels 3.x+)
- `spymx_kernels/console/kernel_5.py` - Kernel implementation (for spyder-kernels 1-2.x)
- `spymx_kernels/start_kernel.py` - Kernel startup script
- `spymx_kernels/utility/` - Utility modules for type handling and encoding

## modelx API Usage by Source File

### spymx_kernels/console/kernel.py

This file uses the following modelx APIs:

#### Module Imports
- `from modelx.core import mxsys` - Access to modelx system
- `import modelx as mx` - Main modelx module
- `from modelx.core.space import ItemSpace, BaseSpace` - Space classes
- `from modelx.core.parent import BaseParent` - Parent container class (modelx > 0.19)
- `from modelx.core.spacecontainer import BaseSpaceContainer` - Space container class (modelx <= 0.19)
- `from modelx.core.reference import ReferenceProxy` - Reference proxy class
- `from modelx.core.base import Interface` - Base interface class
- `from modelx.core.cells import Interface` - Cells interface class
- `from modelx.io.baseio import BaseDataClient` - I/O spec class (modelx < 0.18)
- `from modelx.io.baseio import BaseDataSpec` - I/O spec class (modelx < 0.20)
- `from modelx.io.baseio import BaseIOSpec` - I/O spec class (modelx >= 0.20)

#### modelx Functions and Methods
- `mx.new_model(name)` - Create a new model
- `mx.read_model(modelpath, name)` - Read a model from file
- `mx.write_model(model, modelpath, backup)` - Write a model to file
- `mx.zip_model(model, modelpath, backup)` - Write a model as a zip file
- `mx.get_models()` - Get dictionary of all models
- `mx.cur_model()` - Get current model
- `mx.get_object(fullname, as_proxy=True/False)` - Get modelx object by name
- `mx.VERSION` - modelx version tuple
- `mx.__version__` - modelx version string
- `mx.core.space.ItemSpace` - Item space class access

#### modelx Object Methods
- `model._get_from_name(name)` - Get child object from model by name
- `model.cur_space()` - Get current space in model
- `model.new_space(name=None, bases=None)` - Create new space in model
- `model.close()` - Close model
- `model._get_attrdict(attrs, recursive=False)` - Get model attributes as dictionary
- `model._get_assoc_values()` - Get associated values from model
- `parent.new_space(name=None, bases=None)` - Create new space in parent
- `parent.new_cells(name=None, formula=None)` - Create new cells in parent
- `parent.__delattr__(name)` - Delete attribute from parent
- `obj.node(*args)` - Get node from cells object
- `obj.set_formula(formula)` - Set formula for cells
- `obj._get_attrdict(attrs, recursive=False, extattrs=None)` - Get object attributes
- `obj.spaces` - Access spaces collection
- `obj.cells` - Access cells collection
- `obj.refs` - Access references collection
- `obj.parent` - Access parent object
- `obj.name` - Get object name
- `obj.value` - Get reference value (for ReferenceProxy)
- `node.predecessors` - Get predecessor nodes
- `node.succs` - Get successor nodes
- `spec._get_attrdict()` - Get I/O spec attributes

### spymx_kernels/console/kernel_5.py

This file uses the following modelx APIs:

#### Module Imports
- `from modelx.core import mxsys` - Access to modelx system
- `import modelx as mx` - Main modelx module
- `from modelx.core.space import ItemSpace, BaseSpace` - Space classes
- `from modelx.core.parent import BaseParent` - Parent container class (modelx > 0.19)
- `from modelx.core.spacecontainer import BaseSpaceContainer` - Space container class (modelx <= 0.19)
- `from modelx.core.reference import ReferenceProxy` - Reference proxy class
- `from modelx.core.base import Interface` - Base interface class
- `from modelx.core.cells import Interface` - Cells interface class
- `from modelx.io.baseio import BaseDataClient` - I/O spec class (modelx < 0.18)
- `from modelx.io.baseio import BaseDataSpec` - I/O spec class (modelx < 0.20)
- `from modelx.io.baseio import BaseIOSpec` - I/O spec class (modelx >= 0.20)

#### modelx Functions and Methods
- `mx.new_model(name)` - Create a new model
- `mx.read_model(modelpath, name)` - Read a model from file
- `mx.write_model(model, modelpath, backup)` - Write a model to file
- `mx.zip_model(model, modelpath, backup)` - Write a model as a zip file
- `mx.get_models()` - Get dictionary of all models
- `mx.cur_model()` - Get current model
- `mx.get_object(fullname, as_proxy=True/False)` - Get modelx object by name
- `mx.VERSION` - modelx version tuple
- `mx.__version__` - modelx version string
- `mx.core.space.ItemSpace` - Item space class access

#### modelx Object Methods
- `model._get_from_name(name)` - Get child object from model by name
- `model.cur_space()` - Get current space in model
- `model.new_space(name=None, bases=None)` - Create new space in model
- `model.close()` - Close model
- `model._get_attrdict(attrs, recursive=False)` - Get model attributes as dictionary
- `model._get_assoc_values()` - Get associated values from model
- `parent.new_space(name=None, bases=None)` - Create new space in parent
- `parent.new_cells(name=None, formula=None)` - Create new cells in parent
- `parent.__delattr__(name)` - Delete attribute from parent
- `obj.node(*args)` - Get node from cells object
- `obj.set_formula(formula)` - Set formula for cells
- `obj._get_attrdict(attrs, recursive=False, extattrs=None)` - Get object attributes
- `obj.spaces` - Access spaces collection
- `obj.cells` - Access cells collection
- `obj.refs` - Access references collection
- `obj.parent` - Access parent object
- `obj.name` - Get object name
- `obj.value` - Get reference value (for ReferenceProxy)
- `node.predecessors` - Get predecessor nodes
- `node.succs` - Get successor nodes
- `spec._get_attrdict()` - Get I/O spec attributes

### spymx_kernels/start_kernel.py

This file does not directly use modelx APIs. It imports and instantiates the ModelxKernel class.

### setup.py

This file does not use modelx APIs. It only mentions "modelx" in metadata strings (keywords, description).

## Coding Conventions

1. **Import Style**: modelx is typically imported as `mx` for brevity
2. **Version Checking**: Use `mx.VERSION` tuple for feature detection across modelx versions
3. **Error Handling**: Methods that retrieve objects should handle `NameError` when objects don't exist
4. **Proxy Objects**: Use `as_proxy=True` parameter when working with references that should remain as proxies
5. **Attribute Dictionaries**: Use `_get_attrdict()` method to serialize modelx objects for communication
6. **Version Compatibility**: Code handles multiple modelx versions (< 0.18, < 0.20, >= 0.20) with conditional imports
7. **Space Hierarchy**: Check for `ItemSpace` instances when traversing space hierarchies to find non-item parents

## Dependencies

- **spyder-kernels**: Base kernel implementation (>=1.8.1)
- **modelx**: Core modeling library (not explicitly required in setup.py but required at runtime)
- **cloudpickle**: For serializing Python objects
- **IPython/Jupyter**: Kernel infrastructure
