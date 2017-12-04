import mymodule
mymodule.func_in_module()

# OR

import mymodule as mm
mm.func_in_module()

# OR

from mymodule import func_in_module
func_in_module()

# OR (though not recommended)

from mymodule import *
func_in_module()