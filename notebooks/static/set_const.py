c = get_config()

#Export all the notebooks in the current directory to the sphinx_howto format.
c.Exporter.template_file = 'itb'
c.Exporter.preprocessors = ['itb_preprocessor.ItbPreprocessor']
