# Copyright 2021-2023 Cambridge Quantum Computing Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__all__ = ['draw',
           'TextDiagramPrinter', 'diagram2str',
           'create_pregroup_diagram', 'is_pregroup_diagram', 'remove_cups',
           'remove_swaps']


from lambeq.pregroups.drawing import draw
from lambeq.pregroups.text_printer import TextDiagramPrinter, diagram2str
from lambeq.pregroups.utils import (create_pregroup_diagram,
                                    is_pregroup_diagram, remove_cups,
                                    remove_swaps)
