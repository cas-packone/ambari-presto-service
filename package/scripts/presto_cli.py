# -*- coding: utf-8 -*-
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from resource_management import *


class Cli(Script):
    def install(self, env):
        Execute('wget sdvl3bdch001.td.teradata.com/RPMs/presto-cli-0.114-executable.jar -P /usr/lib/presto/bin')
        Execute('chmod +x /usr/lib/presto/bin/presto-cli-0.114-executable.jar')
        Execute('mv /usr/lib/presto/bin/presto-cli-0.114-executable.jar /usr/lib/presto/bin/presto-cli')

    def status(self, env):
        pass

    def configure(self, env):
        # Actual configuration is done in the master and worker configure() methods
        pass

if __name__ == '__main__':
    Cli().execute()