c = get_config()


#Export all the notebooks in the current directory to the sphinx_howto format.
c.Exporter.template_file = 'icontent'
c.Exporter.preprocessors = ['icontent_preprocessor.IContentPreprocessor','icontent_preprocessor.ExclamationPreprocessor']

