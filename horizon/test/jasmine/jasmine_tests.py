# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


from horizon.test import helpers as test


class ServicesTests(test.JasmineTests):
    sources = [
        'horizon/js/horizon.js',
        'horizon/js/angular/horizon.conf.js',
        'horizon/js/angular/horizon.js',
        'horizon/js/angular/services/horizon.utils.js',
        'horizon/js/angular/hz.api.module.js',
        'horizon/js/angular/services/hz.api.service.js',
        'angular/widget.module.js',
        'angular/action-list/action-list.js',
        'angular/bind-scope/bind-scope.js',
        'angular/charts/charts.js',
        'angular/charts/chart-tooltip.js',
        'angular/charts/pie-chart.js',
        'angular/help-panel/help-panel.js',
        'angular/metadata-tree/metadata-tree-service.js',
        'angular/modal/modal.js',
        'angular/table/table.js',
        'angular/transfer-table/transfer-table.js',
        'angular/wizard/wizard.js',
        'horizon/js/angular/filters/filters.js',
    ]
    specs = [
        'horizon/js/angular/services/hz.api.service.spec.js',
        'horizon/tests/jasmine/metadataWidgetControllerSpec.js',
        'horizon/tests/jasmine/utilsSpec.js',
        'angular/action-list/action-list.spec.js',
        'angular/bind-scope/bind-scope.spec.js',
        'angular/charts/pie-chart.spec.js',
        'angular/help-panel/help-panel.spec.js',
        'angular/modal/simple-modal.spec.js',
        'angular/table/table.spec.js',
        'angular/transfer-table/transfer-table.spec.js',
        'angular/wizard/wizard.spec.js',
        'horizon/js/angular/filters/filters.spec.js',
    ]
    externalTemplates = [
        'angular/action-list/action.html',
        'angular/action-list/menu-item.html',
        'angular/action-list/menu.html',
        'angular/action-list/single-button.html',
        'angular/action-list/split-button.html',
        'angular/charts/chart-tooltip.html',
        'angular/charts/pie-chart.html',
        'angular/help-panel/help-panel.html',
        'angular/transfer-table/transfer-table.html',
        'angular/wizard/wizard.html',
    ]
