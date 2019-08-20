import click
from quote_scraper import get_quote


@click.command()
@click.option(
    "-t",
    "--type",
    type=click.Choice(["love", "art", "funny", "main", "nature"]),
    default="main",
)
def quote(type):
    quote, author = get_quote(type)
    output_quote_box(quote, author)


def output_quote_box(quote: str, author: str) -> str:
    box_top_bottom = " " + "~" * (len(quote) + 2) + " "
    box_mid = "| " + " " * len(quote) + " |"
    box_quote = "| " + quote + " |"
    box_author = "| - " + author + " " * (len(quote) - len(author) - 2) + " |"
    click.echo(box_top_bottom)
    click.echo(box_mid)
    click.echo(box_quote)
    click.echo(box_author)
    click.echo(box_mid)
    click.echo(box_top_bottom)


if __name__ == "__main__":
    quote()
