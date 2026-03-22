def on_config(config, **kwargs):
    from defectdojo_api_generated.cli import __main__

    __main__.discover_commands()

    # TODO: mkdocs-click does not support class nor class methods - create PR for this
    from defectdojo_api_generated.cli.commands import cli

    cli._docs_cli_ = cli.CLI.click

    return config
