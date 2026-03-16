import classyclick

from defectdojo_api_generated.client import DefectDojo

from .cli import CLI


class Version(CLI.Command, classyclick.Command):
    client: DefectDojo = classyclick.ContextMeta('client')

    def __call__(self):
        print(next(self.client.findings_api.list_iterator()).result.title)
