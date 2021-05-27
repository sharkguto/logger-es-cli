#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# cli_driver.py
# @Author : Gustavo Freitas (gustavo@gmf-tech.com)
# @Link   :
# from logger_es_cli.dafaults import decorator_factory
import typer
import os

app = typer.Typer()


kibana_server = typer.Argument("127.0.0.1", envvar="KIBANA_SERVER")
kibana_username = typer.Argument("robots", envvar="KIBANA_USERNAME")
kibana_password = typer.Argument("127456", envvar="KIBANA_PASSWORD")
kibana_server_port = typer.Argument(443, envvar="KIBANA_SERVER_PORT")
environment = typer.Argument("DEVELOPMENT", envvar="ENVIRONMENT")
project_name = typer.Argument("test-index", envvar="PROJECT_NAME")


# @decorator_factory("default")
@app.command()
def start_system(
    message: str = "ok",
    kibana_server: str = typer.Argument("127.0.0.1", envvar="KIBANA_SERVER"),
    kibana_username: str = typer.Argument("robots", envvar="KIBANA_USERNAME"),
    kibana_password: str = typer.Argument("127456", envvar="KIBANA_PASSWORD"),
    kibana_server_port: int = typer.Argument(443, envvar="KIBANA_SERVER_PORT"),
    environment: str = typer.Argument("DEVELOPMENT", envvar="ENVIRONMENT"),
    project_name: str = typer.Argument("test-index", envvar="PROJECT_NAME"),
):

    typer.echo(
        f"send message to kibana:  [{message} {kibana_server}:{kibana_server_port}]!"
    )
    typer.echo(f"username:  [{kibana_username}]!")
