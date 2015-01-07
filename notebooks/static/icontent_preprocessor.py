from IPython.nbconvert.preprocessors import *
import json
import itertools


class IContentPreprocessor(Preprocessor):
    def preprocess(self, nb, resources):
        print('>>>>>>>>preprocess')
        self.setVariables(nb, resources)
        return nb, resources

    def setVariables(self, nb, resources):
        print('>>>>>>>>>setVariables')
        sourcelist = [cell["source"].split("\n") for cell in nb["cells"] if cell["cell_type"] == 'markdown']
        allsource = list(itertools.chain(*sourcelist))

        resources['css'] = "/css/home.css"
        resources['sideleft'] = "sideleft.html"
        resources['links'] = [["Anthony Louis Burns", "http://www.anthonylouisburns.com", "pad0"], ["IContent", "http://www.anthonylouisburns.com/icontent/IContent.html", "pad0"], ["IContent - github", "https://github.com/anthonylouisburns/icontent/", "pad0"], ["Anthony Louis Burn - LinkedIn", "https://www.linkedin.com/in/anthonylouisburns", "pad0"]]

        css_list = [s.partition("=")[2].strip() for s in allsource if s.partition("=")[0] == "css"]
        sideleft_list = [s.partition("=")[2].strip() for s in allsource if s.partition("=")[0] == "sideleft"]
        links_list = [s.partition("=")[2].strip() for s in allsource if s.partition("=")[0] == "links"]

        if len(css_list)>0: resources['css']=css_list[-1]
        if len(sideleft_list)>0: resources['sideleft']=sideleft_list[-1]
        if len(links_list)>0: resources['links']=json.loads(links_list[-1])

        print(resources['links'])



class ExclamationPreprocessor(Preprocessor):
    def preprocess_cell(self, cell, resources, index):
        """
        Adds bold 'cheese' to the start of every markdown cell.
        """
        print('>>>>>>>preprocess_cell')

        if 'source' in cell and cell.cell_type == "markdown":
            cell.source = cell.source + '\n !!!!!!!!!!!!!!'
        return cell, resources