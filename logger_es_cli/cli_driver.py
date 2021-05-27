#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# cli_driver.py
# @Author : Gustavo Freitas (gustavo@gmf-tech.com)
# @Link   :
# from logger_es_cli.dafaults import decorator_factory
from typing import Optional
import typer
import os
from logger_es_cli import logger_factory, logger
import sys
import time
import ujson as json

app = typer.Typer()


@app.command("zum")
def zum(message: str):
    typer.echo(f"{message}")


@app.command("start_system")
def start_system(
    message: str,
    exclude_default: bool = typer.Option(True, envvar="EXCLUDE_DEFAULT"),
    custom_file: Optional[typer.FileText] = typer.Option(None, envvar="CUSTOM_FILE"),
    kibana_ssl: bool = typer.Option(True, envvar="KIBANA_SSL"),
    exclude: str = typer.Option("", envvar="EXCLUDE"),
    save_filepath: str = typer.Option("/tmp", envvar="SAVE_FILEPATH"),
    save_file: bool = typer.Option(False, envvar="SAVE_FILE"),
    kibana_server: str = typer.Option("127.0.0.1", envvar="KIBANA_SERVER"),
    kibana_username: str = typer.Option("robots", envvar="KIBANA_USERNAME"),
    kibana_password: str = typer.Option("127456", envvar="KIBANA_PASSWORD"),
    kibana_server_port: int = typer.Option(443, envvar="KIBANA_SERVER_PORT"),
    environment: str = typer.Option("DEVELOPMENT", envvar="ENVIRONMENT"),
    project_name: str = typer.Option("test-index", envvar="PROJECT_NAME"),
):
    kibana_config = {
        "kibana_username": kibana_username,
        "kibana_server_port": kibana_server_port,
        "kibana_password": kibana_password,
        "kibana_server": kibana_server,
        "kibana_ssl": kibana_ssl,
    }

    extra_args = {}
    if custom_file:
        extra_args = json.loads(custom_file.read())

    logger_factory(
        funcname=sys._getframe().f_code.co_name,
        exclude_default=exclude_default,
        exclude=exclude,
        kibana_config=kibana_config,
        enable_file_log=save_file,
        path_log_file=save_filepath,
        environment=environment,
        project_name=project_name,
    )

    logger.info(message, extra=extra_args)
    logger.warning(message, extra=extra_args)
    logger.debug(message, extra=extra_args)
    logger.error(message, extra=extra_args)

    typer.echo(
        f"send message to kibana:  [{message} {kibana_server}:{kibana_server_port}]!"
    )

    time.sleep(2)
