from IPython.nbconvert.preprocessors import *
import json
import itertools

class ItbPreprocessor(Preprocessor):
    """docstring for CheesePreprocessor"""
    def preprocess(self, nb, resources):
        print('preprocess')
        self.setVariables(nb, resources)
        return nb, resources

    def preprocess_cell(self, cell, resources, index):
        """
        Adds bold 'cheese' to the start of every markdown cell.
        """

        if 'source' in cell and cell.cell_type == "markdown":
            cell.source = '**cheese cheese cheese cheese cheese cheese cheese cheese cheese cheese cheese cheese cheese cheese cheese cheese** ' + cell.source
        return cell, resources

    def setVariables(self, nb, resources):
        print('setVariables')
        print(nb["cells"])
        sourcelist = [cell["source"].split("\n") for cell in nb["cells"] if cell["cell_type"] == 'markdown']
        allsource = list(itertools.chain(*sourcelist))

        resources['template'] = "full"
        resources['css'] = "custom.css"
        resources['sideleft'] = "default.html"
        resources['links'] = [['physics', 'physics.html', 'pad0'], ['chemistry', 'chemistry.html', 'pad1']]

        template_list = [s.partition("=")[2].strip() for s in allsource if s.partition("=")[0] == "template"]
        css_list = [s.partition("=")[2].strip() for s in allsource if s.partition("=")[0] == "css"]
        sideleft_list = [s.partition("=")[2].strip() for s in allsource if s.partition("=")[0] == "sideleft"]

        print("---------------")
        print(sourcelist)
        print("---------------")
        print("---------------")
        print(sideleft_list)
        print("---------------")
        if len(template_list)>0: resources['template']=template_list[-1]
        if len(css_list)>0: resources['css']=css_list[-1]
        if len(sideleft_list)>0: resources['sideleft']=sideleft_list[-1]

        print(resources['template'])
        print(resources['css'])
        print(resources['sideleft'])
        print(resources['links'])