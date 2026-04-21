# CLI Reference

This page provides documentation for the command line tool `dojo`.

<script src="https://asciinema.org/a/fIPDy8iYxGL85pXb.js" id="asciicast-fIPDy8iYxGL85pXb" async="true"></script>

> [uv](https://docs.astral.sh/uv/) recommended or [pipx](https://github.com/pypa/pipx)

```
uv tool install defectdojo-cli
```

::: mkdocs-click
    :module: defectdojo_api_generated.cli.commands.cli
    :command: _docs_cli_
    :prog_name: dojo
    :list_subcommands: true
    :depth: 2

### config.toml

The CLI reads its configuration from `config.toml`. By default it looks in the user config directory for
`defectdojo-generated-api/config.toml`, and if the file does not exist yet it will create one from the bundled example.

The important thing to know is that `config.toml` is tightly coupled to the CLI flags: config keys act as defaults for
options exposed by the root command and subcommands/groups. In practice, if a command supports a flag, the same option
name can usually be provided in `config.toml`, and a command-line flag still wins if both are set.

The main exceptions are `--config` and `--env`:

- `--config` only tells the CLI which TOML file to load, so it is not itself a value carried inside `config.toml`
- `--env` selects which `[env.<name>]` section to merge, so the config file uses `default_env` to provide its default value

Common examples:

- `host`: default value for `--host`
- `token`: default value for `--token`
- `user`: default value for `--user`
- `password`: default value for `--password`
- `disable_tls`: default value for `--disable-tls`
- `default_env`: default environment used when `--env` is not passed

This is not meant to be a rigid exhaustive list. The config file is primarily a place to pre-fill the same options you
would otherwise pass on the command line.

Authentication rules:

- If `token` is set, it is used and `user` / `password` are ignored.
- If `token` is not set, the CLI uses `user` and `password`.
- Command-line flags override values from the config file.

Environment rules:

- Root-level values are the base configuration.
- `default_env` picks a named entry under `[env.<name>]`.
- `dojo --env prod ...` merges `[env.prod]` over the root config.
- This lets you keep shared defaults at the top level and only override what changes per environment.

Example:

```toml
default_env = "demo"

[env.demo]
host = "https://demo.defectdojo.org/"
user = "admin"
password = "..."

[env.local]
host = "http://localhost:8080"
token = "your-api-token"
disable_tls = true
```

With this file:

- `dojo status` uses the `demo` environment because of `default_env`
- `dojo --env local status` uses `http://localhost:8080`, the `local` token, and disables TLS verification
- `dojo -e local --host https://dojo.example.com status` uses the `local` config but overrides `host` from the command line
