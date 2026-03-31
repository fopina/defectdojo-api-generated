def on_config(config, **kwargs):
    # TODO: mkdocs-click does not support class nor class methods - create PR for this
    # so `cli.md` can use `CLI.click` directly instead of monkeypatched `_docs_cli_`
    from defectdojo_api_generated.cli.commands import cli
    from defectdojo_api_generated.cli.commands.cli import CLI

    cli._docs_cli_ = CLI.click

    return config
