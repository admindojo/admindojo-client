# -*- coding: utf-8 -*-

"""Console script for admindojo_client."""
import sys
import click
import admindojo_client.admindojo_client as admindojo

@click.command()
def main(args=None):
    """Console script for admindojo_client."""
    admindojo.main()
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
