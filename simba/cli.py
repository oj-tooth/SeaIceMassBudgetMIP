"""
cli.py

Description: Main command line interface for Sea Ice Mass Budget Analysis package.

Created By: Ollie Tooth (oliver.tooth@noc.ac.uk)
"""

# -- Import dependencies -- #
import logging

import typer
from typing_extensions import Annotated, Optional

from simba.pipeline import describe_simba_pipeline, run_simba_pipeline

from .__init__ import __version__

app = typer.Typer()
logger = logging.getLogger(__name__)

# -- Define CLI Functions -- #
def create_header() -> None:
    """
    Add Sea Ice Mass Budget Analysis header to log.
    """
    logger.info(
        f"""
   ⦿──⦿──⦿──⦿──⦿──⦿──⦿──⦿──⦿──⦿──⦿──⦿
       Sea Ice Mass Budget Analysis      
   ⦿──⦿──⦿──⦿──⦿──⦿──⦿──⦿──⦿──⦿──⦿──⦿

        version: {__version__}

""",
        extra={"simple": True},
    )


def init_logging(
    log_filepath: str
    ) -> None:
    """
    Initialise Sea Ice Mass Budget Analysis logging.

    Parameters:
    -----------
    log_filepath : str | None
        Filepath to log file. If None, logs to 'simba.log'.
    """
    # Verify input:
    if not isinstance(log_filepath, str):
        raise TypeError("log_filepath must be a string.")

    logging.basicConfig(
        format="⦿──⦿  SIMBA  ⦿──⦿  | %(levelname)10s | %(asctime)s | %(message)s",
        level=logging.INFO,
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.FileHandler(log_filepath),
            logging.StreamHandler()
    ]
    )


# -- Create Typer App -- #
@app.callback()
def main():
    pass

@app.command()
def run(
    config: Annotated[str, typer.Argument(help="Path to SIMBA config .toml file")],
    log: Annotated[
        Optional[str],
        typer.Option(help="Path to write SIMBA log file", rich_help_panel="Options")
    ] = "simba.log",
    dry_run: Annotated[
        Optional[bool],
        typer.Option(help="Describe SIMBA pipeline without running", rich_help_panel="Options")
    ] = False,
) -> None:
    """
    Run SIMBA using configuration (.toml) file in current process.
    """
    # -- Initialise Logging -- #
    init_logging(log_filepath=log)
    create_header()

    # -- Run SIMBA Workflow -- #
    args = {
        "config_file": config,
        "log_filepath": log,
        "dry_run": dry_run,
    }
    if dry_run:
        describe_simba_pipeline(args=args)
    else:
        run_simba_pipeline(args=args)

    logging.info("✔ SIMBA Completed ✔")

if __name__ == "__main__":
    app()