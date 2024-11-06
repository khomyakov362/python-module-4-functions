from sys import path

import package.folder1
import package.folder1.package_module_1
import package.folder1.package_module_2
import package.folder2
import package.folder2.folder21
import package.folder2.folder21.package_module_5
import package.folder2.folder21.package_module_6
import package.folder2.package_module_3
import package.folder2.package_module_4
path.append('/package')

import modules.module_1
import modules.module_2
import package

modules.module_1.say_module_1()
modules.module_2.say_module_2()

package.folder1.package_module_1.say_package_module_1()
package.folder1.package_module_2.say_package_module_2()
package.folder2.package_module_4.say_package_module_4()
package.folder2.package_module_3.say_package_module_3()
package.folder2.folder21.package_module_5.say_package_module_5()
package.folder2.folder21.package_module_6.say_package_module_6()






